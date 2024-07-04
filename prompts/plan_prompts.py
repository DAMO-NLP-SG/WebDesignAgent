def get_plan_prompt(text = None,img = None ,css_frame = None,feedback = "",language = "en",local_img_storage = []):
    """Get plan prompt"""
    if language == "en":
        from .plan_prompts_en import plan_output_format_prompt,original_page_template,plan_output_format_prompt_local_img,local_img_storage_page_template
        if img and text:
            prompt = f"Your task is to design which pages we should create to design the website for task: {text};The above image is a reference website we have provided to you. Instead of designing the website according to the above image, you need to imitate the image and then design a new website based on your task.Remember, you need to keep the style consistent between each web page, that is, describe the page_style in detail to ensure the consistency of style between pages (describe the commonality through a common style, and then describe the different styles of each page)"
        elif img:
            prompt = "Your task is to design which pages we should create to design the website based on the website images I provided you.Remember, you need to keep the style consistent between each web page, that is, describe the page_style in detail to ensure the consistency of style between pages (describe the commonality through a common style, and then describe the different styles of each page)"
        else:
            prompt = f"Your task is to design which pages we should create to design the website for task: {text};Remember, you need to keep the style consistent between each web page, that is, describe the page_style in detail to ensure the consistency of style between pages (describe the commonality through a common style, and then describe the different styles of each page)"
        feedback = f"The user's requirements on the website(Very important! You must pay extra attention to the content here and meet user's needs) is : {feedback}" if feedback else ""
    elif language == "zh":
        from .plan_prompts_zh import plan_output_format_prompt,original_page_template,plan_output_format_prompt_local_img,local_img_storage_page_template
        if img and text:
            prompt = f"你的任务是确定我们需要创建哪些页面来设计该任务的网站：{text};上方的图片是我们提供的参考网站。你需要根据该图片进行模仿，但不是完全照搬，而是根据你需要完成的任务设计一个全新的网站。记住，你要保持各个网页之间的风格统一，即详细描述page_style来保证页面之间的风格一致（通过一段共性style描述共性，再描述各个页面的不同style）。"
        elif img:
            prompt = "你的任务是确定我们需要创建哪些页面来设计基于我提供的网站图片的网站。(需要完全根据图片设计，尽量做到一致)。记住，你要保持各个网页之间的风格统一，即详细描述page_style来保证页面之间的风格一致（通过一段共性style描述共性，再描述各个页面的不同style）"
        else:
            prompt = f"你的任务是确定我们需要创建哪些页面来设计该任务的网站：{text};记住，你要保持各个网页之间的风格统一，即详细描述page_style来保证页面之间的风格一致（通过一段共性style描述共性，再描述各个页面的不同style）"
        feedback = f"用户对网站的需求(非常重要！你必须特别注意这里的内容，并满足用户的需求)是：{feedback}" if feedback else ""
    if local_img_storage:
        prompt += plan_output_format_prompt_local_img.format(local_img_storage = local_img_storage,page_template = local_img_storage_page_template)
    else:
        prompt += plan_output_format_prompt.format(page_template = original_page_template)
    return prompt


def get_refine_page_prompt(task,page_info,css_frame = None,feedback = "",language = "en",local_img_storage = []):
    if language == "en":
        from .plan_prompts_en import refine_page_prompt,original_page_example,local_img_storage_page_example,refine_page_local_img_prompt
        task_info = f"The requirements of the website is {task}" if task else ""
        feedback = f"The user feedback on the webpage(Very important! You must pay extra attention to the content here and prioritize making modifications to it) is : {feedback}" if feedback else ""
    elif language == "zh":
        from .plan_prompts_zh import refine_page_prompt,original_page_example,local_img_storage_page_example,refine_page_local_img_prompt
        task_info = f"网站的需求是{task}" if task else ""
        feedback = f"用户对网页的反馈(非常重要！你必须特别注意这里的内容，并优先进行修改)是：{feedback}" if feedback else ""
    if local_img_storage:
        page_example = local_img_storage_page_example
        prompt = refine_page_local_img_prompt.format(task_info = task_info,page_info = page_info,page_example = page_example,feedback = feedback,local_img_storage = local_img_storage)
    else:
        page_example = original_page_example
        prompt = refine_page_prompt.format(task_info = task_info,page_info = page_info,page_example = page_example,feedback = feedback)
    return prompt

def get_page_complete_prompt(task= "",other_pages_info="",page_info="",feedback = "" ,language = "en",local_img_storage = []):
    if language == "en":
        from .plan_prompts_en import page_complete_prompt,page_complete_prompt_local_img
        feedback = f"The user feedback on how to complete the webpage(Very important! You must pay extra attention to the content here and prioritize making modifications to it) is : {feedback}" if feedback else ""
        task_info = f"The requirements of the website is {task}" if task else ""
    elif language == "zh":
        from .plan_prompts_zh import page_complete_prompt,page_complete_prompt_local_img
        feedback = f"用户对如何完成网页的反馈(非常重要！你必须特别注意这里的内容，并优先进行修改)是：{feedback}" if feedback else ""
        task_info = f"网站的需求是{task}" if task else ""
    if local_img_storage:
        prompt = page_complete_prompt_local_img.format(task_info = task_info,other_pages_info = other_pages_info,page_info = page_info,feedback = feedback,local_img_storage = local_img_storage)
    else:
        prompt = page_complete_prompt.format(task_info = task_info,other_pages_info = other_pages_info,page_info = page_info,feedback = feedback)
    return prompt

if __name__ == "__main__":
    print(get_plan_prompt("test",img = True))
    print(get_refine_page_prompt("test","test"))
    print(get_page_complete_prompt("test","test"))