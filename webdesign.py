import asyncio
import os
import json
from base_agent import BaseAgent
from webserver import Webserver
from utils import get_openai_url,write_file,get_content_between_a_b,wrap_func,extract_img_from_html,create_file,extract,modify_input_dict,cal_cost,extract_dimensions,get_html_css_js_from_response
import re
import argparse
from prompts import *

class WebDesignAgent(BaseAgent):
    def __init__(self, model="gpt4o-0513",save_file = "saves/",**kwargs) -> None:
        super().__init__(model)
        self.task = {"img":None,"text":None}
        self.task_queue = []
        self.memory = []
        with open("logs/token.json", "r") as f:
            tokens = json.load(f)
        self.begin_prompt_tokens = tokens[self.model][0]
        self.begin_completion_tokens = tokens[self.model][1]
        self.max_cost_prompt_tokens = 1000000
        self.max_cost_completion_tokens = 1000000
        self.webserver = None
        self.webserver = Webserver(save_file)
        self.user_feedback = None
        if not os.path.exists(save_file):
            os.makedirs(save_file)
        # ["Tailwind","Boostrap","Materialize","Bulma",None]
        self.css_frame = "Tailwind"
        self.save_file = save_file
        self.total_prompt_cost_tokens = 0
        self.total_completion_cost_tokens = 0
        self.refine_times = 2
    
    def act(self,**kwargs):
        self.publish_task(**kwargs)
        self.deal_task()
        return "done"
    
    def deal_task(self):
        print("Planning the website...")
        self.plan()
        print("Successfully planned the website.")
        pages = self.task_queue
        asyncio.run(self.deal_task_async(pages))
    
    async def deal_task_async(self,pages):
        tasks = []
        for page_info in pages:
            task = self.generate_and_refine_single_page_async(page_info)
            tasks.append(task)
        await asyncio.gather(*tasks)
    
    def change_save_file(self,save_file):
        self.save_file = save_file
        self.webserver.save_path = save_file
        if not os.path.exists(save_file):
            os.makedirs(save_file)

    def chat(self, query, **kwargs):
        self.memory.append({"role":"user","content":query})
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]
        response = wrap_func(self.get_answer, messages=self.memory, **kwargs)
        self.memory.append({"role":"assistant","content":response})
        return response

    def publish_task(self,img = None, text = None,refine_times= None,max_cost_prompt_tokens = 1000000,max_cost_completion_tokens = 1000000):
        self.task = {"img":img,"text":text}
        self.max_cost_prompt_tokens = max_cost_prompt_tokens
        self.max_cost_completion_tokens = max_cost_completion_tokens
        self.refine_times = refine_times if refine_times else 2

    
    def check_cost(self):
        with open("logs/token.json", "r") as f:
            tokens = json.load(f)
        current_prompt_tokens = tokens[self.model][0]
        current_completion_tokens = tokens[self.model][1]
        self.total_prompt_cost_tokens = current_prompt_tokens - self.begin_prompt_tokens
        self.total_completion_cost_tokens = current_completion_tokens - self.begin_completion_tokens
        if self.total_prompt_cost_tokens > self.max_cost_prompt_tokens or self.total_completion_cost_tokens > self.max_cost_completion_tokens:
            return False
        return True


    def plan(self):
        if os.path.exists(os.path.join(self.save_file,"pages.json")):
            with open(os.path.join(self.save_file,"pages.json"), "r",encoding='utf-8') as f:
                self.task_queue = json.load(f)
            return self.task_queue
        text = self.task["text"]
        img = self.task["img"]
        print(self.css_frame)
        prompt = get_plan_prompt(text=text,img=img,css_frame=self.css_frame)
        if img:
            messages = [
                {"role":"user","content":[
                    {"type":"image_url","image_url":{"url":get_openai_url(img),"detail":"high"}},
                    {"type":"text","text":prompt},
            ]},
            ]
        else:
            messages = [
                {"role":"user","content":[
                    {"type":"text","text":prompt},
            ]},
            ]
        try_cnt = 0
        while try_cnt < 3:
            response = wrap_func(self.get_answer, messages=messages,wrap_text="Planning now...")
            try:
                pages = response.split("Designed pages:")[-1]
                pages = pages.strip()
                pages = json.loads(pages)
                break
            except:
                print(response)
                try_cnt += 1
                print("Failed to get the designed pages. try again")
        if try_cnt == 3:
            assert False, "Failed to get the designed pages."
        
        new_pages = asyncio.run(self.refine_pages_async(pages))
        new_pages = sorted(new_pages,key = lambda x:x[1])
        new_pages = [page[0] for page in new_pages]
        self.task_queue = new_pages
        print("The pages have been designed.")
        save_path = os.path.join(self.save_file,"pages.json")
        with open(save_path, "w",encoding='utf-8') as f:
            json.dump(self.task_queue,f)
        return self.task_queue
    
    async def refine_pages_async(self,pages):
        tasks = []
        for i,page in enumerate(pages):
            task = self.refine_page_async(i,page)
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results
    

    def get_modified_page_from_response(self,response,page_info):
        modified_page = response.split("modified_page:")[-1].strip()
        if "```python" in modified_page:
            modified_page = get_content_between_a_b("```python","```",modified_page)
        if "```json" in modified_page:
            modified_page = get_content_between_a_b("```json","```",modified_page)
        modified_page = modified_page.replace("True","true").replace("False","false")
        try:
            modified_page = json.loads(modified_page)
        except:
            modified_page = modify_input_dict(modified_page)
            try:
                modified_page = json.loads(modified_page)
            except:
                print("Failed to get the modified page. Please check the format.")
                print(modified_page)
                modified_page = page_info
        return modified_page       


    def refine_page(self,page_info):
        task = self.task["text"]
        task_info = f"The requirements of the website is {task}" if self.task["text"] else ""
        prompt = get_refine_page_prompt(task_info=task_info,page_info=page_info,css_frame=self.css_frame)
        messages = [
            {"role":"user","content":[
                {"type":"text","text":prompt},
        ]},
        ]
        response = wrap_func(self.get_answer, messages=messages,wrap_text="Refining page now...")
        modified_page = self.get_modified_page_from_response(response,page_info)
        print(f"Page has been refined.")
        return modified_page
    
    async def refine_page_async(self,idx,page_info):
        task = self.task["text"]
        task_info = f"The requirements of the website is {task}" if self.task["text"] else ""
        prompt = get_refine_page_prompt(task_info=task_info,page_info=page_info,css_frame=self.css_frame)
        messages = [
            {"role":"user","content":[
                {"type":"text","text":prompt},
        ]},
        ]
        response = await self.get_answer_async(messages=messages)
        modified_page = self.get_modified_page_from_response(response,page_info)
        print(f"Page {idx+1} has been refined.")
        return [modified_page,idx]


    def get_write_original_website_messages(self,page_info):
        img = self.task["img"] if page_info["is_main_page"] else None
        text = self.task["text"]
        prompt = get_write_original_website_prompt(text=text,img=img,page_info=page_info,css_frame=self.css_frame)
        if img:
            messages = [
                {"role":"user","content":[
                    {"type":"image_url","image_url":{"url":get_openai_url(img),"detail":"high"}},
                    {"type":"text","text":prompt},
            ]},
            ]
        else:
            messages = [
                {"role":"user","content":[
                    {"type":"text","text":prompt},
            ]},
            ]       
        return messages 

    def write_original_website(self,page_info):
        if "html_name" not in page_info:
            print("The page_info is not correct.")
            return
        messages = self.get_write_original_website_messages(page_info)
        html,css,js,cnt = None,None,None,0
        while not html and cnt < 5 or (not self.css_frame and (not css or not js)):
            response = wrap_func(self.get_answer, messages=messages,wrap_text="Writing original website now...")
            html,css,js = get_html_css_js_from_response(response)
            cnt += 1
        if not html or (not self.css_frame and (not css or not js)):
            print(response)
            assert False, "Failed to get the original website."
        self.update_html_css_js(page_info,html,css,js)
    
    async def write_original_website_async(self,page_info):
        if "html_name" not in page_info:
            print("The page_info is not correct.")
            return
        messages = self.get_write_original_website_messages(page_info)
        html,css,js,cnt = None,None,None,0
        while not html and cnt < 5 or (not self.css_frame and (not css or not js)):
            response = await self.get_answer_async(messages=messages)
            html,css,js = get_html_css_js_from_response(response)
            cnt += 1
        if not html or (not self.css_frame and (not css or not js)):
            print(response)
            assert False, "Failed to get the original website."
        await self.update_html_css_js_async(page_info,html,css,js)
        page_name = page_info["html_name"]
        print(f"Original website has been written to {page_name}")

    def get_refine_messages(self,page_info):
        html_name = page_info["html_name"]
        css_name = page_info["css_name"] if "css_name" in page_info else None
        js_name = page_info["js_name"] if "js_name" in page_info else None
        img = self.task["img"] if page_info["is_main_page"] else None
        text = self.task["text"]
        css_frame = self.css_frame
        html_path = os.path.join(self.save_file,html_name)
        css_path = os.path.join(self.save_file,css_name) if css_name else None
        js_path = os.path.join(self.save_file,js_name) if js_name else None

        html_code = open(html_path,encoding='utf-8').read()
        css_code = open(css_path,encoding='utf-8').read() if css_name else None
        js_code = open(js_path,encoding='utf-8').read() if js_name else None
        page_name = html_name.split(".")[0]
        page_img_path = os.path.join(self.save_file,f"{page_name}.png")

        feedback = f"The user feedback on the webpage(Very important! You must pay extra attention to the content here and prioritize making modifications to it) is : {self.user_feedback}" if self.user_feedback else ""
        prompt = get_refine_prompt(text=text,img=img,html_code=html_code,css_code=css_code,js_code=js_code,feedback=feedback,page_info=page_info,css_frame=css_frame)
        if img:
            messages = [
                {"role":"user","content":[
                    {"type":"image_url","image_url":{"url":get_openai_url(img),"detail":"high"}},
                    {"type":"image_url","image_url":{"url":get_openai_url(page_img_path),"detail":"high"}},
                    {"type":"text","text":prompt},
            ]},
            ]
        else:
            messages = [
                {"role":"user","content":[
                    {"type":"image_url","image_url":{"url":get_openai_url(page_img_path),"detail":"high"}},
                    {"type":"text","text":prompt},
            ]},
            ]
        return messages

    def refine(self,page_info):
        if "html_name" not in page_info:
            print("The page_info is not correct.")
            return
        messages = self.get_refine_messages(page_info)
        response = wrap_func(self.get_answer, messages=messages,wrap_text="Refining now...")
        html_code,css_code,js_code = get_html_css_js_from_response(response)
        self.update_html_css_js(page_info,html_code,css_code,js_code)
    
    async def refine_async(self,page_info):
        if "html_name" not in page_info:
            print("The page_info is not correct.")
            return
        messages = self.get_refine_messages(page_info)
        response = await self.get_answer_async(messages=messages)
        html_code,css_code,js_code = get_html_css_js_from_response(response)
        await self.update_html_css_js_async(page_info,html_code,css_code,js_code)
        page_name = page_info["html_name"]
        print(f"Page {page_name} has been refined.")


    async def generate_and_refine_single_page_async(self,page_info):
        print(f"Generating and refining page {page_info['html_name']}")
        await self.write_original_website_async(page_info)
        print(f"Original website has been written.")
        for _ in range(self.refine_times):
            print(f"Refining page {page_info['html_name']} {_} times.")
            await self.refine_async(page_info)
            print(f"Page {page_info['html_name']} has been refined.")
        

    def update_html_css_js(self,page_info,html,css,js):
        html_name = page_info["html_name"]
        css_name = page_info["css_name"] if "css_name" in page_info else None
        js_name = page_info["js_name"] if "js_name" in page_info else None
        if not self.css_frame:
            if not css_name or not js_name:
                print("The css_name or js_name is not provided.")
                return
            write_file(os.path.join(self.save_file,html_name), html)
            write_file(os.path.join(self.save_file,css_name), css)
            write_file(os.path.join(self.save_file,js_name), js)
            asyncio.run(self.add_imgs_async(html,os.path.join(self.save_file,html_name)))
        else:
            write_file(os.path.join(self.save_file,html_name), html)
            asyncio.run(self.add_imgs_async(html,os.path.join(self.save_file,html_name)))
        page_name = html_name.split(".")[0]
        page_img_path = os.path.join(self.save_file,f"{page_name}.png")
        self.webserver.get_screenshot(os.path.join(self.save_file,html_name),page_img_path)
        print(f"Screenshot has been saved to {page_img_path}")
    
    async def update_html_css_js_async(self,page_info,html,css,js):
        html_name = page_info["html_name"]
        css_name = page_info["css_name"] if "css_name" in page_info else None
        js_name = page_info["js_name"] if "js_name" in page_info else None
        if not self.css_frame:
            if not css_name or not js_name:
                print("The css_name or js_name is not provided.")
                return
            write_file(os.path.join(self.save_file,html_name), html)
            write_file(os.path.join(self.save_file,css_name), css)
            write_file(os.path.join(self.save_file,js_name), js)
            await self.add_imgs_async(html,os.path.join(self.save_file,html_name))
        else:
            write_file(os.path.join(self.save_file,html_name), html)
            await self.add_imgs_async(html,os.path.join(self.save_file,html_name))
        page_name = html_name.split(".")[0]
        page_img_path = os.path.join(self.save_file,f"{page_name}.png")
        self.webserver.get_screenshot(os.path.join(self.save_file,html_name),page_img_path)
        print(f"Screenshot has been saved to {page_img_path}")

    def complete_page(self,pages,idx):
        page_info = pages[idx]
        page_info = str(page_info)
        other_pages_info = ""
        for i,page in enumerate(pages):
            if i != idx:
                other_pages_info += f"Page {i+1}: {page}\n"
        other_pages_info = modify_input_dict(other_pages_info)
        page_info = modify_input_dict(page_info)
        prompt = page_complete_prompt.format(other_pages_info=other_pages_info,page_info=page_info)
        messages = [
            {"role":"user","content":[
                {"type":"text","text":prompt},
        ]},
        ]
        response = wrap_func(self.get_answer, messages=messages,wrap_text="Completing page now...")
        complete_page = extract(response,"completed_page")
        if "```python" in complete_page:
            complete_page = get_content_between_a_b("```python","```",complete_page)
        elif "```json" in complete_page:
            complete_page = get_content_between_a_b("```json","```",complete_page)
        try:
            complete_page = json.loads(complete_page)
            relationship = complete_page["relationship"]
            if isinstance(relationship,str):
                relationship = modify_input_dict(relationship)
                relationship = json.loads(relationship)
            complete_page["relationship"] = relationship
            pages[idx] = complete_page
        except:
            print("Failed to get the completed page. Please check the format.")
            print(complete_page)
        relationship = extract(response,"page_relationship")
        if "```python" in relationship:
            relationship = get_content_between_a_b("```python","```",relationship)
        elif "```json" in relationship:
            relationship = get_content_between_a_b("```json","```",relationship)
        try:
            relationship = json.loads(relationship)
            for page_relation in relationship:
                html_name = page_relation["html_name"]
                button_name = page_relation["button_name"]
                for i,page in enumerate(pages):
                    if page["html_name"] == html_name:
                        pages[i]["relationship"]["buttons"].append({"button_name": button_name,"jump_page":complete_page["html_name"]})
        except:
            print("Failed to get the relationship. Please check the format.")
            print(relationship)
        return pages
    

    async def add_imgs_async(self,html_code,html_path):
        img_contents = extract_img_from_html(html_code)
        tasks = []
        for img_content in img_contents:
            task = self.add_img_async(img_content,html_code,html_path)
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results


    async def add_img_async(self,img_content,html_code,html_path):
        src = img_content["src"]
        alt = img_content["alt"]
        if not src.startswith("https://placehold.co"):
            return
        img = await self.get_img_async(alt)
        self.save_img_and_update_html(img,img_content,html_code,html_path)

    
    async def get_img_async(self,description):
        img = await self.img_generator.get_img_async(description)
        return img


    def add_imgs(self,html_code,html_path):
        img_contents = extract_img_from_html(html_code)
        for img_content in img_contents:
            src = img_content["src"]
            alt = img_content["alt"]
            if not src.startswith("https://placehold.co"):
                continue
            img = self.get_img(alt)
            self.save_img_and_update_html(img,img_content,html_code,html_path)

    def get_img(self,description):
        img = self.img_generator.get_img(description)
        return img

    def save_img_and_update_html(self,img,img_content,html_code,html_path):
        src = img_content["src"]
        alt = img_content["alt"]
        original = img_content["original"]
        width,height = extract_dimensions(src)
        for i in range(10000):
            img_name = f"img_{i}.png"
            img_path = os.path.join(self.save_file,img_name)
            if not os.path.exists(img_path):
                break
        create_file(img_path)
        img.save(img_path)
        html_code = open(html_path,encoding='utf-8').read()
        if "class" in img_content:
            img_class = img_content["class"]
            html_code = html_code.replace(original,f'src="{img_name}" alt="{alt}" class="{img_class}" style="width: {width}px; height: {height}px;"')
        else:
            html_code = html_code.replace(original,f'src="{img_name}" alt="{alt}" style="width: {width}px; height: {height}px;"')
        with open(html_path, "w",encoding='utf-8') as f:
            f.write(html_code)
        print(f"Image {img_path} has been added to the folder.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--save_file", type=str, default="saves/shopping/")
    parser.add_argument("--text", type=str, default=None)
    parser.add_argument("--img", type=str, default=None)
    parser.add_argument("--refine_times", type=int, default=2)
    
    args = parser.parse_args()
    save_file = args.save_file
    text = args.text
    img = args.img
    refine_times = args.refine_times
    agent = WebDesignAgent(save_file=save_file)
    agent.act(text = text,img = img,refine_times = refine_times)
    print(f"Total prompt cost tokens: {agent.total_prompt_cost_tokens}, Total completion cost tokens: {agent.total_completion_cost_tokens}")
    cost = cal_cost(agent.total_prompt_cost_tokens,agent.total_completion_cost_tokens)
    print(f"Total cost: {cost}")

