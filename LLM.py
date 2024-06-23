from openai import AzureOpenAI, OpenAI
from utils import get_openai_url
import yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
import time
import httpx
import logging
import os
import json
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed,
)
import requests
from PIL import Image
from io import BytesIO
from utils import wrap_func

is_azure = config.get("is_azure", True)
token_log_file = os.environ.get("TOKEN_LOG_FILE", "logs/token.json")

if is_azure:
    os.environ["AZURE_OPENAI_ENDPOINT"] = config.get('AZURE_OPENAI_ENDPOINT', '')
    os.environ["AZURE_OPENAI_KEY"] = config.get('AZURE_OPENAI_KEY', '')
    os.environ["AZURE_OPENAI_API_VERSION"] = config.get('AZURE_OPENAI_API_VERSION', '')

    if "AZURE_OPENAI_ENDPOINT" not in os.environ or os.environ["AZURE_OPENAI_ENDPOINT"] == "":
        raise ValueError("AZURE_OPENAI_ENDPOINT is not set")
    if "AZURE_OPENAI_KEY" not in os.environ or os.environ["AZURE_OPENAI_KEY"] == "":
        raise ValueError("AZURE_OPENAI_KEY is not set")
    if "AZURE_OPENAI_API_VERSION" not in os.environ or os.environ["AZURE_OPENAI_API_VERSION"] == "":
        raise ValueError("AZURE_OPENAI_API_VERSION is not set")
    client = AzureOpenAI(
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
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY") if proxy_url is None or proxy_url == "" else OpenAI(api_key= os.environ.get("OPENAI_API_KEY"), http_client=httpx.Client(proxy=proxy_url)))

def before_retry_fn(retry_state):
    if retry_state.attempt_number > 1:
        logging.info(f"Retrying API call. Attempt #{retry_state.attempt_number}, f{retry_state}")

@retry(wait=wait_fixed(10), stop=stop_after_attempt(10), before=before_retry_fn)
def Openai_response(messages,**kwargs):
    try:
        response = client.chat.completions.create(
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
def get_openai_imgs(prompt, save_path="saves/dalle3.jpg"):
    try:
        return _get_openai_imgs(prompt, save_path)
    except Exception as e:
        # Catch the specific safety warning and modify the prompt
        if "Your prompt may contain text that is not allowed by our safety system." in str(e):
            logging.info(f"Safety system error with prompt: {prompt}. Modifying prompt and retrying.")
            new_prompt = "a colorful abstract painting of a cat"
            return _get_openai_imgs(new_prompt, save_path)
        raise  # Re-raise the exception for other types of errors

def _get_openai_imgs(prompt, save_path):
    result = client.images.generate(
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


    



if __name__ == "__main__":
    prompt = """

"""
    messages = [
        {"role":"user","content":[
            {"type":"text","text":prompt},
    ]},
    ]
    response = Openai_response(messages,model="gpt4o-0513")
    print(response.choices[0].message.content)

