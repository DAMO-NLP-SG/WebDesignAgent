# ["Tailwind","Boostrap","Materialize","Bulma",None]
def get_refine_prompt(text = None,img = None,html_code = None,css_code = None,page_info = None,feedback = "",css_frame = None,language = "en",local_img_storage = []):
    if language == "en":
        from .refine_prompts_en import refine_Tailwind_output_format,refine_Boostrap_output_format,refine_Materialize_output_format,refine_Bulma_output_format,refine_original_output_format,refine_feedback_task,refine_img_text_task,refine_img_task,refine_text_task,refine_prompt,Tailwind_role,Boostrap_role,Materialize_role,Bulma_role,original_role
        feedback = f"The user's feedback is as follows(very important, please pay attention to it!):{feedback}" if feedback else ""
        local_img_storage = f"The img you maybe use to design the page(It is not required to use it, you can choose it according to the situation, please pay close attention to the size of the picture):{local_img_storage}" if local_img_storage else ""
        pre_task =  "The image above is a screenshot of the website you have already designed."

    elif language == "zh":
        from .refine_prompts_zh import refine_Tailwind_output_format,refine_Boostrap_output_format,refine_Materialize_output_format,refine_Bulma_output_format,refine_original_output_format,refine_feedback_task,refine_img_text_task,refine_img_task,refine_text_task,refine_prompt,Tailwind_role,Boostrap_role,Materialize_role,Bulma_role,original_role
        feedback = f"用户的反馈如下(非常重要，请注意！):{feedback}" if feedback else ""
        local_img_storage = f"您可能在你的网页中可能可以用到的图片(并非要求一定使用，你看情况使用挑选，请严格注意图片的大小尺寸):{local_img_storage}" if local_img_storage else ""
        pre_task = "上面的图片是您已经设计的网站的截图。"

    if css_frame == "Tailwind":
        role = Tailwind_role
        output_format = refine_Tailwind_output_format.format(html_code = html_code,feedback = feedback)
    elif css_frame == "Boostrap":
        role = Boostrap_role
        output_format = refine_Boostrap_output_format.format(html_code = html_code,feedback = feedback)
    elif css_frame == "Materialize":
        role = Materialize_role
        output_format = refine_Materialize_output_format.format(html_code = html_code,feedback = feedback)
    elif css_frame == "Bulma":
        role = Bulma_role
        output_format = refine_Bulma_output_format.format(html_code = html_code,feedback = feedback)
    else:
        role = original_role
        output_format = refine_original_output_format.format(html_code = html_code,css_code=css_code,feedback = feedback)
    if feedback:
        task = refine_feedback_task.format(page_info = page_info,local_img_storage = local_img_storage)
    elif img and text:
        task = refine_img_text_task.format(page_info = page_info,local_img_storage = local_img_storage)
    elif img:
        task = refine_img_task.format(page_info = page_info,local_img_storage = local_img_storage)
    else:
        task = refine_text_task.format(page_info = page_info,local_img_storage = local_img_storage)
        task = pre_task + task

    prompt = refine_prompt.format(role = role,task = task,output_format = output_format)
    return prompt