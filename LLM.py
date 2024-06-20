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

@retry(wait=wait_fixed(10), stop=stop_after_attempt(6), before=before_retry_fn)
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

@retry(wait=wait_fixed(10), stop=stop_after_attempt(6))
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
You are a webpage design master, and your task is to complete a unfinished webpage.
The other page information is as follows:
[{"html_name": "index.html", "css_name": "main.css", "js_name": "main.js", "js_description": "Interactive elements for the homepage, such as navigation, sliders, and pop-ups.", "description": "This is the main page of the game company website, featuring highlights of the company's games, latest news, and introductory content.", "relationship": {"buttons": [{"button_name": "About Us", "jump_page": "about.html", "description": "Navigates to the About Us page"}, {"button_name": "Our Games", "jump_page": "games.html", "description": "Navigates to the Our Games page"}, {"button_name": "News", "jump_page": "news.html", "description": "Navigates to the News page"}, {"button_name": "Careers", "jump_page": "careers.html", "description": "Navigates to the Careers page"}, {"button_name": "Contact", "jump_page": "contact.html", "description": "Navigates to the Contact page"}], "links": []}, "additional_features": "User account login, language selection", "is_main_page": true}, {"html_name": "about.html", "css_name": "about.css", "js_name": "about.js", "js_description": "Interactive elements for displaying the company's rich history, ambitious mission, and talented team. Includes animations and dynamic content for an engaging user experience.", "description": "This page offers an in-depth look at the game company's illustrious history, its mission to revolutionize the action genre, and the diverse, talented team behind its success. It showcases the company's journey from inception to fame with Black Myth Wukong.", "relationship": {"buttons": [{"button_name": "Home", "jump_page": "index.html", "description": "Navigates back to the main page"}], "links": []}, "additional_features": "Detailed team member profiles with interactive hover effects that reveal more information about their roles, backgrounds, and contributions to the company.", "is_main_page": false}, {"html_name": "games.html", "css_name": "games.css", "js_name": "games.js", "js_description": "Interactive gallery of the company's games with detailed descriptions and videos.", "description": "This page showcases the company's games, including Black Myth Wukong, with detailed descriptions, images, and videos.", "relationship": {"buttons": [{"button_name": "Home", "jump_page": "index.html", "description": "Navigates back to the main page"}], "links": []}, "additional_features": "Game trailers and gameplay videos", "is_main_page": false}, {"html_name": "news.html", "css_name": "news.css", "js_name": "news.js", "js_description": "A dynamic and interactive news feed that brings you the freshest updates, announcements, and exclusive content from our AAA level action games.", "description": "Stay updated with the latest news and announcements from our renowned game company, famous for creating the critically acclaimed Black Myth Wukong. This page is your go-to source for all things related to our groundbreaking AAA action games.", "relationship": {"buttons": [{"button_name": "Home", "jump_page": "index.html", "description": "Navigates back to the main page, where you can explore our portfolio, learn about upcoming releases, and more."}], "links": []}, "additional_features": "Subscribe to our news feed to get instant notifications on game updates, exclusive announcements, and behind-the-scenes content.", "is_main_page": false}, {"html_name": "careers.html", "css_name": "careers.css", "js_name": "careers.js", "js_description": "Interactive job listings and application forms, with dynamic filtering and real-time updates.", "description": "Explore your career opportunities with us! This page lists current job openings and allows users to apply for positions with ease. Join our team to work on groundbreaking AAA action games like Black Myth Wukong.", "relationship": {"buttons": [{"button_name": "Home", "jump_page": "index.html", "description": "Navigates back to the main page"}], "links": []}, "additional_features": "Job application forms and submission, real-time job listing updates, and dynamic filtering options to help users find the perfect role.", "is_main_page": false}, {"html_name": "contact.html", "css_name": "contact.css", "js_name": "contact.js", "js_description": "Interactive contact form with validation, real-time feedback, and company contact information display.", "description": "This page provides comprehensive contact information and an interactive form allowing users to reach out to the company with inquiries, feedback, or support requests. The form is designed to be user-friendly and responsive.", "relationship": {"buttons": [{"button_name": "Home", "jump_page": "index.html", "description": "Navigates back to the main page, where you can find the latest updates, news, and game releases from our AAA action titles."}], "links": []}, "additional_features": "Google Maps integration for office location, including street view and directions.", "is_main_page": false}]
The current page information is as follows:
{
        "html_name": “wukong.html",
        "css_name": "wukong.css",
        "js_name": "wukong.js",
        "js_description": "",
        "description": "The website introducing the game wukong ",
        "relationship": {
        },
        "additional_features": "",
        "is_main_page": false
    },
Please complete and refine the information on this page based on the information on other pages and the known information on the current page (pay attention to the jump relationship between pages), and consider which pages need to be designed with links or buttons to jump to the current page
Your output should be in the following format:
Thinking steps:
{Your thinking steps}

<completed_page>
{Your completed and refined page, do not change or add or delete the original key of the page, you can modify the value of the key, and the page should be dict format}
</completed_page>

<page_relationship>
{The name of pages that need to be designed with links or buttons to jump to the current page and the output format should be a list. For example:[{"html_name":"index.html","button_name":"jump"},{"html_name":"home.html","button_name":"jump"}]}
</page_relationship>
"""

    messages = [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": prompt}
      ],
    }
  ]
    response = wrap_func(Openai_response,messages= messages,model="gpt4o-0513")
    # response = Openai_response(messages,model = "gpt4o-0513")
    print(response.choices[0].message.content)