original_role_en = "You are an expert Html developer.You are very good at writing a webpage by using HTML, CSS, and JavaScript.(No need to output js file, embed js file into html file)"

Tailwind_role_en = "You are an expert Tailwind developer.You are very good at writing a webpage by using Tailwind CSS framework."

Boostrap_role_en = "You are an expert Bootstrap developer.You are very good at writing a webpage by using Bootstrap CSS framework."

Materialize_role_en = "You are an expert Materialize developer.You are very good at writing a webpage by using Materialize CSS framework."

Bulma_role_en = "You are an expert Bulma developer.You are very good at writing a webpage by using Bulma CSS framework."

refine_img_task_en = """
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

refine_img_text_task_en = """
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
- If you want to add images through constants in js, Please refer to the following form for definition:
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

refine_text_task_en = """
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
- If you want to add images through constants in js, Please refer to the following form for definition:
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

refine_feedback_task_en = """
The image above is a web page screenshot that you have already built.
The page information is as follows:{page_info}(The file names of the jump pages of the bottom and link are their link addresses);

Your task is to modify your code based on user feedback to meet user needs.
- For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.For images that already exist on the web page, do not change their address.
- You must pay close attention to user feedback and try to modify your code based on user feedback so that the final effect meets user needs.
- You can add js or modify the css layout, or add elements to meet user feedback.
- Avoid using images as background. Such as: background: url('https://placehold.co/1600x900').
- If you want to add images through constants in js, Please refer to the following form for definition:
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



refine_original_output_format_en = """
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

refine_Tailwind_output_format_en = """
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

refine_Boostrap_output_format_en = """
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

refine_Materialize_output_format_en = """
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

refine_Bulma_output_format_en = """
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

original_role_zh = "您是一位专家级的Html开发者，擅长使用HTML、CSS、JavaScript编写网页。(无需输出js文件，将js文件嵌入到html文件中即可)"

Tailwind_role_zh = "您是一位专家级的Tailwind开发者，擅长使用Tailwind CSS框架编写网页。"

Boostrap_role_zh = "您是一位专家级的Bootstrap开发者，擅长使用Bootstrap CSS框架编写网页。"

Materialize_role_zh = "您是一位专家级的Materialize开发者，擅长使用Materialize CSS框架编写网页。"

Bulma_role_zh = "您是一位专家级的Bulma开发者，擅长使用Bulma CSS框架编写网页。"

refine_img_task_zh = """
第一张图片是我们的目标网页的截图，第二张图片是您已经构建的网页截图。
页面信息如下：
{page_info}(button和link的跳转页面的文件名为其链接地址)

您的目标是修改第二个网页的代码，使其更新为更像目标页面(第一张图片)的样子。

- 确保您创建的页面与截图完全相同。
- 注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。完全匹配颜色和大小。
- 使用截图中的确切文本。
- 避免将图像用作背景。例如：background: url('https://placehold.co/1600x900')。
- 根据需要重复元素以匹配截图。例如，如果有15个项目，则代码应该有15个项目。
- 对于图像，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。对于已经存在于网页上的图像，请不要更改其地址。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的交互性和功能性。目的是使页面对用户更实用和吸引。
"""

refine_img_text_task_zh = """
第一张图片是参考网页的截图，第二张图片是您已经构建的网页截图。
页面信息如下：
{page_info}(button和link的跳转页面的文件名为其链接地址)

您的目标是修改第二个图片的网页代码，模仿第一个图片的布局结构，并满足页面信息要求。
- 不要匹配参考网页上的文本！根据自己的需要添加文本！
- 不需要与参考网页一致，只需从其优点中学习。
- 注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。
- 对于图像，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。对于已经存在于网页上的图像，请不要更改其地址。
- 尽量使页面看起来丰富而不乏味。
- 注意协调，例如，技术网站应设计具有技术感，而购物网站应具有新鲜感。
- 鼓励您使用更多的颜色、更多的按钮、更精致的布局，并尝试添加更多的特效，例如波浪效果、渐变效果、滚动效果等。
- 避免将图像用作背景。例如：background: url('https://placehold.co/1600x900')。

- 增强功能性和实用性：思考如何通过修改代码来提高页面的功能性和实用性。
- 请分析当前页面的页眉、导航、内容排列、侧边栏、页脚、视觉元素、布局、行动号召、响应性和其他功能，并分析如何优化这些功能，使布局更美观和和谐。
- 请思考如何修改代码以使页面满足我们的需求(例如添加图像、添加按钮、增加动画效果或添加一些文本内容、详细内容等)。
- 如果要通过js中的常量添加图像，请模仿以下方式定义常量：
const imageInfo = {{
imgsrc: "https://placehold.co/1600x900",
alt: "这是一个示例图像",
width: 600,
height: 400,
title: "示例图像标题",
}}
也就是说，一定要使用“imgsrc”添加图像地址(使用https://placehold.co中的占位图像)，使用“alt”描述图像内容(图像生成AI稍后可以生成图像)，并根据需要添加其他关键字。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的交互性和功能性。目的是使页面对用户更实用和吸引。
"""

refine_text_task_zh = """
上面的图片是您已经构建的网页截图。
页面信息如下：{page_info}(button和link的跳转页面的文件名为其链接地址);

您的任务是根据用户反馈修改代码，以满足用户需求。
- 对于图像，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。对于已经存在于网页上的图像，请不要更改其地址。
- 您必须密切关注用户反馈，并尝试根据用户反馈修改您的代码，以便最终效果符合用户需求。
- 您可以添加js或修改css布局，或添加元素以满足用户反馈。
- 避免将图像用作背景。例如：background: url('https://placehold.co/1600x900')。
- 如果要通过js中的常量添加图像，请模仿以下方式定义常量：
const imageInfo = {{
imgsrc: "https://placehold.co/1600x900",
alt: "这是一个示例图像",
width: 600,
height: 400,
title: "示例图像标题",
}}
也就是说，一定要使用“imgsrc”添加图像地址(使用https://placehold.co中的占位图像)，使用“alt”描述图像内容(图像生成AI稍后可以生成图像)，并根据需要添加其他关键字。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的交互性和功能性。目的是使页面对用户更实用和吸引。
"""

refine_feedback_task_zh = """
上面的图片是您已经构建的网页截图。
页面信息如下：{page_info}(button和link的跳转页面的文件名为其链接地址);

您的任务是根据用户反馈修改代码，以满足用户需求。
- 对于图像，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。对于已经存在于网页上的图像，请不要更改其地址。
- 您必须密切关注用户反馈，并尝试根据用户反馈修改您的代码，以便最终效果符合用户需求。
- 您可以添加js或修改css布局，或添加元素以满足用户反馈。
- 避免将图像用作背景。例如：background: url('https://placehold.co/1600x900')。
- 如果要通过js中的常量添加图像，请模仿以下方式定义常量：
const imageInfo = {{
imgsrc: "https://placehold.co/1600x900",
alt: "这是一个示例图像",
width: 600,
height: 400,
title: "示例图像标题",
}}
也就是说，一定要使用“imgsrc”添加图像地址(使用https://placehold.co中的占位图像)，使用“alt”描述图像内容(图像生成AI稍后可以生成图像)，并根据需要添加其他关键字。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的交互性和功能性。目的是使页面对用户更实用和吸引。
"""

refine_original_output_format_zh = """
第二个页面的代码如下：
HTML代码是：
{html_code}
CSS代码是：
{css_code}

{feedback}

请提供一个修改计划，然后输出第二个页面的修改后的html(包含js代码)，css代码。

输出格式如下：
修改计划：
1.
2.
...

修改后的html:

修改后的css:

"""

refine_Tailwind_output_format_zh = """
第二个页面的代码如下：
使用Tailwind CSS框架的HTML代码是：
{html_code}

{feedback}

请提供一个修改计划，然后输出第二个页面的修改后的html代码。

输出格式如下：
修改计划：
1.
2.
...

修改后的html:
"""

refine_Boostrap_output_format_zh = """
第二个页面的代码如下：
使用Bootstrap CSS框架的HTML代码是：
{html_code}

{feedback}

请提供一个修改计划，然后输出第二个页面的修改后的html代码。

输出格式如下：
修改计划：
1.  
2.
...

修改后的html:
"""

refine_Materialize_output_format_zh = """
第二个页面的代码如下：
使用Materialize CSS框架的HTML代码是：
{html_code}

{feedback}

请提供一个修改计划，然后输出第二个页面的修改后的html代码。

输出格式如下：
修改计划：
1.
2.
...

修改后的html:
"""

refine_Bulma_output_format_zh = """
第二个页面的代码如下：
使用Bulma CSS框架的HTML代码是：
{html_code}

{feedback}

请提供一个修改计划，然后输出第二个页面的修改后的html代码。

输出格式如下：
修改计划：
1.
2.
...

修改后的html:
    
"""



refine_prompt = """
{role}
{task}
{output_format}
"""

# ["Tailwind","Boostrap","Materialize","Bulma",None]
def get_refine_prompt(text = None,img = None,html_code = None,css_code = None,page_info = None,feedback = "",css_frame = None,language = "en"):
    if language == "en":
        feedback = f"The user's feedback is as follows(very important, please pay attention to it!):{feedback}" if feedback else ""
        if css_frame == "Tailwind":
            role = Tailwind_role_en
            output_format = refine_Tailwind_output_format_en.format(html_code = html_code,feedback = feedback)
        elif css_frame == "Boostrap":
            role = Boostrap_role_en
            output_format = refine_Boostrap_output_format_en.format(html_code = html_code,feedback = feedback)
        elif css_frame == "Materialize":
            role = Materialize_role_en
            output_format = refine_Materialize_output_format_en.format(html_code = html_code,feedback = feedback)
        elif css_frame == "Bulma":
            role = Bulma_role_en
            output_format = refine_Bulma_output_format_en.format(html_code = html_code,feedback = feedback)
        else:
            role = original_role_en
            output_format = refine_original_output_format_en.format(html_code = html_code,css_code=css_code,feedback = feedback)
        if feedback:
            task = refine_feedback_task_en.format(page_info = page_info)
        elif img and text:
            task = refine_img_text_task_en.format(page_info = page_info)
        elif img:
            task = refine_img_task_en.format(page_info = page_info)
        else:
            task = refine_text_task_en.format(page_info = page_info)

        prompt = refine_prompt.format(role = role,task = task,output_format = output_format)
        return prompt
    elif language == "zh":
        feedback = f"用户的反馈如下(非常重要，请注意！):{feedback}" if feedback else ""
        if css_frame == "Tailwind":
            role = Tailwind_role_zh
            output_format = refine_Tailwind_output_format_zh.format(html_code = html_code,feedback = feedback)
        elif css_frame == "Boostrap":
            role = Boostrap_role_zh
            output_format = refine_Boostrap_output_format_zh.format(html_code = html_code,feedback = feedback)
        elif css_frame == "Materialize":
            role = Materialize_role_zh
            output_format = refine_Materialize_output_format_zh.format(html_code = html_code,feedback = feedback)
        elif css_frame == "Bulma":
            role = Bulma_role_zh
            output_format = refine_Bulma_output_format_zh.format(html_code = html_code,feedback = feedback)
        else:
            role = original_role_zh
            output_format = refine_original_output_format_zh.format(html_code = html_code,css_code=css_code,feedback = feedback)
        if feedback:
            task = refine_feedback_task_zh.format(page_info = page_info)
        elif img and text:
            task = refine_img_text_task_zh.format(page_info = page_info)
        elif img:
            task = refine_img_task_zh.format(page_info = page_info)
        else:
            task = refine_text_task_zh.format(page_info = page_info)
    
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