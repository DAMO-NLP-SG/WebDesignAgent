original_role_en = "You are an expert Html developer.You are very good at writing a webpage by using HTML, CSS, and JavaScript.(No need to output js file, embed js file into html file)"

Tailwind_role_en = "You are an expert Tailwind developer.You are very good at writing a webpage by using Tailwind CSS framework."

Boostrap_role_en = "You are an expert Bootstrap developer.You are very good at writing a webpage by using Bootstrap CSS framework."

Materialize_role_en = "You are an expert Materialize developer.You are very good at writing a webpage by using Materialize CSS framework."

Bulma_role_en = "You are an expert Bulma developer.You are very good at writing a webpage by using Bulma CSS framework."

img_task_en = """
The above picture is a screenshot of the webpage we provide to you. 
The page relationship is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);
Your task is to build a single page app according to the screenshot and the page relationship.
- Make sure the your create page looks exactly like the screenshot.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly.
- Use the exact text from the screenshot.
- Repeat elements as needed to match the screenshot. For example, if there are 15 items, the code should have 15 items. DO NOT LEAVE comments like "<!-- Repeat for each news item -->" or bad things will happen.
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.
- Avoid using images as background. Such as: background: url('https://placehold.co/1600x900').
- You must ensure that the page you generate is completely consistent with the page we provide(Layout, Format, Text, Content)!
- You are encouraged to use more js to implement some operation functions to make the page more practical and interesting.
"""

text_img_task_en = """
The above picture is a screenshot of the reference webpage we provide to you. 
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);
Your task is to build a new web page by imitating the structure and layout of the reference web page and the provided page information
- Don't match the text on the reference webpage! Add text based on your own needs!
- It does not need to be consistent with the reference web page, just learn from its excellent points.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.
- Try to make the page appear rich and not boring. 
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Avoid using images as background. Such as: background: url('https://placehold.co/1600x900').
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
- If you want to add images through constants in js, please define constants in the following way:
const imageInfo = {{
imgsrc: "https://placehold.co/1600x900",
alt: "This is an example image",
width: 600,
height: 400,
title: "Example image title",
}}
That is, be sure to use "imgsrc" to add the image address(use placeholder images from https://placehold.co), and use "alt" to describe the image content(an image generation AI can generate the image later), and add other keywords as needed.
- You are encouraged to enhance the interactivity and functionality of the webpage by implementing additional JavaScript operation functions. Aim to make the page more practical and engaging for users.
"""

text_task_en = """
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);
Your task is to build a single page app according to the page information.
- Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. 
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.
- Try to make the page appear rich and not boring. 
- Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
- Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on.
- Avoid using images as background. Such as: background: url('https://placehold.co/1600x900').
- If you want to add images through constants in js, please define constants in the following way:
const imageInfo = {{
imgsrc: "https://placehold.co/1600x900",
alt: "This is an example image",
width: 600,
height: 400,
title: "Example image title",
}}
That is, be sure to use "imgsrc" to add the image address(use placeholder images from https://placehold.co), and use "alt" to describe the image content(an image generation AI can generate the image later), and add other keywords as needed.
- You are encouraged to enhance the interactivity and functionality of the webpage by implementing additional JavaScript operation functions. Aim to make the page more practical and engaging for users.
"""

# - Use the Tailwind CSS framework to style the page.
original_output_format_en = """
{feedback}

Please output the html(contain js code), css code.
"""

Tailwind_output_format_en = """
{feedback}

Now output the HTML code with Tailwind CSS framework.
"""

Boostrap_output_format_en = """
{feedback}

Now output the HTML code with Bootstrap CSS framework.
"""

Materialize_output_format_en = """
{feedback}

Now output the HTML code with Materialize CSS framework.
"""

Bulma_output_format_en = """
{feedback}

Now output the HTML code with Bulma CSS framework.
"""

original_role_zh = "您是一位专家级的Html开发者，擅长使用HTML、CSS和JavaScript编写网页。(无需输出js文件，将js文件嵌入到html文件中)"

Tailwind_role_zh = "您是一位专家级的Tailwind开发者，擅长使用Tailwind CSS框架编写网页。"

Boostrap_role_zh = "您是一位专家级的Bootstrap开发者，擅长使用Bootstrap CSS框架编写网页。"

Materialize_role_zh = "您是一位专家级的Materialize开发者，擅长使用Materialize CSS框架编写网页。"

Bulma_role_zh = "您是一位专家级的Bulma开发者，擅长使用Bulma CSS框架编写网页。"

img_task_zh = """
上图是我们提供给您的网页的截图。
页面关系如下:{page_info}(button和link的跳转页面的文件名为其链接地址);
您的任务是根据截图和页面关系构建一个单页面应用。
- 确保您创建的页面与截图完全一致。
- 请注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。确保颜色和大小完全匹配。
- 使用截图中的确切文本。
- 根据需要重复元素以匹配截图。例如，如果有15个项目，则代码应该有15个项目。
- 对于图像，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。
- 避免使用图像作为背景。例如: background: url('https://placehold.co/1600x900')。
- 您必须确保您生成的页面与我们提供的页面完全一致(布局、格式、文本、内容)!
- 鼓励您使用更多js来实现一些操作功能，使页面更加实用和有趣。
"""

text_img_task_zh = """
上图是我们提供给您的参考网页的截图。
页面信息如下:{page_info}(button和link的跳转页面的文件名为其链接地址);
您的任务是根据参考网页的结构和布局以及提供的页面信息构建一个新的网页。
- 不要匹配参考网页上的文本! 根据自己的需要添加文本!
- 不需要与参考网页一致，只需学习其优点。
- 请注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。
- 对于图像，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。
- 尽量使页面看起来丰富而不乏味。
- 应注意协调，例如，技术网站应设计有技术感，而购物网站应具有新鲜感。
- 避免使用图像作为背景。例如: background: url('https://placehold.co/1600x900')。
- 鼓励您使用更多颜色、更多按钮、更精致的布局，并尝试添加更多特效，例如波浪效果、渐变效果、滚动效果等。
- 如果您想通过js中的常量添加图像，请以以下方式定义常量:
const imageInfo = {{
imgsrc: "https://placehold.co/1600x900",
alt: "这是一张参考图片",
width: 600,
height: 400,
title: "参考图片标题",
}}
也就是说，一定要使用"imgsrc"添加图像地址(使用https://placehold.co中的占位图像)，使用"alt"描述图像内容(图像生成AI稍后可以生成图像)，并根据需要添加其他关键字。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的互动性和功能性。目的是使页面对用户更实用和吸引。
"""

text_task_zh = """
页面信息如下:{page_info}(button和link的跳转页面的文件名为其链接地址);
您的任务是根据页面信息构建一个单页面应用。
- 请注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。
- 对于图像，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。
- 尽量使页面看起来丰富而不乏味。
- 应注意协调，例如，技术网站应设计有技术感，而购物网站应具有新鲜感。
- 鼓励您使用更多颜色、更多按钮、更精致的布局，并尝试添加更多特效，例如波浪效果、渐变效果、滚动效果等。
- 避免使用图像作为背景。例如: background: url('https://placehold.co/1600x900')。
- 如果您想通过js中的常量添加图像，请以以下方式定义常量:
const imageInfo = {{
imgsrc: "https://placehold.co/1600x900",
alt: "这是一张参考图片",
width: 600,
height: 400,
title: "参考图片标题",
}}
也就是说，一定要使用"imgsrc"添加图像地址(使用https://placehold.co中的占位图像)，使用"alt"描述图像内容(图像生成AI稍后可以生成图像)，并根据需要添加其他关键字。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的互动性和功能性。目的是使页面对用户更实用和吸引。
"""

original_output_format_zh = """
{feedback}

请输出html(包含js代码)，css代码。
"""

Tailwind_output_format_zh = """
{feedback}

现在输出带有Tailwind CSS框架的HTML代码。
"""

Boostrap_output_format_zh = """
{feedback}

现在输出带有Bootstrap CSS框架的HTML代码。
"""

Materialize_output_format_zh = """
{feedback}

现在输出带有Materialize CSS框架的HTML代码。
"""

Bulma_output_format_zh = """
{feedback}

现在输出带有Bulma CSS框架的HTML代码。
"""



write_original_prompt = """
{role}
{task}
{output_format}
"""



def get_write_original_website_prompt(text = None,img = None,page_info = None,css_frame = None,feedback = "",language = "en"):
    if language == "en":
        feedback = f"The user's requirements is as follows(very important, please pay attention to it!):{feedback}" if feedback else ""
        if css_frame == "Tailwind":
            role = Tailwind_role_en
            output_format = Tailwind_output_format_en.format(feedback=feedback)
        elif css_frame == "Boostrap":
            role = Boostrap_role_en
            output_format = Boostrap_output_format_en.format(feedback=feedback)
        elif css_frame == "Materialize":
            role = Materialize_role_en
            output_format = Materialize_output_format_en.format(feedback=feedback)
        elif css_frame == "Bulma":
            role = Bulma_role_en
            output_format = Bulma_output_format_en.format(feedback=feedback)
        else:
            role = original_role_en
            output_format = original_output_format_en.format(feedback=feedback)
        if img and text:
            task = text_img_task_en.format(page_info=page_info)
            prompt = write_original_prompt.format(role=role,task=task,page_info=page_info,output_format=output_format)
        elif img:
            try:
                page_info = page_info["relationship"]
            except:
                page_info = page_info
            task = img_task_en.format(page_info=page_info)
            prompt = write_original_prompt.format(role=role,task=task,output_format=output_format)
        else:
            task = text_task_en.format(page_info = page_info)
            prompt = write_original_prompt.format(role=role,task=task,output_format=output_format)
        return prompt
    elif language == "zh":
        feedback = f"用户的需求如下(非常重要，请注意!):{feedback}" if feedback else ""
        if css_frame == "Tailwind":
            role = Tailwind_role_zh
            output_format = Tailwind_output_format_zh.format(feedback=feedback)
        elif css_frame == "Boostrap":
            role = Boostrap_role_zh
            output_format = Boostrap_output_format_zh.format(feedback=feedback)
        elif css_frame == "Materialize":
            role = Materialize_role_zh
            output_format = Materialize_output_format_zh.format(feedback=feedback)
        elif css_frame == "Bulma":
            role = Bulma_role_zh
            output_format = Bulma_output_format_zh.format(feedback=feedback)
        else:
            role = original_role_zh
            output_format = original_output_format_zh.format(feedback=feedback)
        if img and text:
            task = text_img_task_zh.format(page_info=page_info)
            prompt = write_original_prompt.format(role=role,task=task,page_info=page_info,output_format=output_format)
        elif img:
            try:
                page_info = page_info["relationship"]
            except:
                page_info = page_info
            task = img_task_zh.format(page_info=page_info)
            prompt = write_original_prompt.format(role=role,task=task,output_format=output_format)
        else:
            task = text_task_zh.format(page_info = page_info)
            prompt = write_original_prompt.format(role=role,task=task,output_format=output_format)
        return prompt


if __name__ == "__main__":
    frames = ["Tailwind","Boostrap","Materialize","Bulma"]
    texts = ["a technology website","a shopping website"]
    imgs = [None]
    page_infos = [None]
    print(get_write_original_website_prompt(text="a technology website",page_info="a technology website"))