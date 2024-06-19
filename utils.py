import base64
import re
import os
from yaspin import yaspin


def cal_cost(prompt_tokens,completion_tokens):
    return prompt_tokens/1000 *0.005 + completion_tokens/1000 *0.015

def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

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


def extract_img_from_html(html_code):
    pattern = r'<img\s+([^>]+)>'
    img_tags = re.findall(pattern, html_code)
    result = []
    for tag in img_tags:
        img_info = {}
        src_match = re.search(r'src="([^"]*)"', tag)
        if src_match:
            img_info["src"] = src_match.group(1)
        alt_match = re.search(r'alt="([^"]*)"', tag)
        if alt_match:
            img_info["alt"] = alt_match.group(1)
        data_description_match = re.search(r'description="([^"]*)"', tag)
        if data_description_match:
            img_info["description"] = data_description_match.group(1)
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