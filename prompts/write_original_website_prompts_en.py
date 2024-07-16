original_role = "You are an expert Html developer.You are very good at writing a webpage by using HTML, CSS, and JavaScript.(No need to output js file, embed js file into html file)"

Tailwind_role = "You are an expert Tailwind developer.You are very good at writing a webpage by using Tailwind CSS framework."

Boostrap_role = "You are an expert Bootstrap developer.You are very good at writing a webpage by using Bootstrap CSS framework."

Materialize_role = "You are an expert Materialize developer.You are very good at writing a webpage by using Materialize CSS framework."

Bulma_role = "You are an expert Bulma developer.You are very good at writing a webpage by using Bulma CSS framework."

img_task = """
The above picture is a screenshot of the webpage we provide to you. 
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);
Your task is to build a single page app according to the screenshot and the page relationship.
- Make sure the page you create is exactly the same as the screenshot.
- Pay attention to the layout of the page, image distribution, image size, related text, buttons, links, etc. to be consistent with the screenshot.
- Pay attention to the background color, text color, font size, font family, padding, margins, borders, etc. Exactly match the color and size to be consistent with the screenshot.
- Use the exact text from the screenshot.
- Be careful not to let the image cover the text, the text layer should be the top layer.
- Please pay close attention to the image size to ensure that the final page looks good.
- Repeat elements as needed to match the screenshot. For example, if there are 15 items, the code should have 15 items. DO NOT LEAVE comments like "<!-- Repeat for each news item -->" or bad things will happen.
- For images, try to use local images in the page information and do not modify its file path. If you want to add additional images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.
- Avoid using placehold as background. Such as: background: url('https://placehold.co/1600x900').You can use gradient colors as background or local images as background.
- You must ensure that the page you generate is completely consistent with the page we provide(Layout, Format, Text, Content)!
- You are encouraged to enhance the interactivity and functionality of web pages by implementing additional JavaScript operations (e.g. scrolling, clicking, hovering, color changes, click effects, page switching, etc.). The purpose is to make the page more practical and attractive to users.
"""

text_img_task = """
The above picture is a screenshot of the reference webpage we provide to you. 
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);
Your task is to build a new web page by imitating the structure and layout of the reference web page and the provided page information
- Don't match the text on the reference webpage! Add text based on your own needs!
- Be careful not to let the image cover the text, the text layer should be the top layer.
- It does not need to be consistent with the reference web page, just learn from its excellent points.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- For images, try to use local images in the page information and do not modify its file path. If you want to add additional images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.
- Try to make the page look rich and not boring, such as using rich background colors, button colors, font colors, etc.
- Please pay close attention to the image size to ensure that the final page looks good.
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Avoid using placehold as background. Such as: background: url('https://placehold.co/1600x900').You can use gradient colors as background or local images as background.
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
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

text_task = """
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);
Your task is to build a single page app according to the page information.
- Be careful not to let the image cover the text, the text layer should be the top layer.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- For images, try to use local images in the page information and do not modify its file path. If you want to add additional images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.
- Try to make the page look rich and not boring, such as using rich background colors, button colors, font colors, etc.
- Please pay close attention to the image size to ensure that the final page looks good.
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on.
- Avoid using placehold as background. Such as: background: url('https://placehold.co/1600x900').You can use gradient colors as background or local images as background.
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

# - Use the Tailwind CSS framework to style the page.
original_output_format = """
{feedback}

Now please export your web design plan and finally output the html(contain js code), css code.
"""

Tailwind_output_format = """
{feedback}

Now please export your web design plan and finally output the HTML code with Tailwind CSS framework.(Must add link :<link href="https://cdn.jsdelivr.net/npm/tailwindcss@latest/dist/tailwind.min.css" rel="stylesheet"> to your html file.)
"""

Boostrap_output_format = """
{feedback}

Now please export your web design plan and finally output the HTML code with Bootstrap CSS framework.(Must add link :<link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet"> to your html file.)
"""

Materialize_output_format = """
{feedback}

Now please export your web design plan and finally output the HTML code with Materialize CSS framework.(Must add link :<link href="https://cdn.jsdelivr.net/npm/materialize-css@latest/dist/css/materialize.min.css" rel="stylesheet"> to your html file.)
"""

Bulma_output_format = """
{feedback}

Now please export your web design plan and finally output the HTML code with Bulma CSS framework.(Must add link :<link href="https://cdn.jsdelivr.net/npm/bulma@latest/dist/css/bulma.min.css" rel="stylesheet"> to your html file.)
"""

write_original_prompt = """
{role}
{task}
{output_format}
"""