import base64
import re
import os
import httpx
from yaspin import yaspin


def cal_cost(prompt_tokens,completion_tokens,model = "gpt-4"):
    if "gpt-4o" in model:
        return prompt_tokens/1000000 * 5 + completion_tokens/1000000 * 15
    elif "Sonnet" in model:
        return prompt_tokens/1000000 * 3 + completion_tokens/1000000 * 15
    elif model == "glm-4-alltools":
        return (prompt_tokens + completion_tokens)/1000 * 0.1 * 0.14 
    elif model == "glm-4-0520":
        return (prompt_tokens + completion_tokens)/1000 * 0.1 * 0.14 
    elif model == "glm-4":
        return (prompt_tokens + completion_tokens)/1000 * 0.001 * 0.14
    else:
        return prompt_tokens/1000 *0.005 + completion_tokens/1000 *0.015

def write_file(file_path, content):
    with open(file_path, "w",encoding='utf-8') as f:
        f.write(content)

def get_all_files_in_dir(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list




def get_content_between_a_b(start_tag, end_tag, text):
    """
    Args:
        start_tag (str): start_tag
        end_tag (str): end_tag
        text (str): complete sentence
    Returns:
        str: the content between start_tag and end_tag
    """
    extracted_text = ""
    start_index = text.find(start_tag)
    while start_index != -1:
        end_index = text.find(end_tag, start_index + len(start_tag))
        if end_index != -1:
            extracted_text += text[start_index + len(start_tag) : end_index] + " "
            start_index = text.find(start_tag, end_index + len(end_tag))
        else:
            break

    return extracted_text.strip()


def extract(text, type):
    """extract the content between <type></type>
    Args:
        text (str): complete sentence
        type (str): tag
    Returns:
        str: content between <type></type>
    """
    target_str = get_content_between_a_b(f"<{type}>", f"</{type}>", text)
    return target_str


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_openai_url(img_pth):
    end = img_pth.split(".")[-1]
    if end == "jpg":
        end = "jpeg"
    base64_image = encode_image(img_pth)
    return f"data:image/{end};base64,{base64_image}"

def wrap_func(func,**args):
    text = "🤖💭 " + args.get("wrap_text","Thinking now...")
    if "wrap_text" in args:
        del args["wrap_text"]
    with yaspin(text = text, color="cyan") as spinner:
        result = func(**args)
        spinner.ok("✔")
    return result


def extract_dimensions(url):
    # Regular expression to match numbers in the format '300x200'
    matches = re.findall(r"(\d+)x(\d+)", url)

    if matches:
        width, height = matches[0]  # Extract the first match
        width = int(width)
        height = int(height)
        return (width, height)
    else:
        return (100, 100)


def extract_img_from_html(html_code):
    pattern = r'<img\s+([^>]+)>'
    img_tags = re.findall(pattern, html_code)
    result = []
    for tag in img_tags:
        img_info = {"original": tag}
        src_match = re.search(r'src="([^"]*)"', tag)
        if src_match:
            img_info["src"] = src_match.group(1)
        alt_match = re.search(r'alt="([^"]*)"', tag)
        if alt_match:
            img_info["alt"] = alt_match.group(1)
        
        class_match = re.search(r'class="([^"]*)"', tag)
        if class_match:
            img_info["class"] = class_match.group(1)
        if "src" in img_info and "alt" in img_info:
            result.append(img_info)
    return result

def create_file(path):
    if not os.path.exists(path):
        directory = os.path.dirname(os.path.abspath(path))
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(path, 'w') as f:
            f.write("{}")


def modify_input_dict(s):
    s = s.replace("\'","\"")
    s = s.replace("False","false")
    s = s.replace("True","true")
    s = s.replace("None","null")
    s = s.replace("\'","\"")
    s = s.replace("\"s","\'s")
    s = s.replace(" \'"," \"")
    return s

def get_html_css_from_response(response):
    html = get_content_between_a_b("```html", "```", response) if "```html" in response else None
    css = get_content_between_a_b("```css", "```", response) if "```css" in response else None
    return html,css


async def fetch_image(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Ensure the request was successful
        return response.content

if __name__ == "__main__":
    img_url = get_openai_url("/Users/jianghuyihei/code/WebDesignAgent/damo.png")
    print(img_url)