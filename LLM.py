from openai import AzureOpenAI, OpenAI,AsyncAzureOpenAI,AsyncOpenAI
from anthropic import Anthropic,AsyncAnthropic
from zhipuai import ZhipuAI
from dashscope import Generation
from dashscope.aigc.generation import AioGeneration
from abc import abstractmethod
from http import HTTPStatus
import platform
import dashscope
import yaml
import os
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
for key, value in config.items():
    os.environ[key] = str(value)
import httpx
import logging
import json
import time
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed,
)
import asyncio
import requests
from PIL import Image
from io import BytesIO
from utils import fetch_image,get_openai_url,encode_image

def before_retry_fn(retry_state):
    if retry_state.attempt_number > 1:
        logging.info(f"Retrying API call. Attempt #{retry_state.attempt_number}, f{retry_state}")
token_log_file = os.environ.get("TOKEN_LOG_FILE", "logs/token.json")




class base_llm:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def response(self,messages,**kwargs):
        pass

    def get_imgs(self,prompt, save_path="saves/dalle3.jpg"):
        pass

class base_img_llm(base_llm):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_img(self,prompt, save_path="saves/dalle3.jpg"):
        pass

class openai_llm(base_llm):
    def __init__(self) -> None:
        super().__init__()
        is_azure = config.get("is_azure", True)

        if is_azure:
            if "AZURE_OPENAI_ENDPOINT" not in os.environ or os.environ["AZURE_OPENAI_ENDPOINT"] == "":
                raise ValueError("AZURE_OPENAI_ENDPOINT is not set")
            if "AZURE_OPENAI_KEY" not in os.environ or os.environ["AZURE_OPENAI_KEY"] == "":
                raise ValueError("AZURE_OPENAI_KEY is not set")
            
            api_version = os.environ.get("AZURE_OPENAI_API_VERSION",None)
            if api_version == "":
                api_version = None
            self.client = AzureOpenAI(
                azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
                api_key=os.environ["AZURE_OPENAI_KEY"],
                api_version= api_version
                )
            self.async_client = AsyncAzureOpenAI(
                azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
                api_key=os.environ["AZURE_OPENAI_KEY"],
                api_version= api_version
                )

        else:
            if "OPENAI_API_KEY" not in os.environ or os.environ["OPENAI_API_KEY"] == "":
                raise ValueError("OPENAI_API_KEY is not set")
            
            api_key = os.environ.get("OPENAI_API_KEY",None)
            proxy_url = os.environ.get("OPENAI_PROXY_URL", None)
            if proxy_url == "":
                proxy_url = None
            base_url = os.environ.get("OPENAI_BASE_URL", None)
            if base_url == "":
                base_url = None
            http_client = httpx.Client(proxy=proxy_url) if proxy_url else None
            async_http_client = httpx.AsyncClient(proxy=proxy_url) if proxy_url else None

            self.client = OpenAI(api_key=api_key,base_url=base_url,http_client=http_client)

            self.async_client = AsyncOpenAI(api_key=api_key,base_url=base_url,http_client=async_http_client)
    
    def process_messages(self, messages):
        new_messages = []
        for message in messages:
            if message["role"] == "user":
                content = message["content"]
                if isinstance(content, list):
                    new_content= []
                    for c in content:
                        if c["type"] == "image":
                            new_content.append({"type":"image_url","image_url":{"url":get_openai_url(c["url"]),"detail":"high"}})
                        else:
                            new_content.append(c)
                    new_messages.append({"role":"user","content":new_content})
                else:
                    new_messages.append(message)
            else:
                new_messages.append(message)
        return new_messages
    
    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    def response(self,messages,**kwargs):
        messages = self.process_messages(messages)
        try:
            response = self.client.chat.completions.create(
                # gpt-35-turbo-16k  gpt4-turbo-2024-04-29 gpt-4o-2
                model=kwargs.get("model", "gpt-35-turbo-16k"),
                messages=messages,
                n = kwargs.get("n", 1),
                temperature= kwargs.get("temperature", 0.7),
                max_tokens=kwargs.get("max_tokens", 4000),
                timeout=kwargs.get("timeout", 180)
            )
        except Exception as e:
            model = kwargs.get("model", "gpt-35-turbo-16k")
            print(f"get {model} response failed: {e}")
            logging.info(e)
            return
        
        if not os.path.exists(token_log_file):
            with open(token_log_file, "w") as f:
                json.dump({},f)
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
            current_model = kwargs.get("model", "gpt-35-turbo-16k")
            if current_model not in tokens:
                tokens[current_model] = [0,0]
            tokens[current_model][0] += response.usage.prompt_tokens
            tokens[current_model][1] += response.usage.completion_tokens
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)

        return response.choices[0].message.content
    
    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    async def response_async(self,messages,**kwargs):
        messages = self.process_messages(messages)
        try:
            response = await self.async_client.chat.completions.create(
                # gpt-35-turbo-16k  gpt4-turbo-2024-04-29 gpt-4o-2
                model=kwargs.get("model", "gpt-35-turbo-16k"),
                messages=messages,
                n = kwargs.get("n", 1),
                temperature= kwargs.get("temperature", 0.7),
                max_tokens=kwargs.get("max_tokens", 4000),
                timeout=kwargs.get("timeout", 180)
            )
        except Exception as e:
            model = kwargs.get("model", "gpt-35-turbo-16k")
            print(f"get {model} response failed: {e}")
            logging.info(e)
            return
        
        if not os.path.exists(token_log_file):
            with open(token_log_file, "w") as f:
                json.dump({},f)
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
            current_model = kwargs.get("model", "gpt-35-turbo-16k")
            if current_model not in tokens:
                tokens[current_model] = [0,0]
            tokens[current_model][0] += response.usage.prompt_tokens
            tokens[current_model][1] += response.usage.completion_tokens
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)

        return response.choices[0].message.content


class claude_llm(base_llm):
    def __init__(self) -> None:
        super().__init__()
        if "CLAUDE_API_KEY" not in os.environ or os.environ["CLAUDE_API_KEY"] == "":
            raise ValueError("CLAUDE_API_KEY is not set")
        self.client = Anthropic(api_key=os.environ["CLAUDE_API_KEY"])
        self.async_client = AsyncAnthropic(api_key=os.environ["CLAUDE_API_KEY"])
    
    def process_messages(self, messages):
        new_messages = []
        for message in messages:
            if message["role"] == "user":
                content = message["content"]
                if isinstance(content, list):
                    new_content = []
                    for c in content:
                        if c["type"] == "image":
                            image_type = c["url"].split(".")[-1]
                            if image_type == "jpg":
                                image_type = "jpeg"
                            new_content.append({"type":"image","source":{"type":"base64","media_type":f"image/{image_type}","data":encode_image(c["url"])}})
                        else:
                            new_content.append(c)
                    new_messages.append({"role":"user","content":new_content})
                else:
                    new_messages.append(message)
            else:
                new_messages.append(message)
        return new_messages
    
    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    def response(self, messages, **kwargs):
        messages = self.process_messages(messages)
        try:
            response = self.client.messages.create(
                model = kwargs.get("model", "claude-3-5-sonnet-20240620"),
                temperature= kwargs.get("temperature", 0.7),
                max_tokens=kwargs.get("max_tokens", 4000),
                messages=messages,
                timeout=kwargs.get("timeout", 180)
            )
        except Exception as e:
            model = kwargs.get("model", "gpt-35-turbo-16k")
            print(f"get {model} response failed: {e}")
            print(e)
            logging.info(e)
            return

        if not os.path.exists(token_log_file):
            with open(token_log_file, "w") as f:
                json.dump({},f)
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
            current_model = kwargs.get("model", "gpt-35-turbo-16k")
            if current_model not in tokens:
                tokens[current_model] = [0,0]
            tokens[current_model][0] += response.usage.input_tokens
            tokens[current_model][1] += response.usage.output_tokens
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)

        return response.content[0].text

    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    async def response_async(self, messages, **kwargs):
        messages = self.process_messages(messages)
        try:
            response = await self.async_client.messages.create(
                model = kwargs.get("model", "claude-3-5-sonnet-20240620"),
                temperature= kwargs.get("temperature", 0.7),
                max_tokens=kwargs.get("max_tokens", 4000),
                messages=messages,
                timeout=kwargs.get("timeout", 180)
            )
        except Exception as e:
            model = kwargs.get("model", "gpt-35-turbo-16k")
            print(f"get {model} response failed: {e}")
            logging.info(e)
            return

        if not os.path.exists(token_log_file):
            with open(token_log_file, "w") as f:
                json.dump({},f)
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
            current_model = kwargs.get("model", "gpt-35-turbo-16k")
            if current_model not in tokens:
                tokens[current_model] = [0,0]
            tokens[current_model][0] += response.usage.input_tokens
            tokens[current_model][1] += response.usage.output_tokens
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)
        return response.content[0].text

class glm_llm(base_llm):
    def __init__(self) -> None:
        super().__init__()
        if "GLM_API_KEY" not in os.environ or os.environ["GLM_API_KEY"] == "":
            raise ValueError("GLM_API_KEY is not set")
        self.client = ZhipuAI(api_key=os.environ["GLM_API_KEY"])
    
    def process_messages(self, messages):
        new_messages = []
        for message in messages:
            if message["role"] == "user":
                content = message["content"]
                if isinstance(content, list):
                    new_content= []
                    for c in content:
                        if c["type"] == "image":
                            new_content.append({"type":"image_url","image_url":{"url":get_openai_url(c["url"]),"detail":"high"}})
                        else:
                            new_content.append(c)
                    new_messages.append({"role":"user","content":new_content})
                else:
                    new_messages.append(message)
            else:
                new_messages.append(message)
        return new_messages
    
    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    def response(self, messages, **kwargs):
        messages = self.process_messages(messages)
        try:
            response = self.client.chat.completions.create(
                model = kwargs.get("model", "glm-4v"),
                messages = messages,
                timeout = kwargs.get("timeout", 180),
                max_tokens=kwargs.get("max_tokens", 4000)
            )
        except Exception as e:
            model = kwargs.get("model", "glm-4v")
            print(f"get {model} response failed: {e}")
            print(e)
            logging.info(e)
            return
        
        if not os.path.exists(token_log_file):
            with open(token_log_file, "w") as f:
                json.dump({},f)
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
            current_model = kwargs.get("model", "glm-4")
            if current_model not in tokens:
                tokens[current_model] = [0,0]
            tokens[current_model][0] += response.usage.prompt_tokens
            tokens[current_model][1] += response.usage.completion_tokens
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)
        return response.choices[0].message.content
    
    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    async def response_async(self, messages, **kwargs):
        messages = self.process_messages(messages)
        try:
            response_total = self.client.chat.asyncCompletions.create(
                model = kwargs.get("model", "glm-4"),
                messages = messages,
                timeout = kwargs.get("timeout", 180),
                max_tokens=kwargs.get("max_tokens", 4000),
            )
            task_id = response_total.id
            task_status = response_total.task_status

            async def time_sleep():
                await asyncio.sleep(1)
        
            get_cnt = 0
            while task_status != 'SUCCESS' and task_status != 'FAILED' and get_cnt <= 40:
                await time_sleep()
                result_response = self.client.chat.asyncCompletions.retrieve_completion_result(id=task_id)
                task_status = result_response.task_status
                time.sleep(2)
                get_cnt += 1
            response = result_response


        except Exception as e:
            model = kwargs.get("model", "glm-4v")
            print(f"get {model} response failed: {e}")
            print(e)
            logging.info(e)
            return
        
        if not os.path.exists(token_log_file):
            with open(token_log_file, "w") as f:
                json.dump({},f)
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
            current_model = kwargs.get("model", "glm-4v")
            if current_model not in tokens:
                tokens[current_model] = [0,0]
            tokens[current_model][0] += response.usage.prompt_tokens
            tokens[current_model][1] += response.usage.completion_tokens
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)
        return response.choices[0].message.content

class qwen_llm(base_llm):
    def __init__(self) -> None:
        super().__init__()
        if "DASHSCOPE_API_KEY" not in os.environ or os.environ["DASHSCOPE_API_KEY"] == "":
            raise ValueError("DASHSCOPE_API_KEY is not set")
        dashscope.api_key = os.environ["DASHSCOPE_API_KEY"]
    
    def process_messages(self, messages):
        new_messages = []
        for message in messages:
            if message["role"] == "user":
                content = message["content"]
                if isinstance(content, list):
                    new_content= []
                    for c in content:
                        if c["type"] == "image":
                            new_content.append({"type":"image_url","image_url":{"url":get_openai_url(c["url"]),"detail":"high"}})
                        else:
                            new_content.append(c)
                    new_messages.append({"role":"user","content":new_content})
                else:
                    new_messages.append(message)
            else:
                new_messages.append(message)
        return new_messages
    
    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    def response(self, messages, **kwargs):
        messages = self.process_messages(messages)
        try:
            response = Generation.call(
                model = kwargs.get("model", "qwen-max-longcontext"),
                messages = messages,
                timeout = kwargs.get("timeout", 180),
                max_tokens=kwargs.get("max_tokens", 4000),
                result_format = "message"
            )
        except Exception as e:
            model = kwargs.get("model", "qwen-max-longcontext")
            print(f"get {model} response failed: {e}")
            print(e)
            logging.info(e)
            return
        if not os.path.exists(token_log_file):
            with open(token_log_file, "w") as f:
                json.dump({},f)
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
            current_model = kwargs.get("model", "qwen-max-longcontext")
            if current_model not in tokens:
                tokens[current_model] = [0,0]
            tokens[current_model][0] += response.usage.input_tokens
            tokens[current_model][1] += response.usage.output_tokens
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)
        return response.output.choices[0].message.content
    
    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    async def response_async(self, messages, **kwargs):
        messages = self.process_messages(messages)
        try:
            response = await AioGeneration.call(
                model = kwargs.get("model", "qwen-max-longcontext"),
                messages = messages,
                timeout = kwargs.get("timeout", 180),
                max_tokens=kwargs.get("max_tokens", 4000),
                result_format = "message"
            )
        except Exception as e:
            print("response:",response)
            model = kwargs.get("model", "qwen-max-longcontext")
            print(f"get {model} response failed: {e}")
            logging.info(e)
            return
        
        if not os.path.exists(token_log_file):
            with open(token_log_file, "w") as f:
                json.dump({},f)
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
            current_model = kwargs.get("model", "qwen-max-longcontext")
            if current_model not in tokens:
                tokens[current_model] = [0,0]
            tokens[current_model][0] += response.usage.input_tokens
            tokens[current_model][1] += response.usage.output_tokens
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)
        return response.output.choices[0].message.content




class Dalle3_llm(base_img_llm):
    def __init__(self) -> None:
        super().__init__()
        is_azure = config.get("is_azure", True)

        if is_azure:
            api_version = os.environ.get("AZURE_OPENAI_API_VERSION",None)
            if api_version == "":
                api_version = None
            self.client = AzureOpenAI(
                azure_endpoint=os.environ["AZURE_OPENAI_DALLE_ENDPOINT"],
                api_key=os.environ["AZURE_OPENAI_DALLE_KEY"],
                api_version= api_version
                )
            self.async_client = AsyncAzureOpenAI(
                azure_endpoint=os.environ["AZURE_OPENAI_DALLE_ENDPOINT"],
                api_key=os.environ["AZURE_OPENAI_DALLE_KEY"],
                api_version= api_version
                )
        else:
            api_key = os.environ.get("OPENAI_API_KEY",None)
            proxy_url = os.environ.get("OPENAI_PROXY_URL", None)
            if proxy_url == "":
                proxy_url = None
            base_url = os.environ.get("OPENAI_BASE_URL", None)
            if base_url == "":
                base_url = None
            http_client = httpx.Client(proxy=proxy_url) if proxy_url else None
            async_http_client = httpx.AsyncClient(proxy=proxy_url) if proxy_url else None

            self.client = OpenAI(api_key=api_key,base_url=base_url,http_client=http_client)
            self.async_client = AsyncOpenAI(api_key=api_key,base_url=base_url,http_client=async_http_client)

    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    def get_img(self,prompt, save_path="saves/dalle3.jpg"):
        try:
            return self._get_img(prompt, save_path)
        except Exception as e:
            # Catch the specific safety warning and modify the prompt
            if "Your prompt may contain text that is not allowed by our safety system." in str(e):
                logging.info(f"Safety system error with prompt: {prompt}. Modifying prompt and retrying.")
                new_prompt = "a colorful abstract painting of a cat"
                return self._get_img(new_prompt, save_path)
            print("Error: generate img failed",e)

    def _get_img(self,prompt, save_path):
        img_client = self.client
        result = img_client.images.generate(
            model="dalle3",
            prompt=prompt,
            n=1,
            timeout=180
        )
        image_url = json.loads(result.model_dump_json())['data'][0]['url']
        img = requests.get(image_url).content
        img = Image.open(BytesIO(img))
        img.save(save_path)

        # Log token usage
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
        current_model = "dalle3"
        if current_model not in tokens:
            tokens[current_model] = 0
        tokens[current_model] += 1
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)
        return img       

    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    async def get_img_async(self,prompt, save_path="saves/dalle3.jpg"):
        try:
            return await self._get_img_async(prompt, save_path)
        except Exception as e:
            # Catch the specific safety warning and modify the prompt
            if "Your prompt may contain text that is not allowed by our safety system." in str(e):
                logging.info(f"Safety system error with prompt: {prompt}. Modifying prompt and retrying.")
                new_prompt = "a colorful abstract painting of a cat"
                return await self._get_img_async(new_prompt, save_path)
            print("Error: generate img failed",e)
    
    async def _get_img_async(self,prompt, save_path):
        img_client = self.async_client
        result = await img_client.images.generate(
            model="dalle3",
            prompt=prompt,
            n=1,
            timeout=180
        )
        image_url = json.loads(result.model_dump_json())['data'][0]['url']
        img = await fetch_image(image_url)
        img = Image.open(BytesIO(img))
        img.save(save_path)

        # Log token usage
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
        current_model = "dalle3"
        if current_model not in tokens:
            tokens[current_model] = 0
        tokens[current_model] += 1
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)
        return img

class cogview3_llm(base_img_llm):
    def __init__(self) -> None:
        super().__init__()
        self.client = ZhipuAI(api_key=os.environ["GLM_API_KEY"])
    
    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    def get_img(self,prompt, save_path="saves/cogview-3.jpg"):
        try:
            return self._get_img(prompt, save_path)
        except Exception as e:
            # Catch the specific safety warning and modify the prompt
            try:
                new_prompt = "一只可爱的小猫在草地奔跑"
                return self._get_img(new_prompt, save_path)
            except Exception as e:
                print("Error: generate img failed",e)

    def _get_img(self,prompt, save_path):
        result = self.client.images.generations(
            model="cogview-3",
            prompt=prompt,
            n=1,
            timeout=180
        )
        image_url = json.loads(result.model_dump_json())['data'][0]['url']
        img = requests.get(image_url).content
        img = Image.open(BytesIO(img))
        img.save(save_path)

        # Log token usage
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
        current_model = "cogview-3"
        if current_model not in tokens:
            tokens[current_model] = 0
        tokens[current_model] += 1
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)
        return img       

    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    async def get_img_async(self,prompt, save_path="saves/cogview-3.jpg"):
        try:
            return await self._get_img_async(prompt, save_path)
        except Exception as e:
            # Catch the specific safety warning and modify the prompt
            try:
                new_prompt = "一只可爱的小猫在草地奔跑"
                return await self._get_img_async(new_prompt, save_path)
            except Exception as e:
                print("Error: generate img failed",e)
    
    async def _get_img_async(self,prompt, save_path):
        result = self.client.images.generations(
            model="cogview-3",
            prompt=prompt,
            n=1,
            timeout=180
        )
        image_url = json.loads(result.model_dump_json())['data'][0]['url']
        img = await fetch_image(image_url)
        img = Image.open(BytesIO(img))
        img.save(save_path)

        # Log token usage
        with open(token_log_file, "r") as f:
            tokens = json.load(f)
        current_model = "cogview-3"
        if current_model not in tokens:
            tokens[current_model] = 0
        tokens[current_model] += 1
        with open(token_log_file, "w") as f:
            json.dump(tokens, f)
        return img
    
    



def get_llm():
    llm_type = config.get("LLM_TYPE", "openai")
    img_gen_type = config.get("IMG_GEN_TYPE", "dalle3")
    llm , img_generator = None,None
    if llm_type in ["openai"]:
        llm = openai_llm()
    elif llm_type == "claude":
        llm = claude_llm()
    elif llm_type == "glm":
        llm = glm_llm()
    elif llm_type == "qwen":
        llm = qwen_llm()
    else:
        raise ValueError(f"Unknown LLM type: {llm_type}")
    if img_gen_type == "dalle3":
        img_generator = Dalle3_llm()
    elif img_gen_type == "cogview-3":
        img_generator = cogview3_llm()
    else:
        raise ValueError(f"Unknown image generator type: {img_gen_type}")
    return llm, img_generator
    




if __name__ == "__main__":
    llm , img_llm= get_llm()
    prompt = "孙悟空大战猪八戒"
    tasks = [img_llm.get_img_async(prompt,save_path="saves/cogview-32.jpg"),img_llm.get_img_async(prompt,save_path="saves/cogview-33.jpg")]
    asyncio.run(asyncio.gather(*tasks))





