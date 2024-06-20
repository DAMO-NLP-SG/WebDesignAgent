import os
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://agent-eastus.openai.azure.com/"
os.environ["AZURE_OPENAI_KEY"] = "8d97baf24d6341deb01e30ba04d389e8"
os.environ["AZURE_OPENAI_API_VERSION"] = "2024-02-01"

import json
from base_agent import BaseAgent
from webserver import Webserver
from utils import get_openai_url,write_file,get_content_between_a_b,wrap_func,extract_img_from_html,create_file,extract,modify_input_dict,cal_cost
from LLM import get_openai_imgs
import re
from prompt import *


class WebDesignAgent(BaseAgent):
    def __init__(self, model="gpt4o-0513",save_file = "saves/") -> None:
        super().__init__(model)
        self.task = None
        self.task_queue = []
        self.memory = []
        with open("logs/token.json", "r") as f:
            tokens = json.load(f)
        self.begin_prompt_tokens = tokens[self.model][0]
        self.begin_completion_tokens = tokens[self.model][1]
        self.max_cost_prompt_tokens = 100000
        self.max_cost_completion_tokens = 100000
        self.webserver = None
        self.webserver = Webserver(save_file)
        self.user_feedback = None
        if not os.path.exists(save_file):
            os.makedirs(save_file)
        self.save_file = save_file
        self.total_prompt_cost_tokens = 0
        self.total_completion_cost_tokens = 0
    
    def act(self,**kwargs):
        self.publish_task(**kwargs)
        self.deal_task()
        return "done"
    
    def deal_task(self,refine_times = 2):
        self.plan()
        for page_info in self.task_queue:
            cnt = 0
            self.write_original_website(page_info)
            while cnt < refine_times and self.check_cost():
                self.refine(page_info)
                cnt += 1
    
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

    def publish_task(self,img = None, text = None,max_cost_prompt_tokens = 100000,max_cost_completion_tokens = 100000):
        self.task = {"img":img,"text":text}
        self.max_cost_prompt_tokens = max_cost_prompt_tokens
        self.max_cost_completion_tokens = max_cost_completion_tokens

    
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
            with open(os.path.join(self.save_file,"pages.json"), "r") as f:
                self.task_queue = json.load(f)
            return self.task_queue
        text = self.task["text"]
        img = self.task["img"]
        prompt = get_plan_prompt(text=text,img=img)
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
            try:
                response = wrap_func(self.get_answer, messages=messages,wrap_text="Planning now...")
                pages = response.split("Designed pages:")[-1]
                pages = pages.strip()
                pages = json.loads(pages)
                break
            except:
                try_cnt += 1
                print("Failed to get the designed pages. try again")
        if try_cnt == 3:
            assert False, "Failed to get the designed pages."
        new_pages = []
        for i,page in enumerate(pages):
            page = self.refine_page(page)
            print(f"Page {i+1}: {page}")
            new_pages.append(page)
        self.task_queue = new_pages
        print("The pages have been designed.")
        save_path = os.path.join(self.save_file,"pages.json")
        with open(save_path, "w") as f:
            json.dump(self.task_queue,f)
        return self.task_queue
        
    def refine_page(self,page_info):
        task = self.task["text"]
        task_info = f"The requirements of the website is {task}" if self.task["text"] else ""
        prompt = refine_page_prompt.format(task_info=task_info,page_info=page_info)
        messages = [
            {"role":"user","content":[
                {"type":"text","text":prompt},
        ]},
        ]
        response = wrap_func(self.get_answer, messages=messages,wrap_text="Refining page now...")
        modified_page = response.split("modified_page:")[-1].strip()
        modified_page = modify_input_dict(modified_page)
        if "```python" in modified_page:
            modified_page = get_content_between_a_b("```python","```",modified_page)
        if "```json" in modified_page:
            modified_page = get_content_between_a_b("```json","```",modified_page)
        try:
            modified_page = json.loads(modified_page)
        except:
            print("Failed to get the modified page. Please check the format.")
            print(modified_page)
            print("##############################################")
            modified_page = page_info
        return modified_page


    def refine(self,page_info):
        self.refine_details(page_info)
        self.refine_layout(page_info)
        

    def refine_details(self,page_info):
        html_name = page_info["html_name"]
        css_name = page_info["css_name"]
        js_name = page_info["js_name"]
        img = self.task["img"] if page_info["is_main_page"] else None
        text = self.task["text"]
        html_code = open(os.path.join(self.save_file,html_name)).read()
        css_code = open(os.path.join(self.save_file,css_name)).read()
        js_code = open(os.path.join(self.save_file,js_name)).read()
        page_name = html_name.split(".")[0]
        page_img_path = os.path.join(self.save_file,f"{page_name}.png")

        feedback = f"The user feedback on the website(Very important! You must pay extra attention to the content here and prioritize making modifications to it) is : {self.user_feedback}" if self.user_feedback else ""
        prompt = get_refine_prompt(text=text,img=img,html_code=html_code,css_code=css_code,js_code=js_code,feedback=feedback,page_info=page_info)
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
        response = wrap_func(self.get_answer, messages=messages,wrap_text="Refining now...")
        html = get_content_between_a_b("```html", "```", response) if "```html" in response else html_code
        css = get_content_between_a_b("```css", "```", response) if "```css" in response else css_code
        js = get_content_between_a_b("```javascript", "```", response) if "```javascript" in response else js_code
        js = get_content_between_a_b("```js", "```", response) if "```js" in response else js
        if html:
            write_file(os.path.join(self.save_file,html_name), html)
        if css:
            write_file(os.path.join(self.save_file,css_name), css)
        if js:
            write_file(os.path.join(self.save_file,js_name), js)
        self.add_imgs(html,js)
        print(f"Refined website has been written to {html_name}, {css_name}, {js_name}")
        self.webserver.get_screenshot(os.path.join(self.save_file,html_name),page_img_path)


    def refine_layout(self,page_info):
        html_name = page_info["html_name"]
        html_code = open(os.path.join(self.save_file,html_name)).read()
        css_name = page_info["css_name"]
        css_code = open(os.path.join(self.save_file,css_name)).read()
        img = self.task["img"] if page_info["is_main_page"] else None
        text = self.task["text"]
        feedback = f"The feedback provided by users regarding the current implementation effect of your code is very important. Please take it seriously and make modifications based on user feedback!\n The user's feedback is:{self.user_feedback}" if self.user_feedback else ""
        prompt = get_refine_layout_prompt(text=text,img=img,html_code=html_code,css_code=css_code,feedback=feedback)
        page_name = html_name.split(".")[0]
        page_img_path = os.path.join(self.save_file,f"{page_name}.png")
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

        response = wrap_func(self.get_answer, messages=messages,wrap_text="Refining CSS now...")
        css = get_content_between_a_b("```css", "```", response) if "```css" in response else css_code
        html = get_content_between_a_b("```html", "```", response) if "```html" in response else html_code
        if css:
            write_file(os.path.join(self.save_file,css_name), css)
            print(f"Refined CSS has been written to {css_name}")
        if html:
            write_file(os.path.join(self.save_file,html_name), html)
            print(f"Refined HTML has been written to {html_name}")
        self.add_imgs(html,"")
        self.webserver.get_screenshot(os.path.join(self.save_file,html_name),page_img_path)


    def write_original_website(self,page_info):
        html_name = page_info["html_name"]
        css_name = page_info["css_name"]
        js_name = page_info["js_name"]
        img = self.task["img"] if page_info["is_main_page"] else None
        text = self.task["text"]
        prompt = get_write_original_website_prompt(text=text,img=img,page_info=page_info)
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
        html,css,js = None,None,None
        cnt = 0
        while not html or not css or not js and cnt < 5:
            response = wrap_func(self.get_answer, messages=messages,wrap_text="Writing original website now...")
            html = get_content_between_a_b("```html", "```", response) if "```html" in response else None
            css = get_content_between_a_b("```css", "```", response) if "```css" in response else None
            js = get_content_between_a_b("```javascript", "```", response) if "```javascript" in response else None
            js = get_content_between_a_b("```js", "```", response) if "```js" in response else js
            cnt += 1
        if not html or not css or not js:
            print(response)
            assert False, "Failed to get the original website."
        write_file(os.path.join(self.save_file,html_name), html)
        write_file(os.path.join(self.save_file,css_name), css)
        write_file(os.path.join(self.save_file,js_name), js)
        self.add_imgs(html,js)
        print(f"Original website has been written to {html_name}, {css_name}, {js_name}")
        page_name = html_name.split(".")[0]
        page_img_path = os.path.join(self.save_file,f"{page_name}.png")
        self.webserver.get_screenshot(os.path.join(self.save_file,html_name),page_img_path)
    
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
            print("##############################################")
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
            print("##############################################")
        return pages
    
    def add_imgs(self,html_code,js_code):
        img_contents = extract_img_from_html(html_code)
        for img_content in img_contents:
            img_path = os.path.join(self.save_file,img_content["src"])
            if os.path.exists(img_path) or "description" not in img_content or not img_path.split(".")[1] in ["jpg","png","jpeg"]:
                continue
            img_description = img_content["description"]
            img = self.get_img(img_description)
            create_file(img_path)
            img.save(img_path)
            print(f"Image {img_path} has been added to the folder.")
        pattern = re.compile(r'\{[^}]*?imgSrc:\s*(?:\'|")(.*?)(?:\'|")[^}]*?description:\s*(?:\'|")(.*?)(?:\'|")[^}]*\}')
        matches = pattern.findall(js_code)
        results = [{'imgSrc': match[0], 'description': match[1]} for match in matches]
        for result in results:
            img_path = os.path.join(self.save_file,result["imgSrc"])
            if os.path.exists(img_path):
                continue
            img_description = result["description"]
            img = self.get_img(img_description)
            create_file(img_path)
            img.save(img_path)
            print(f"Image {img_path} has been added to the folder.")
        return html_code

    def get_img(self,description):
        task = self.task["text"]
        description = f"This is a img used for the website({task}),The description of the img is:{description}" if self.task["text"] else description
        img = get_openai_imgs(description)
        return img


if __name__ == "__main__":
    agent = WebDesignAgent(save_file="saves/shopping/")
    agent.act(text = "a shopping website")
    print(f"Total prompt cost tokens: {agent.total_prompt_cost_tokens}, Total completion cost tokens: {agent.total_completion_cost_tokens}")
    cost = cal_cost(agent.total_prompt_cost_tokens,agent.total_completion_cost_tokens)
    print(f"Total cost: {cost}")
