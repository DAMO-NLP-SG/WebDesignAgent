import asyncio
import os
import json
import shutil
from bs4 import BeautifulSoup
from base_agent import BaseAgent
from webserver import Webserver
from utils import write_file,get_content_between_a_b,wrap_func,extract_img_from_html,create_file,extract,modify_input_dict,cal_cost,extract_dimensions,get_html_css_from_response,get_all_files_in_dir
from PIL import Image
import re
import argparse
import random
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
        self.gen_img = "Gen"
        self.local_img_storage = []
        self.local_img_storage_path = None
        self.local_img_storage_copy = []
        self.local_img_storage_en = []
        self.local_img_storage_zh = []
        self.language = "en"
        self.save_file = save_file
        self.total_prompt_cost_tokens = 0
        self.total_completion_cost_tokens = 0
        self.refine_times = 2
        self.vision = True
    
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
        feedback = self.user_feedback if self.user_feedback else ""
        prompt = get_plan_prompt(text=text,img=img,css_frame=self.css_frame,feedback=feedback,language=self.language,local_img_storage=self.local_img_storage)
        if img:
            messages = [
                {"role":"user","content":[
                    {"type":"image","url":img},
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
        print("Planning the website...")
        while try_cnt < 3:
            response = wrap_func(self.get_answer, messages=messages,wrap_text="Planning now...")
            try:
                pages = extract(response,"designed_pages")
                pages = pages.strip()
                pages = json.loads(pages)
                if self.css_frame:
                    for page in pages:
                        if "css_name" in page:
                            del page["css_name"]
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
        modified_page = extract(response,"modified_page")
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
        if self.css_frame:
            if "css_name" in modified_page:
                del modified_page["css_name"]
        return modified_page       


    def refine_page(self,page_info,feedback = ""):
        task = self.task["text"]
        prompt = get_refine_page_prompt(task=task,page_info=page_info,css_frame=self.css_frame,feedback=feedback,language=self.language,local_img_storage=self.local_img_storage)
        messages = [
            {"role":"user","content":[
                {"type":"text","text":prompt},
        ]},
        ]
        response = wrap_func(self.get_answer, messages=messages,wrap_text="Refining page now...")
        modified_page = self.get_modified_page_from_response(response,page_info)
        print(f"Page has been refined.")
        return modified_page
    
    async def refine_page_async(self,idx,page_info,feedback = ""):
        task = self.task["text"]
        prompt = get_refine_page_prompt(task=task,page_info=page_info,css_frame=self.css_frame,feedback=feedback,language=self.language,local_img_storage=self.local_img_storage)
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
        feedback = self.user_feedback if self.user_feedback else ""
        prompt = get_write_original_website_prompt(text=text,img=img,page_info=page_info,css_frame=self.css_frame,feedback=feedback,language=self.language)
        if img:
            messages = [
                {"role":"user","content":[
                    {"type":"image","url":img},
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
        html,css,cnt = None,None,0
        while not html and cnt < 5 or (not self.css_frame and not css):
            response = wrap_func(self.get_answer, messages=messages,wrap_text="Writing original website now...")
            html,css = get_html_css_from_response(response)
            cnt += 1
        if not html or (not self.css_frame and not css):
            print(response)
            assert False, "Failed to get the original website."
        self.update_html_css(page_info,html,css)
    
    async def write_original_website_async(self,page_info):
        if "html_name" not in page_info:
            print("The page_info is not correct.")
            return
        messages = self.get_write_original_website_messages(page_info)
        html,css,cnt = None,None,0
        while not html and cnt < 5 or (not self.css_frame and not css):
            response = await self.get_answer_async(messages=messages)
            html,css = get_html_css_from_response(response)
            cnt += 1
        if not html or (not self.css_frame and not css):
            print(response)
            assert False, "Failed to get the original website."
        await self.update_html_css_async(page_info,html,css)
        page_name = page_info["html_name"]
        print(f"Original website has been written to {page_name}")

    def get_refine_messages(self,page_info):
        html_name = page_info["html_name"]
        css_name = page_info["css_name"] if "css_name" in page_info else None
        img = self.task["img"] if page_info["is_main_page"] else None
        text = self.task["text"]
        css_frame = self.css_frame
        html_path = os.path.join(self.save_file,html_name)
        css_path = os.path.join(self.save_file,css_name) if css_name else None

        html_code = open(html_path,encoding='utf-8').read()
        css_code = open(css_path,encoding='utf-8').read() if css_name else None
        page_name = html_name.split(".")[0]
        page_img_path = os.path.join(self.save_file,f"{page_name}.png")

        feedback = self.user_feedback if self.user_feedback else ""

        if len(self.local_img_storage) > 10:
            local_img_storage = random.sample(self.local_img_storage,10)
        else:
            local_img_storage = self.local_img_storage
        prompt = get_refine_prompt(text=text,img=img,html_code=html_code,css_code=css_code,feedback=feedback,page_info=page_info,css_frame=css_frame,language=self.language,local_img_storage=local_img_storage,vision=self.vision)
        if self.vision == False:
            messages = [
                {"role":"user","content":[
                    {"type":"text","text":prompt},
            ]},
            ]
        elif img:
            messages = [
                {"role":"user","content":[
                    {"type":"image","url":img},
                    {"type":"image","url":page_img_path},
                    {"type":"text","text":prompt},
            ]},
            ]
        else:
            messages = [
                {"role":"user","content":[
                    {"type":"image","url":page_img_path},
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
        html_code,css_code = get_html_css_from_response(response)
        self.update_html_css(page_info,html_code,css_code)
    
    async def refine_async(self,page_info):
        if "html_name" not in page_info:
            print("The page_info is not correct.")
            return
        messages = self.get_refine_messages(page_info)
        response = await self.get_answer_async(messages=messages)
        html_code,css_code = get_html_css_from_response(response)
        await self.update_html_css_async(page_info,html_code,css_code)
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
        

    def update_html_css(self,page_info,html,css):
        html_name = page_info["html_name"]
        css_name = page_info["css_name"] if "css_name" in page_info else None
        print(self.gen_img)
        if not self.css_frame:
            if not css_name:
                print("The css_name is not provided.")
                return
            write_file(os.path.join(self.save_file,html_name), html)
            write_file(os.path.join(self.save_file,css_name), css)
            if self.gen_img == "Gen":
                html_code = asyncio.run(self.add_imgs_async(html))
                write_file(os.path.join(self.save_file,html_name), html_code)
        else:
            write_file(os.path.join(self.save_file,html_name), html)
            if self.gen_img == "Gen":
                print("begin add imgs")
                html_code = asyncio.run(self.add_imgs_async(html))
                write_file(os.path.join(self.save_file,html_name), html_code)
        page_name = html_name.split(".")[0]
        page_img_path = os.path.join(self.save_file,f"{page_name}.png")
        self.webserver.get_screenshot(os.path.join(self.save_file,html_name),page_img_path)
        print(f"Screenshot has been saved to {page_img_path}")
    
    async def update_html_css_async(self,page_info,html,css):
        html_name = page_info["html_name"]
        css_name = page_info["css_name"] if "css_name" in page_info else None
        if not self.css_frame:
            if not css_name:
                print("The css_name is not provided.")
                return
            write_file(os.path.join(self.save_file,html_name), html)
            write_file(os.path.join(self.save_file,css_name), css)
            if self.gen_img == "Gen":
                html_code = await self.add_imgs_async(html)
                write_file(os.path.join(self.save_file,html_name), html_code)
        else:
            write_file(os.path.join(self.save_file,html_name), html)
            if self.gen_img == "Gen":
                html_code = await self.add_imgs_async(html)
                write_file(os.path.join(self.save_file,html_name), html_code)
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
        feedback = self.user_feedback if self.user_feedback else ""
        task = self.task["text"] if self.task["text"] else ""
        prompt = get_page_complete_prompt(task = task,page_info=page_info,other_pages_info=other_pages_info,feedback=feedback,language=self.language,local_img_storage=self.local_img_storage)
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
    

    async def add_imgs_async(self,html_code):
        soup = BeautifulSoup(html_code, "html.parser")
        images = soup.find_all("img")
        scripts = soup.find_all("script")
        tasks = []

        tasks.append(self.add_imgs_to_background_async(html_code))
        for image in images:
            tasks.append(self.add_img_async(image))

        async def process_script(script):
            if script.string:
                script.string = await self.add_imgs_to_script_async(script.string)
        for script in scripts:
            tasks.append(process_script(script))
        await asyncio.gather(*tasks)
        return soup.prettify()
    
    async def add_imgs_to_background_async(self,html_code):
        # 正则表达式模式
        pattern = r"url\(['\"]?(.*?)['\"]?\)"
        # 搜索匹配
        matchs = re.findall(pattern, html_code)
        # 提取文件名
        for match in matchs:
            image_filename = match
            if "png" in image_filename or "jpg" in image_filename or "jpeg" in image_filename:
                img_name = os.path.basename(image_filename).split(".")[0]
                img_path = os.path.join(self.save_file,f"{img_name}.png")
                if os.path.exists(img_path):
                    continue
                text = self.task["text"] if self.task["text"] else ""
                if text:
                    description = f"This is a image used in the background of the website. The website description is: {text}, The image name is {img_name}."
                else:
                    description = f"This is a image used in the background of the website. The image name is {img_name}."
                img = await self.get_img_async(description)
                create_file(img_path)
                img.save(img_path)
                print(f"Image {img_path} has been added to the folder.")


    
    async def add_imgs_to_script_async(self,script):
        pattern = re.compile(r'{[^}]*\bimgsrc:\s*\'([^\']*)\'[^}]*\balt:\s*\'([^\']*)\'[^}]*}')
        for match in pattern.finditer(script):
            imgsrc = match.group(1)
            alt = match.group(2)
            img = await self.get_img_async(alt)
            image = self.save_img(img,{"src":imgsrc,"alt":alt})
            new_imgsrc = image["src"]
            old_segment = match.group(0)
            new_segment = old_segment.replace(imgsrc,new_imgsrc)
            script = script.replace(old_segment,new_segment,1)
        return script


    async def add_img_async(self,img_content):
        try:
            src = img_content["src"]
            alt = img_content["alt"]
        except:
            return 
        if os.path.exists(os.path.join(self.save_file,src)):
            return
        img = await self.get_img_async(alt)
        self.save_img(img,img_content)

    
    async def get_img_async(self,description):
        img = await self.img_generator.get_img_async(description)
        return img


    def add_imgs(self,html_code):
        soup = BeautifulSoup(html_code, "html.parser")
        images = soup.find_all("img")
        scripts = soup.find_all("script")
        for image in images:
            try:
                src = image["src"]
                alt = image["alt"]
            except:
                continue
            if os.path.exists(os.path.join(self.save_file,src)):
                continue
            img = self.get_img(alt)
            image = self.save_img(img,image)
        for script in scripts:
            if script.string:
                script.string = self.add_imgs_to_script(script.string)
        return soup.prettify()
    
    def add_imgs_to_script(self,script):
        pattern = re.compile(r'{[^}]*\bimgsrc:\s*\'([^\']*)\'[^}]*\balt:\s*\'([^\']*)\'[^}]*}')
        for match in pattern.finditer(script):
            imgsrc = match.group(1)
            alt = match.group(2)
            img = self.get_img(alt)
            image = self.save_img(img,{"src":imgsrc,"alt":alt})
            new_imgsrc = image["src"]
            old_segment = match.group(0)
            new_segment = old_segment.replace(imgsrc,new_imgsrc)
            script = script.replace(old_segment,new_segment,1)
        return script


    def get_img(self,description):
        img = self.img_generator.get_img(description)
        return img

    def save_img(self,img,image):
        src = image["src"]
        width,height = extract_dimensions(src)
        image["height"] = height
        image["width"] = width
        for i in range(10000):
            img_name = f"img_{i}.png"
            img_path = os.path.join(self.save_file,img_name)
            if not os.path.exists(img_path):
                break
        create_file(img_path)
        img.save(img_path)
        image["src"] = img_name
        print(f"Image {img_path} has been added to the folder.")
        return image

    def load_local_img_storage(self):
        local_img_storage_path = self.local_img_storage_path
        if os.path.exists(os.path.join(local_img_storage_path,f"local_img_storage_en.json")):
            with open(os.path.join(local_img_storage_path,f"local_img_storage_en.json"), "r",encoding="utf-8") as f:
                self.local_img_storage_en = json.load(f)
        if os.path.exists(os.path.join(local_img_storage_path,f"local_img_storage_zh.json")):
            with open(os.path.join(local_img_storage_path,f"local_img_storage_zh.json"), "r",encoding="utf-8") as f:
                self.local_img_storage_zh = json.load(f)
        if os.path.exists(os.path.join(local_img_storage_path,f"local_img_storage_zh.json")):
            if self.language == "en":
                self.local_img_storage = self.local_img_storage_en
            elif self.language == "zh":
                self.local_img_storage = self.local_img_storage_zh
        else:
            self.local_img_storage = []

        known_img_paths = [img["img_path"] for img in self.local_img_storage]
        all_files = get_all_files_in_dir(local_img_storage_path)
        img_files = []
        for file in all_files:
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                img_name = os.path.basename(file)
                new_img_path = os.path.join(self.save_file,img_name)
                shutil.copy(file,new_img_path)
                if img_name in known_img_paths:
                    continue
                img_files.append(new_img_path)
        asyncio.run(self.add_imgs_to_storage_async(img_files))
        with open(os.path.join(local_img_storage_path,"local_img_storage_en.json"), "w",encoding="utf-8") as f:
            json.dump(self.local_img_storage_en,f)
        with open(os.path.join(local_img_storage_path,"local_img_storage_zh.json"), "w",encoding="utf-8") as f:
            json.dump(self.local_img_storage_zh,f)
        
        if self.language == "en":
            self.local_img_storage = self.local_img_storage_en
        elif self.language == "zh":
            self.local_img_storage = self.local_img_storage_zh
        print(self.local_img_storage)
    
    async def add_imgs_to_storage_async(self,img_files):
        tasks = []
        for img_path in img_files:
            tasks.append(self.add_img_to_storage_async(img_path))
        await asyncio.gather(*tasks)

    
    async def add_img_to_storage_async(self,img_path):
        img = Image.open(img_path)
        width,height = img.size
        img_name = os.path.basename(img_path)
        process_img_prompt = get_process_img_prompt(language=self.language)
        messages = [
            {"role":"user","content":[
                {"type":"image","url":img_path},
                {"type":"text","text":process_img_prompt},
        ]},
        ]
        response = await self.get_answer_async(messages=messages)
        chinese_description = extract(response,"Chinese")
        english_description = extract(response,"English")
        self.local_img_storage_en.append({"img_path":img_name,"description":english_description,"height":height,"width":width})
        self.local_img_storage_zh.append({"img_path":img_name,"description":chinese_description,"height":height,"width":width})
        print(f"Image {img_name} has been added to the local image storage.")
    
    def clean_useless_imgs(self):
        srcs = []
        for page in self.task_queue:
            html_name = page["html_name"]
            page_name = html_name.split(".")[0]
            page_img = os.path.join(self.save_file,f"{page_name}.png")
            srcs.append(page_img)
            html_path = os.path.join(self.save_file,html_name)
            if not os.path.exists(html_path):
                continue
            html_code = open(html_path,encoding='utf-8').read()
            soup = BeautifulSoup(html_code, "html.parser")
            images = soup.find_all("img")
            for image in images:
                src = image["src"]
                srcs.append(src)
            scripts = soup.find_all("script")
            for script in scripts:
                if script.string:
                    pattern = re.compile(r'{[^}]*\bimgsrc:\s*\'([^\']*)\'[^}]*\balt:\s*\'([^\']*)\'[^}]*}')
                    for match in pattern.finditer(script.string):
                        src = match.group(1)
                        srcs.append(src)
        all_files = get_all_files_in_dir(self.save_file)
        for file in all_files:
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                img_name = os.path.basename(file)
                if img_name not in srcs:
                    os.remove(file)
                    print(f"Image {img_name} has been removed.")

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




