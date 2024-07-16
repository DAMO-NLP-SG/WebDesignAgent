original_role = "You are an expert Html developer.You are very good at writing a webpage by using HTML, CSS, and JavaScript.(No need to output js file, embed js file into html file)"

Tailwind_role = "You are an expert Tailwind developer.You are very good at writing a webpage by using Tailwind CSS framework."

Boostrap_role = "You are an expert Bootstrap developer.You are very good at writing a webpage by using Bootstrap CSS framework."

Materialize_role = "You are an expert Materialize developer.You are very good at writing a webpage by using Materialize CSS framework."

Bulma_role = "You are an expert Bulma developer.You are very good at writing a webpage by using Bulma CSS framework."

refine_img_task = """
The first image is a screenshot of our target webpage, and the second image is a web page screenshot that you have already built. 
{local_img_storage}
The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Your goal is to modify the code of the second webpage to update it to look more like the target page(The first image).

- Make sure the page you create is exactly the same as the screenshot.
- Pay attention to the layout of the page, image distribution, image size, related text, buttons, links, etc. to be consistent with the screenshot.
- Pay attention to the background color, text color, font size, font family, padding, margins, borders, etc. Exactly match the color and size to be consistent with the screenshot.
- Use the exact text from the screenshot.
- Be careful not to let the image cover the text, the text layer should be the top layer.
- Please pay close attention to the image size to ensure that the final page looks good.
- Avoid using images as background. Such as: background: url('https://placehold.co/1600x900').
- Repeat elements as needed to match the screenshot. For example, if there are 15 items, the code should have 15 items. DO NOT LEAVE comments like "<!-- Repeat for each news item -->" or bad things will happen.
- For images, try to use local images in the page information and do not modify its file path. If you want to add additional images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later. For images that already exist on the web page, do not change their address.
- You are encouraged to enhance the interactivity and functionality of web pages by implementing additional JavaScript operations (e.g. scrolling, clicking, hovering, color changes, click effects, page switching, etc.). The purpose is to make the page more practical and attractive to users.
"""

refine_img_text_task = """
The first image is a screenshot of reference webpage, and the second image is a web page screenshot that you have already built. 
{local_img_storage}
The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Your goal is to modify the webpage code of the second img by imitating the layout structure of the first img and meet the page information requirements. 
- Don't match the text on the reference webpage! Add text based on your own needs!
- It does not need to be consistent with the reference web page, just learn from its excellent points.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- Try to make the page look rich and not boring, such as using rich background colors, button colors, font colors, etc.
- Please pay close attention to the image size to ensure that the final page looks good.
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
- Enhanced Functionality and Practicality: Think about how to improve the functionality and practicality of the page by modifying the code.
- You need to learn the good points of the reference webpage and adopt them into your web design, not just copy them.
- For images, try to use local images in the page information and do not modify its file path. If you want to add additional images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later. For images that already exist on the web page, do not change their address.
- Be careful not to let the image cover the text, the text layer should be the top layer.
- Avoid using placehold as background. Such as: background: url('https://placehold.co/1600x900').You can use gradient colors as background or local images as background.
- Please analyze the current page's header, navigation, content arrangement, sidebars, footers, visual elements, layout, call to action, responsiveness, and any other features, and analyze how to optimize these to make the layout more beautiful and harmonious.
- Please think about how to modify the code to make the page meet our needs (such as adding images, adding buttons, increasing animation effectsincreasing animation effects or add some text content, detailed content etc.).
- If you want to add images through constants in js, please define constants in the following way:
const imageInfo = {{
imgsrc: "search.png",
alt: "This is an example image",
width: 600,
height: 400,
title: "Example image title",
}}
That is, be sure to use "imgsrc" to add the image address(try to use a local address, otherwise use a placeholder image from https://placehold.co), and use "alt" to describe the image content(an image generation AI can generate the image later), and add other keywords as needed.
- You are encouraged to enhance the interactivity and functionality of web pages by implementing additional JavaScript operations (e.g. scrolling, clicking, hovering, color changes, click effects, page switching, etc.). The purpose is to make the page more practical and attractive to users.
"""

refine_text_task = """
{local_img_storage}
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);

Your task is to modify the code of the current webpage to update it to meet the page information requirements and make the page more beautiful and harmonious.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- For images, try to use local images in the page information and do not modify its file path. If you want to add additional images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later. For images that already exist on the web page, do not change their address.
- Try to make the page look rich and not boring, such as using rich background colors, button colors, font colors, etc.
- Please pay close attention to the image size to ensure that the final page looks good.
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
- Avoid using placehold as background. Such as: background: url('https://placehold.co/1600x900').You can use gradient colors as background or local images as background.
- Enhanced Functionality and Practicality: Think about how to improve the functionality and practicality of the page by modifying the code.
- You need to learn the good points of the reference webpage and adopt them into your web design, not just copy them.
- Please analyze the current page's header, navigation, content arrangement, sidebars, footers, visual elements, layout, call to action, responsiveness, and any other features, and analyze how to optimize these to make the layout more beautiful and harmonious.
- Please think about how to modify the code to make the page meet our needs (such as adding images, adding buttons, increasing animation effectsincreasing animation effects or add some text content, detailed content etc.).
- If you want to add images through constants in js, please define constants in the following way:
const imageInfo = {{
imgsrc: "search.png",
alt: "This is an example image",
width: 600,
height: 400,
title: "Example image title",
}}
That is, be sure to use "imgsrc" to add the image address(try to use a local address, otherwise use a placeholder image from https://placehold.co), and use "alt" to describe the image content(an image generation AI can generate the image later), and add other keywords as needed.
- You are encouraged to enhance the interactivity and functionality of web pages by implementing additional JavaScript operations (e.g. scrolling, clicking, hovering, color changes, click effects, page switching, etc.). The purpose is to make the page more practical and attractive to users.
"""

refine_feedback_task = """
{local_img_storage}
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);

Your task is to modify your code based on user feedback to meet user needs.
- Pay close attention to human's feedback and modify the code to make the page more beautiful and harmonious.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- For images, try to use local images in the page information and do not modify its file path. If you want to add additional images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later. For images that already exist on the web page, do not change their address.
- Try to make the page look rich and not boring, such as using rich background colors, button colors, font colors, etc.
- Please pay close attention to the image size to ensure that the final page looks good.
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
- Avoid using placehold as background. Such as: background: url('https://placehold.co/1600x900').You can use gradient colors as background or local images as background.
- Enhanced Functionality and Practicality: Think about how to improve the functionality and practicality of the page by modifying the code.
- You need to learn the good points of the reference webpage and adopt them into your web design, not just copy them.
- Please analyze the current page's header, navigation, content arrangement, sidebars, footers, visual elements, layout, call to action, responsiveness, and any other features, and analyze how to optimize these to make the layout more beautiful and harmonious.
- Please think about how to modify the code to make the page meet our needs (such as adding images, adding buttons, increasing animation effectsincreasing animation effects or add some text content, detailed content etc.).
- If you want to add images through constants in js, please define constants in the following way:
const imageInfo = {{
imgsrc: "search.png",
alt: "This is an example image",
width: 600,
height: 400,
title: "Example image title",
}}
That is, be sure to use "imgsrc" to add the image address(try to use a local address, otherwise use a placeholder image from https://placehold.co), and use "alt" to describe the image content(an image generation AI can generate the image later), and add other keywords as needed.
- You are encouraged to enhance the interactivity and functionality of web pages by implementing additional JavaScript operations (e.g. scrolling, clicking, hovering, color changes, click effects, page switching, etc.). The purpose is to make the page more practical and attractive to users.
"""



refine_original_output_format = """
The code of current page are as follows:
The HTML code is: 
{html_code}
The CSS code is: 
{css_code}

{feedback}
Please provide a modification plan and then output the modified html(contains js code), css code of second page.
The output format is as follows:
The shortcomings of the current webpage:
1.
2.

Modify plan:
1.
2.
...

modified html:

modified css:

"""

refine_Tailwind_output_format = """
The code of current page are as follows:
The HTML code with Tailwind CSS framework is:
{html_code}

{feedback}
please provide a modification plan and then output the modified html code of second page.
The output format is as follows:
The shortcomings of the current webpage:
1.
2.

Modify plan:
1.
2.
...

modified html:
"""

refine_Boostrap_output_format = """
The code of current page are as follows:
The HTML code with Bootstrap CSS framework is:
{html_code}

{feedback}
please provide a modification plan and then output the modified html code of second page.
The output format is as follows:
The shortcomings of the current webpage:
1.
2.

Modify plan:
1.
2.
...

modified html:
"""

refine_Materialize_output_format = """
The code of current page are as follows:
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
The code of current page are as follows:
The HTML code with Bulma CSS framework is:
{html_code}

{feedback}
please provide a modification plan and then output the modified html code of second page.
The output format is as follows:
The shortcomings of the current webpage:
1.
2.

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