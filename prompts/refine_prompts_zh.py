original_role  = "您是一位专家级的Html开发者，擅长使用HTML、CSS、JavaScript编写网页。(无需输出js文件，将js文件嵌入到html文件中即可)"

Tailwind_role  = "您是一位专家级的Tailwind开发者，擅长使用Tailwind CSS框架编写网页。"

Boostrap_role  = "您是一位专家级的Bootstrap开发者，擅长使用Bootstrap CSS框架编写网页。"

Materialize_role = "您是一位专家级的Materialize开发者，擅长使用Materialize CSS框架编写网页。"

Bulma_role = "您是一位专家级的Bulma开发者，擅长使用Bulma CSS框架编写网页。"

refine_img_task = """
第一张图片是我们的目标网页的截图，第二张图片是您已经构建的网页截图。
{local_img_storage}
页面信息如下：
{page_info}(button和link的跳转页面的文件名为其链接地址)

您的目标是修改第二个网页的代码，使其更新为更像目标页面(第一张图片)的样子。

- 确保您创建的页面与截图完全相同。
- 注意页面的布局，图片分布，图片大小，相关文本，按钮，链接等要与截图完全一致。
- 注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。完全匹配颜色和大小要与截图完全一致。
- 使用截图中的确切文本，不要更改文本
- 避免将placehold用作背景。例如：background: url('https://placehold.co/1600x900'),你可以使用渐变的颜色作为背景或者本地图片作为背景。
- 对于图像，尽量使用页面信息里的本地图片而且不要修改它的文件路径，如果要添加额外图片，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。对于已经存在的图像，请不要修改其文件路径。
- 请你严格关注图片的尺寸问题，确保最后页面的呈现效果美观。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的互动性和功能性（例如：滚动、点击、悬停，颜色变化，点击特效，页面切换等）。目的是使页面对用户更实用和吸引。
"""

refine_img_text_task = """
第一张图片是参考网页的截图，第二张图片是您已经构建的网页截图。
{local_img_storage}
页面信息如下：
{page_info}(button和link的跳转页面的文件名为其链接地址)

您的目标是修改第二个图片的网页代码，模仿第一个图片的布局结构，并满足页面信息要求。
- 不要匹配参考网页上的文本！根据自己的需要添加文本！
- 不需要与参考网页一致，只需从其优点中学习。
- 您可以添加js或修改css布局，或添加元素以满足用户反馈。
- 注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。
- 尽量使页面看起来丰富而不乏味，比如说用丰富的背景色，按钮颜色，字体颜色等。
- 注意协调，例如，技术网站应设计具有技术感，而购物网站应具有新鲜感。
- 请你严格关注图片的尺寸问题，确保最后页面的呈现效果美观。
- 对于图像，尽量使用页面信息里的本地图片而且不要修改它的文件路径，如果要添加额外图片，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。对于已经存在的图像，请不要修改其文件路径。
- 注意，不要让图片遮挡住文字，文字的图层应该是最顶层的。
- 鼓励您使用更多的颜色、更多的按钮、更精致的布局，更多的图片，并尝试添加更多的特效，例如波浪效果、渐变效果、滚动效果等。
- 避免将placehold用作背景。例如：background: url('https://placehold.co/1600x900'),你可以使用渐变的颜色作为背景或者本地图片作为背景。
- 增强功能性和实用性：思考如何通过修改代码来提高页面的功能性和实用性。
- 请分析当前页面的页眉、导航、内容排列、侧边栏、页脚、视觉元素、布局、行动号召、响应性和其他功能，并分析如何优化这些功能，使布局更美观和和谐。
- 请思考如何修改代码以使页面满足我们的需求(例如添加图像、添加按钮、增加动画效果或添加一些文本内容、详细内容等)。
- 如果您想通过js中的常量添加图像，请以以下方式定义常量:
const imageInfo = {{
imgsrc: "search.png",
alt: "这是一张参考图片",
width: 600,
height: 400,
title: "参考图片标题",
}}
也就是说，一定要使用"imgsrc"添加图像地址(尽量使用本地地址，否则则使用https://placehold.co中的占位图像)，使用"alt"描述图像内容(图像生成AI稍后可以生成图像)，并根据需要添加其他关键字。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的互动性和功能性（例如：滚动、点击、悬停，颜色变化，点击特效，页面切换等）。目的是使页面对用户更实用和吸引。
"""

refine_text_task = """
{local_img_storage}
页面信息如下：{page_info}(button和link的跳转页面的文件名为其链接地址);

您的任务是根据用户反馈修改代码，以满足用户需求。
- 对于图像，尽量使用页面信息里的本地图片而且不要修改它的文件路径，如果要添加额外图片，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。对于已经存在的图像，请不要修改其文件路径。
- 您可以添加js或修改css布局，或添加元素以满足用户反馈。
- 注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。
- 尽量使页面看起来丰富而不乏味，比如说用丰富的背景色，按钮颜色，字体颜色等。
- 注意协调，例如，技术网站应设计具有技术感，而购物网站应具有新鲜感。
- 请你严格关注图片的尺寸问题，确保最后页面的呈现效果美观。
- 对于图像，尽量使用页面信息里的本地图片而且不要修改它的文件路径，如果要添加额外图片，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。对于已经存在的图像，请不要修改其文件路径。
- 注意，不要让图片遮挡住文字，文字的图层应该是最顶层的。
- 鼓励您使用更多的颜色、更多的按钮、更精致的布局，更多的图片，并尝试添加更多的特效，例如波浪效果、渐变效果、滚动效果等。
- 避免将placehold用作背景。例如：background: url('https://placehold.co/1600x900'),你可以使用渐变的颜色作为背景或者本地图片作为背景。
- 增强功能性和实用性：思考如何通过修改代码来提高页面的功能性和实用性。
- 请分析当前页面的页眉、导航、内容排列、侧边栏、页脚、视觉元素、布局、行动号召、响应性和其他功能，并分析如何优化这些功能，使布局更美观和和谐。
- 请思考如何修改代码以使页面满足我们的需求(例如添加图像、添加按钮、增加动画效果或添加一些文本内容、详细内容等)。
- 如果您想通过js中的常量添加图像，请以以下方式定义常量:
const imageInfo = {{
imgsrc: "search.png",
alt: "这是一张参考图片",
width: 600,
height: 400,
title: "参考图片标题",
}}
也就是说，一定要使用"imgsrc"添加图像地址(尽量使用本地地址，否则则使用https://placehold.co中的占位图像)，使用"alt"描述图像内容(图像生成AI稍后可以生成图像)，并根据需要添加其他关键字。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的互动性和功能性（例如：滚动、点击、悬停，颜色变化，点击特效，页面切换等）。目的是使页面对用户更实用和吸引。
"""

refine_feedback_task = """
{local_img_storage}
页面信息如下：{page_info}(button和link的跳转页面的文件名为其链接地址);

您的任务是根据用户反馈修改代码，以满足用户需求。
- 您必须密切关注用户反馈，并尝试根据用户反馈修改您的代码，以便最终效果符合用户需求。
- 您可以添加js或修改css布局，或添加元素以满足用户反馈。
- 注意背景颜色、文字颜色、字体大小、字体系列、内边距、外边距、边框等。
- 尽量使页面看起来丰富而不乏味，比如说用丰富的背景色，按钮颜色，字体颜色等。
- 注意协调，例如，技术网站应设计具有技术感，而购物网站应具有新鲜感。
- 请你严格关注图片的尺寸问题，确保最后页面的呈现效果美观。
- 对于图像，尽量使用页面信息里的本地图片而且不要修改它的文件路径，如果要添加额外图片，请使用https://placehold.co中的占位图像，并在alt文本中包含图像的详细描述，以便图像生成AI稍后生成图像。对于已经存在的图像，请不要修改其文件路径。
- 注意，不要让图片遮挡住文字，文字的图层应该是最顶层的。
- 鼓励您使用更多的颜色、更多的按钮、更精致的布局，更多的图片，并尝试添加更多的特效，例如波浪效果、渐变效果、滚动效果等。
- 避免将placehold用作背景。例如：background: url('https://placehold.co/1600x900'),你可以使用渐变的颜色作为背景或者本地图片作为背景。
- 增强功能性和实用性：思考如何通过修改代码来提高页面的功能性和实用性。
- 请分析当前页面的页眉、导航、内容排列、侧边栏、页脚、视觉元素、布局、行动号召、响应性和其他功能，并分析如何优化这些功能，使布局更美观和和谐。
- 请思考如何修改代码以使页面满足我们的需求(例如添加图像、添加按钮、增加动画效果或添加一些文本内容、详细内容等)。
- 如果您想通过js中的常量添加图像，请以以下方式定义常量:
const imageInfo = {{
imgsrc: "search.png",
alt: "这是一张参考图片",
width: 600,
height: 400,
title: "参考图片标题",
}}
也就是说，一定要使用"imgsrc"添加图像地址(尽量使用本地地址，否则则使用https://placehold.co中的占位图像)，使用"alt"描述图像内容(图像生成AI稍后可以生成图像)，并根据需要添加其他关键字。
- 鼓励您通过实现额外的JavaScript操作功能来增强网页的互动性和功能性（例如：滚动、点击、悬停，颜色变化，点击特效，页面切换等）。目的是使页面对用户更实用和吸引。
"""

refine_original_output_format = """
目前的页面的代码如下：
HTML代码是：
{html_code}
CSS代码是：
{css_code}

{feedback}

请提供一个修改计划，然后输出第二个页面的修改后的html(包含js代码)，css代码。

输出格式如下：
当前网页不足之处：  
1.
2.

修改计划：
1.
2.
...

修改后的html:

修改后的css:

"""

refine_Tailwind_output_format = """
目前的页面的代码如下：
使用Tailwind CSS框架的HTML代码是：
{html_code}

{feedback}

请提供一个修改计划，然后输出第二个页面的修改后的html代码。

输出格式如下：
当前网页不足之处：  
1.
2.

修改计划：
1.
2.
...

修改后的html:
"""

refine_Boostrap_output_format = """
目前的页面的代码如下：
使用Bootstrap CSS框架的HTML代码是：
{html_code}

{feedback}

请提供一个修改计划，然后输出第二个页面的修改后的html代码。

输出格式如下：
当前网页不足之处：  
1.
2.

修改计划：
1.  
2.
...

修改后的html:
"""

refine_Materialize_output_format = """
目前的页面的代码如下：
使用Materialize CSS框架的HTML代码是：
{html_code}

{feedback}

请提供一个修改计划，然后输出第二个页面的修改后的html代码。

输出格式如下：
当前网页不足之处：  
1.
2.

修改计划：
1.
2.
...

修改后的html:
"""

refine_Bulma_output_format = """
目前的页面的代码如下：
使用Bulma CSS框架的HTML代码是：
{html_code}

{feedback}

请提供一个修改计划，然后输出第二个页面的修改后的html代码。

输出格式如下：
当前网页不足之处：  
1.
2.

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

