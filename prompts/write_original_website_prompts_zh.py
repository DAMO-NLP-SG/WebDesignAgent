original_role = "您是一位专家级的Html开发者，擅长使用HTML、CSS和JavaScript编写网页。(无需输出js文件，将js文件嵌入到html文件中)"

Tailwind_role = "您是一位专家级的Tailwind开发者，擅长使用Tailwind CSS框架编写网页。"

Boostrap_role = "您是一位专家级的Bootstrap开发者，擅长使用Bootstrap CSS框架编写网页。"

Materialize_role = "您是一位专家级的Materialize开发者，擅长使用Materialize CSS框架编写网页。"

Bulma_role = "您是一位专家级的Bulma开发者，擅长使用Bulma CSS框架编写网页。"

img_task = """
上图是我们提供给您的网页的截图。
页面信息如下:{page_info}(button和link的跳转页面的文件名为其链接地址);
您的任务是根据截图和页面关系构建一个单页面应用。
- 确保您创建的页面与截图完全一致。
- 请注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。确保颜色和大小完全匹配。
- 使用截图中的确切文本。
- 根据需要重复元素以匹配截图。例如，如果有15个项目，则代码应该有15个项目。
- 对于图像，尽量使用页面信息里的本地图片而且不要修改它的文件路径，如果要添加额外图片，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。
- 避免使用图像作为背景。例如: background: url('https://placehold.co/1600x900')。
- 您必须确保您生成的页面与我们提供的页面完全一致(布局、格式、文本、内容)!
- 请你严格关注图片的尺寸问题，确保最后页面的呈现效果美观。
- 鼓励您使用更多js来实现一些操作功能，使页面更加实用和有趣。
"""

text_img_task = """
上图是我们提供给您的参考网页的截图。
页面信息如下:{page_info}(button和link的跳转页面的文件名为其链接地址);
您的任务是根据参考网页的结构和布局以及提供的页面信息构建一个新的网页。
- 不要匹配参考网页上的文本! 根据自己的需要添加文本!
- 不需要与参考网页一致，只需学习其优点。
- 请注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。
- 对于图像，尽量使用页面信息里的本地图片而且不要修改它的文件路径，如果要添加额外图片，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。
- 尽量使页面看起来丰富而不乏味。
- 请你严格关注图片的尺寸问题，确保最后页面的呈现效果美观。
- 应注意协调，例如，技术网站应设计有技术感，而购物网站应具有新鲜感。
- 避免使用图像作为背景。例如: background: url('https://placehold.co/1600x900')。
- 鼓励您使用更多颜色、更多按钮、更精致的布局，并尝试添加更多特效，例如波浪效果、渐变效果、滚动效果等。
- 如果您想通过js中的常量添加图像，请以以下方式定义常量:
const imageInfo = {{
imgsrc: "search.png",
alt: "这是一张参考图片",
width: 600,
height: 400,
title: "参考图片标题",
}}
也就是说，一定要使用"imgsrc"添加图像地址(尽量使用本地地址，否则则使用https://placehold.co中的占位图像)，使用"alt"描述图像内容(图像生成AI稍后可以生成图像)，并根据需要添加其他关键字。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的互动性和功能性。目的是使页面对用户更实用和吸引。
"""

text_task = """
页面信息如下:{page_info}(button和link的跳转页面的文件名为其链接地址);
您的任务是根据页面信息构建一个单页面应用。
- 请注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。
- 对于图像，尽量使用页面信息里的本地图片而且不要修改它的文件路径，如果要添加额外图片，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。
- 尽量使页面看起来丰富而不乏味。
- 应注意协调，例如，技术网站应设计有技术感，而购物网站应具有新鲜感。
- 鼓励您使用更多颜色、更多按钮、更精致的布局，并尝试添加更多特效，例如波浪效果、渐变效果、滚动效果等。
- 请你严格关注图片的尺寸问题，确保最后页面的呈现效果美观。
- 避免使用图像作为背景。例如: background: url('https://placehold.co/1600x900')。
- 如果您想通过js中的常量添加图像，请以以下方式定义常量:
const imageInfo = {{
imgsrc: "search.png",
alt: "这是一张参考图片",
width: 600,
height: 400,
title: "参考图片标题",
}}
也就是说，一定要使用"imgsrc"添加图像地址(尽量使用本地地址，否则则使用https://placehold.co中的占位图像)，使用"alt"描述图像内容(图像生成AI稍后可以生成图像)，并根据需要添加其他关键字。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的互动性和功能性。目的是使页面对用户更实用和吸引。
"""

original_output_format = """
{feedback}

请输出html(包含js代码)，css代码。
"""

Tailwind_output_format = """
{feedback}

现在输出带有Tailwind CSS框架的HTML代码。
"""

Boostrap_output_format = """
{feedback}

现在输出带有Bootstrap CSS框架的HTML代码。
"""

Materialize_output_format = """
{feedback}

现在输出带有Materialize CSS框架的HTML代码。
"""

Bulma_output_format = """
{feedback}

现在输出带有Bulma CSS框架的HTML代码。
"""



write_original_prompt = """
{role}
{task}
{output_format}
"""


