original_role = "You are an expert Html developer.You are very good at writing a webpage by using HTML, CSS, and JavaScript.(No need to output js file, embed js file into html file)"

Tailwind_role = "You are an expert Tailwind developer.You are very good at writing a webpage by using Tailwind CSS framework."

Boostrap_role = "You are an expert Bootstrap developer.You are very good at writing a webpage by using Bootstrap CSS framework."

Materialize_role = "You are an expert Materialize developer.You are very good at writing a webpage by using Materialize CSS framework."

Bulma_role = "You are an expert Bulma developer.You are very good at writing a webpage by using Bulma CSS framework."

refine_img_task = """
The first image is a screenshot of our target webpage, and the second image is a web page screenshot that you have already built. 
The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Your goal is to modify the code of the second webpage to update it to look more like the target page(The first image).

- Make sure your create page looks exactly like the screenshot.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly.
- Use the exact text from the screenshot.
- Avoid using images as background. Such as: background: url('https://placehold.co/1600x900').
- Repeat elements as needed to match the screenshot. For example, if there are 15 items, the code should have 15 items. DO NOT LEAVE comments like "<!-- Repeat for each news item -->" or bad things will happen.
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.For images that already exist on the web page, do not change their address.
- You are encouraged to enhance the interactivity and functionality of the webpage by implementing additional JavaScript operation functions. Aim to make the page more practical and engaging for users.
"""

refine_img_text_task = """
The first image is a screenshot of reference webpage, and the second image is a web page screenshot that you have already built. 
The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Your goal is to modify the webpage code of the second img by imitating the layout structure of the first img and meet the page information requirements. 
- Don't match the text on the reference webpage! Add text based on your own needs!
- It does not need to be consistent with the reference web page, just learn from its excellent points.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.For images that already exist on the web page, do not change their address.
- Try to make the page appear rich and not boring. 
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
- Avoid using images as background. Such as: background: url('https://placehold.co/1600x900').
- Enhanced Functionality and Practicality: Think about how to improve the functionality and practicality of the page by modifying the code.
- You need to learn the good points of the reference webpage and adopt them into your web design, not just copy them.
- Please analyze the current page's header, navigation, content arrangement, sidebars, footers, visual elements, layout, call to action, responsiveness, and any other features, and analyze how to optimize these to make the layout more beautiful and harmonious.
- Please think about how to modify the code to make the page meet our needs (such as adding images, adding buttons, increasing animation effectsincreasing animation effects or add some text content, detailed content etc.).
- If you want to add images through constants in js, please define constants in the following way:
const imageInfo = {{
imgsrc: "https://via.placeholder.com/150",
alt: "This is an example image",
width: 600,
height: 400,
title: "Example image title",
}}
That is, be sure to use "imgsrc" to add the image address(use placeholder images from https://placehold.co), and use "alt" to describe the image content(an image generation AI can generate the image later), and add other keywords as needed.
- You are encouraged to enhance the interactivity and functionality of the webpage by implementing additional JavaScript operation functions. Aim to make the page more practical and engaging for users.
"""

refine_text_task = """
The image above is a web page screenshot that you have already built.
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);

Your task is to modify the code of the current webpage to update it to meet the page information requirements and make the page more beautiful and harmonious.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.For images that already exist on the web page, do not change their address.
- Try to make the page appear rich and not boring. 
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on.
- Avoid using images as background. Such as: background: url('https://placehold.co/1600x900').
- Enhanced Functionality and Practicality: Think about how to improve the functionality and practicality of the page by modifying the code.
- Please analyze the current page's header, navigation, content arrangement, sidebars, footers, visual elements, layout, call to action, responsiveness, and any other features, and analyze how to optimize these to make the layout more beautiful and harmonious.
- Please think about how to modify the code to make the page meet our needs (such as adding images, adding buttons, increasing animation effectsincreasing animation effects or add some text content, detailed content etc.).
- If you want to add images through constants in js, please define constants in the following way:
const imageInfo = {{
imgsrc: "https://via.placeholder.com/150",
alt: "This is an example image",
width: 600,
height: 400,
title: "Example image title",
}}
That is, be sure to use "imgsrc" to add the image address(use placeholder images from https://placehold.co), and use "alt" to describe the image content(an image generation AI can generate the image later), and add other keywords as needed.
- You are encouraged to enhance the interactivity and functionality of the webpage by implementing additional JavaScript operation functions. Aim to make the page more practical and engaging for users.
"""

refine_feedback_task = """
The image above is a web page screenshot that you have already built.
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);

Your task is to modify your code based on user feedback to meet user needs.
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.For images that already exist on the web page, do not change their address.
- You must pay close attention to user feedback and try to modify your code based on user feedback so that the final effect meets user needs.
- You can add js or modify the css layout, or add elements to meet user feedback.
- Avoid using images as background. Such as: background: url('https://placehold.co/1600x900').
- If you want to add images through constants in js, please define constants in the following way:
const imageInfo = {{
imgsrc: "https://via.placeholder.com/150",
alt: "This is an example image",
width: 600,
height: 400,
title: "Example image title",
}}
That is, be sure to use "imgsrc" to add the image address(use placeholder images from https://placehold.co), and use "alt" to describe the image content(an image generation AI can generate the image later), and add other keywords as needed.
- You are encouraged to enhance the interactivity and functionality of the webpage by implementing additional JavaScript operation functions. Aim to make the page more practical and engaging for users.
"""



refine_original_output_format = """
The code of second page are as follows:
The HTML code is: 
{html_code}
The CSS code is: 
{css_code}

{feedback}
Please provide a modification plan and then output the modified html(contains js code), css code of second page.
The output format is as follows:
Modify plan:
1.
2.
...

modified html:

modified css:

"""

refine_Tailwind_output_format = """
The code of second page are as follows:
The HTML code with Tailwind CSS framework is:
{html_code}

{feedback}
please provide a modification plan and then output the modified html code of second page.
The output format is as follows:
Modify plan:
1.
2.
...

modified html:
"""

refine_Boostrap_output_format = """
The code of second page are as follows:
The HTML code with Bootstrap CSS framework is:
{html_code}

{feedback}
please provide a modification plan and then output the modified html code of second page.
The output format is as follows:
Modify plan:
1.
2.
...

modified html:
"""

refine_Materialize_output_format = """
The code of second page are as follows:
The HTML code with Materialize CSS framework is:
{html_code}

{feedback}
please provide a modification plan and then output the modified html code of second page.
The output format is as follows:
Modify plan:
1.
2.
...

modified html:
"""

refine_Bulma_output_format = """
The code of second page are as follows:
The HTML code with Bulma CSS framework is:
{html_code}

{feedback}
please provide a modification plan and then output the modified html code of second page.
The output format is as follows:
Modify plan:
1.
2.
...

modified html:

"""

refine_prompt = """
{role}
{task}
{output_format}
"""

# ["Tailwind","Boostrap","Materialize","Bulma",None]
def get_refine_prompt(text = None,img = None,html_code = None,css_code = None,page_info = None,feedback = "",css_frame = None):
    feedback = f"The feedback is as follows(very important, please pay attention to it!):{feedback}" if feedback else ""
    if css_frame == "Tailwind":
        role = Tailwind_role
        output_format = refine_Tailwind_output_format.format(html_code = html_code,feedback = feedback)
    elif css_frame == "Boostrap":
        role = Boostrap_role.format(html_code = html_code)
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
        task = refine_feedback_task.format(page_info = page_info,feedback = feedback)
    elif img and text:
        task = refine_img_text_task.format(page_info = page_info)
    elif img:
        task = refine_img_task.format(page_info = page_info)
    else:
        task = refine_text_task.format(page_info = page_info)

    prompt = refine_prompt.format(role = role,task = task,output_format = output_format)
    return prompt


if __name__ == "__main__":
    frames = ["Tailwind","Boostrap","Materialize","Bulma"]
    texts = ["a technology website","a shopping website"]
    imgs = [None,"1"]
    page_infos = [None,"1"]
    css_code = "<div class='container'><div class='row'><div class='col-md-12'><h1>Hello, World!</h1></div></div></div>"
    html_code = "<html><head></head><body><h1>Hello, World!</h1></body></html>"
    js_code = ""
    feedback = "The page layout is not balanced, and the color scheme is not harmonious."
    for frame in frames:
        for text in texts:
            for img in imgs:
                for page_info in page_infos:
                    print(get_refine_prompt(text = text,img = img,html_code = html_code,css_code = css_code,js_code = js_code,page_info = page_info,feedback = feedback,css_frame = frame))
                    print("\n\n")