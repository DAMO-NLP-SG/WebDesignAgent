from openai import AzureOpenAI, OpenAI,AsyncAzureOpenAI,AsyncOpenAI
from abc import abstractmethod
import yaml
import os
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

for key, value in config.items():
    os.environ[key] = str(value)

import httpx
import logging
import json
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed,
)
import requests
from PIL import Image
from io import BytesIO
from utils import wrap_func,fetch_image

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
            if "AZURE_OPENAI_API_VERSION" not in os.environ or os.environ["AZURE_OPENAI_API_VERSION"] == "":
                self.client = AzureOpenAI(
                    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-01"),
                    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
                    )
                self.async_client = AsyncAzureOpenAI(
                    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-01"),
                    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
                    )
            else:
                self.client = AzureOpenAI(
                    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-01"),
                    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
                    api_key=os.environ["AZURE_OPENAI_KEY"]
                    )
                self.async_client = AsyncAzureOpenAI(
                    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-01"),
                    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
                    api_key=os.environ["AZURE_OPENAI_KEY"]
                    )
        else:
            os.environ["OPENAI_API_KEY"] = config.get('OPENAI_API_KEY', '')
            os.environ["OPENAI_PROXY_URL"] = config.get('OPENAI_PROXY_URL', '')

            if "OPENAI_API_KEY" not in os.environ or os.environ["OPENAI_API_KEY"] == "":
                raise ValueError("OPENAI_API_KEY is not set")
            
            proxy_url = os.environ.get("OPENAI_PROXY_URL")
            self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY") if proxy_url is None or proxy_url == "" else OpenAI(api_key= os.environ.get("OPENAI_API_KEY"), http_client=httpx.Client(proxy=proxy_url)))
            self.async_client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY") if proxy_url is None or proxy_url == "" else AsyncOpenAI(api_key= os.environ.get("OPENAI_API_KEY"), http_client=httpx.AsyncClient(proxy=proxy_url)))


    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    def response(self,messages,**kwargs):
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
            print(e)
            logging.info(e)
        
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

        return response
    
    @retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
    async def response_async(self,messages,**kwargs):
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
            print(e)
            logging.info(e)
        
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

        return response
    

class Dalle3_llm(base_img_llm):
    def __init__(self) -> None:
        super().__init__()
        is_azure = config.get("is_azure", True)

        if is_azure:
            if "AZURE_OPENAI_DALLE_ENDPOINT" not in os.environ or os.environ["AZURE_OPENAI_DALLE_ENDPOINT"] == "":
                raise ValueError("AZURE_OPENAI_DALLE_ENDPOINT is not set")
            if "AZURE_OPENAI_DALLE_KEY" not in os.environ or os.environ["AZURE_OPENAI_DALLE_KEY"] == "":
                raise ValueError("AZURE_OPENAI_DALLE_KEY is not set")


            if "AZURE_OPENAI_API_VERSION" not in os.environ or os.environ["AZURE_OPENAI_API_VERSION"] == "":
                self.client = AzureOpenAI(
                    azure_endpoint=os.environ["AZURE_OPENAI_DALLE_ENDPOINT"],
                    api_key=os.environ["AZURE_OPENAI_DALLE_KEY"]
                    )
                self.async_client = AsyncAzureOpenAI(
                    azure_endpoint=os.environ["AZURE_OPENAI_DALLE_ENDPOINT"],
                    api_key=os.environ["AZURE_OPENAI_DALLE_KEY"]
                    )
            else:
                self.client = AzureOpenAI(
                    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-01"),
                    azure_endpoint=os.environ["AZURE_OPENAI_DALLE_ENDPOINT"],
                    api_key=os.environ["AZURE_OPENAI_DALLE_KEY"]
                    )
                self.async_client = AsyncAzureOpenAI(
                    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-01"),
                    azure_endpoint=os.environ["AZURE_OPENAI_DALLE_ENDPOINT"],
                    api_key=os.environ["AZURE_OPENAI_DALLE_KEY"]
                    )
        else:
            os.environ["OPENAI_API_KEY"] = config.get('OPENAI_API_KEY', '')
            os.environ["OPENAI_PROXY_URL"] = config.get('OPENAI_PROXY_URL', '')

            if "OPENAI_API_KEY" not in os.environ or os.environ["OPENAI_API_KEY"] == "":
                raise ValueError("OPENAI_API_KEY is not set")
            
            proxy_url = os.environ.get("OPENAI_PROXY_URL")
            self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY") if proxy_url is None or proxy_url == "" else OpenAI(api_key= os.environ.get("OPENAI_API_KEY"), http_client=httpx.Client(proxy=proxy_url)))
            self.async_client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY") if proxy_url is None or proxy_url == "" else AsyncOpenAI(api_key= os.environ.get("OPENAI_API_KEY"), http_client=httpx.AsyncClient(proxy=proxy_url)))

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
            raise  # Re-raise the exception for other types of errors

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
            raise
    
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

def get_llm():
    llm_type = config.get("LLM_TYPE", "openai")
    img_gen_type = config.get("IMG_GEN_TYPE", "dalle3")
    llm , img_generator = None,None
    if llm_type == "openai":
        llm = openai_llm()
    else:
        raise ValueError(f"Unknown LLM type: {llm_type}")
    if img_gen_type == "dalle3":
        img_generator = Dalle3_llm()
    else:
        raise ValueError(f"Unknown image generator type: {img_gen_type}")
    return llm, img_generator
    




if __name__ == "__main__":
    llm , delle = get_llm()
    print("success")
    prompt = """
黑暗风格的猪八戒
    """
    img = delle.get_img(prompt,save_path="/Users/jianghuyihei/code/black_myth_pic/bajie.png")






    




if __name__ == "__main__":
    prompt = """
hello, please tell me 1 + 1 = ?
"""
    messages = [
        {"role":"user","content":[
            {"type":"text","text":prompt},
    ]},
    ]
    llm , _= get_llm()
    response = llm.response(messages,model = "gpt4o-0513")
    print(response)




