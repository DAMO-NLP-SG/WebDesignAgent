original_role = "You are an expert Html developer.You are very good at writing a webpage by using HTML, CSS, and JavaScript."

Tailwind_role = "You are an expert Tailwind developer.You are very good at writing a webpage by using Tailwind CSS framework."

Boostrap_role = "You are an expert Bootstrap developer.You are very good at writing a webpage by using Bootstrap CSS framework."

Materialize_role = "You are an expert Materialize developer.You are very good at writing a webpage by using Materialize CSS framework."

Bulma_role = "You are an expert Bulma developer.You are very good at writing a webpage by using Bulma CSS framework."

img_task = """
The above picture is a screenshot of the webpage we provide to you. 
The page relationship is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);
Your task is to build a single page app according to the screenshot and the page relationship.
- Make sure the your create page looks exactly like the screenshot.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly.
- Use the exact text from the screenshot.
- Do not add comments in the code such as "<!-- Add other navigation links as needed -->" and "<!-- ... other news items ... -->" in place of writing the full code. WRITE THE FULL CODE.
- Repeat elements as needed to match the screenshot. For example, if there are 15 items, the code should have 15 items. DO NOT LEAVE comments like "<!-- Repeat for each news item -->" or bad things will happen.
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.
- You must ensure that the page you generate is completely consistent with the page we provide(Layout, Format, Text, Content)!
- You are encouraged to use more js to implement some operation functions to make the page more practical and interesting.
"""

text_img_task = """
The above picture is a screenshot of the webpage we provide to you. 
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);
Your task is to build a single page app according to the screenshot and the page information.
- Make sure the your create page's layout looks exactly like the screenshot.(content can be different).
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- Do not add comments in the code such as "<!-- Add other navigation links as needed -->" and "<!-- ... other news items ... -->" in place of writing the full code. WRITE THE FULL CODE.
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.
- Try to make the page appear rich and not boring. 
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
- You are encouraged to use more js to implement some operation functions to make the page more practical and interesting.
"""

text_task = """
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);
Your task is to build a single page app according to the page information.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- Do not add comments in the code such as "<!-- Add other navigation links as needed -->" and "<!-- ... other news items ... -->" in place of writing the full code. WRITE THE FULL CODE.
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.
- Try to make the page appear rich and not boring. 
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on.
- You are encouraged to use more js to implement some operation functions to make the page more practical and interesting.
"""

# - Use the Tailwind CSS framework to style the page.
original_output_format = """
Please output the html, css and js code.
"""

Tailwind_output_format = """
Now output the HTML code with Tailwind CSS framework.
"""

Boostrap_output_format = """
Now output the HTML code with Bootstrap CSS framework.
"""

Materialize_output_format = """
Now output the HTML code with Materialize CSS framework.
"""

Bulma_output_format = """
Now output the HTML code with Bulma CSS framework.
"""

write_original_prompt = """
{role}
{task}
{output_format}
"""



def get_write_original_website_prompt(text = None,img = None,page_info = None,css_frame = None):
    if css_frame == "Tailwind":
        role = Tailwind_role
        output_format = Tailwind_output_format
    elif css_frame == "Boostrap":
        role = Boostrap_role
        output_format = Boostrap_output_format
    elif css_frame == "Materialize":
        role = Materialize_role
        output_format = Materialize_output_format
    elif css_frame == "Bulma":
        role = Bulma_role
        output_format = Bulma_output_format
    else:
        role = original_role
        output_format = original_output_format
    if img and text:
        task = text_img_task.format(page_info=page_info)
        prompt = write_original_prompt.format(role=role,task=task,page_info=page_info,output_format=output_format)
    elif img:
        try:
            page_info = page_info["relationship"]
        except:
            page_info = page_info
        task = img_task.format(page_info=page_info)
        prompt = write_original_prompt.format(role=role,task=task,output_format=output_format)
    else:
        task = text_task.format(page_info = page_info)
        prompt = write_original_prompt.format(role=role,task=task,output_format=output_format)
    return prompt


if __name__ == "__main__":
    frames = ["Tailwind","Boostrap","Materialize","Bulma"]
    texts = ["a technology website","a shopping website"]
    imgs = [None]
    page_infos = [None]
    print(get_write_original_website_prompt(text="a technology website",page_info="a technology website"))