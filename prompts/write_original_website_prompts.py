def get_write_original_website_prompt(text = None,img = None,page_info = None,css_frame = None,feedback = "",language = "en"):
    if language == "en":
        from .write_original_website_prompts_en import text_img_task,text_task,img_task,write_original_prompt,Tailwind_role,Boostrap_role,Materialize_role,Bulma_role,original_role,Tailwind_output_format,Boostrap_output_format,Materialize_output_format,Bulma_output_format,original_output_format
        feedback = f"The user's requirements is as follows(very important, please pay attention to it!):{feedback}" if feedback else ""

    elif language == "zh":
        from .write_original_website_prompts_zh import text_img_task,text_task,img_task,write_original_prompt,Tailwind_role,Boostrap_role,Materialize_role,Bulma_role,original_role,Tailwind_output_format,Boostrap_output_format,Materialize_output_format,Bulma_output_format,original_output_format
        feedback = f"用户的需求如下(非常重要，请注意!):{feedback}" if feedback else ""


    if css_frame == "Tailwind":
        role = Tailwind_role
        output_format = Tailwind_output_format.format(feedback=feedback)
    elif css_frame == "Boostrap":
        role = Boostrap_role
        output_format = Boostrap_output_format.format(feedback=feedback)
    elif css_frame == "Materialize":
        role = Materialize_role
        output_format = Materialize_output_format.format(feedback=feedback)
    elif css_frame == "Bulma":
        role = Bulma_role
        output_format = Bulma_output_format.format(feedback=feedback)
    else:
        role = original_role
        output_format = original_output_format.format(feedback=feedback)
    if img and text:
        task = text_img_task.format(page_info=page_info)
        prompt = write_original_prompt.format(role=role,task=task,page_info=page_info,output_format=output_format)
    elif img:
        task = img_task.format(page_info=page_info)
        prompt = write_original_prompt.format(role=role,task=task,output_format=output_format)
    else:
        task = text_task.format(page_info = page_info)
        prompt = write_original_prompt.format(role=role,task=task,output_format=output_format)
    return prompt