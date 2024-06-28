original_page_template = """
[
{
"html_name": {HTML文件名},
"css_name": {css文件名},
"js_description": {为该页面设计的JavaScript功能},
"description": {页面描述},
"relationship": {
"buttons":[
        {
        "button_name" : {按钮名称},
        "jump_page" : {跳转到的页面名称}
        },
        ...
    ],
"links":[
        {
        "link_name" : {链接名称},
        "jump_page" : {跳转到的页面名称}
        },
        ...
    ]
},
"practice_features": {页面需要具备的实用功能},
"additional_features": {您想要添加到页面的其他功能},
"page_style": {页面风格},
"is_main_page" : {true或false,如果页面是我们提供的图片请设置为true}
}
...
]
"""


original_page_example = """
{
    "html_name": "search_results.html",
    "css_name": "search_results.css",
    "js_description": "基于查询显示搜索结果，并在用户与过滤器和分页交互时动态更新结果。",
    "description": "此页面显示用户查询的搜索结果，根据搜索词提供相关项目的列表。用户可以使用过滤器细化搜索，并浏览多个结果页面。",
    "relationship": {
    "buttons": [
    {"button_name": "按相关性排序", "action": "sortResults('relevance')"},
    {"button_name": "按日期排序", "action": "sortResults('date')"},
    {"button_name": "按热度排序", "action": "sortResults('popularity')"},
    {"button_name": "返回", "jump_page": "previous_page.html"},
    {"button_name": "下一页", "jump_page": "next_page.html"}
    ],
    "links": [
    {"link_name": "主页", "jump_page": "index.html"}
    ]
    },
    "practice_features": "搜索结果显示，分页，交互式排序选项。",
    "additional_features": "搜索结果的过滤器，包括类别，日期范围和价格范围。用户输入时实时搜索建议。",
    "page_style": "简洁现代的设计，注重可用性和可读性。",
    "is_main_page": false
    }
"""

local_img_storage_page_template = """
[
{
"html_name": {HTML文件名},
"css_name": {css文件名},
"js_description": {为该页面设计的JavaScript功能},
"description": {页面描述},
"relationship": {
"buttons":[
        {
        "button_name" : {按钮名称},
        "jump_page" : {跳转到的页面名称}
        },
        ...
    ],
"links":[
        {
        "link_name" : {链接名称},
        "jump_page" : {跳转到的页面名称}
        },
        ...
    ],
"imgs": [
    {
    "src": {图片路径，必须是本地图片},
    "alt": {图片描述},
    "description": {图片在该页面中的作用}
        },
        ...
    ],
},
"practice_features": {页面需要具备的实用功能},
"additional_features": {您想要添加到页面的其他功能},
"page_style": {页面风格},
"is_main_page" : {true或false,如果页面是我们提供的图片请设置为true}
}
...
]
"""

local_img_storage_page_example = """
{
    "html_name": "search_results.html",
    "css_name": "search_results.css",
    "js_description": "基于查询显示搜索结果，并在用户与过滤器和分页交互时动态更新结果。",
    "description": "此页面显示用户查询的搜索结果，根据搜索词提供相关项目的列表。用户可以使用过滤器细化搜索，并浏览多个结果页面。",
    "relationship": {
    "buttons": [
    {"button_name": "按相关性排序", "action": "sortResults('relevance')"},
    {"button_name": "按日期排序", "action": "sortResults('date')"},
    {"button_name": "按热度排序", "action": "sortResults('popularity')"},
    {"button_name": "返回", "jump_page": "previous_page.html"},
    {"button_name": "下一页", "jump_page": "next_page.html"}
    ],
    "links": [
    {"link_name": "主页", "jump_page": "index.html"}
    ]
    },
    "imgs": [
    {
    "src": "search_icon.png",
    "alt": "搜索图标",
    "description": "搜索图标用于用户输入框，表示搜索功能。"
    },
    {
    "src": "filter_icon.png",
    "alt": "过滤器图标",
    "description": "过滤器图标用于筛选搜索结果，用户可以根据类别和价格范围进行过滤。"
    }
    ],
    "practice_features": "搜索结果显示，分页，交互式排序选项。",
    "additional_features": "搜索结果的过滤器，包括类别，日期范围和价格范围。用户输入时实时搜索建议。",
    "page_style": "简洁现代的设计，注重可用性和可读性。",
    "is_main_page": false
    }
"""


plan_output_format_prompt = """
请确保所有页面都可以通过按钮或链接访问，并且所有页面最终都可以跳转回主页。
页面样例如下：
{page_template}

请严格按照以下格式输出(不允许额外信息):
<designed_pages>
{{设计的页面}}
</designed_pages>
"""

plan_output_format_prompt_local_img = """
以下是你可能要用到的本地图片信息（请注意，这些图片可能需要在你的设计中使用，且你需要尽量使用这些图片）：
{local_img_storage}

请确保所有页面都可以通过按钮或链接访问，并且所有页面最终都可以跳转回主页。
页面样例如下：
{page_template}

请严格按照以下格式输出(不允许额外信息):
<designed_pages>
{{设计的页面}}
</designed_pages>
"""

refine_page_prompt = """
你是一个网页设计大师，你当前的任务是修改一个网站的细节。
{task_info}
以下页面是网站的页面之一。请帮我丰富其细节，注意不要改变格式。
修改后的页面应该是dict格式，不要有额外输出(不要添加新的链接到其他页面)。
例如:
{page_example}
您可以通过丰富描述和其他方法(例如，添加布局描述，添加网页效果，添加实用功能，添加按钮等)来丰富页面细节。

页面是:
{page_info}(请注意button和link的跳转页面的文件名是它们的链接地址)

{feedback}

输出格式应该如下:
<modified_page>
{{你修改后的页面}}
</modified_page>
"""

refine_page_local_img_prompt = """
你是一个网页设计大师，你当前的任务是修改一个网站的细节。
{task_info}
以下页面是网站的页面之一。请帮我丰富其细节，注意不要改变格式。
修改后的页面应该是dict格式，不要有额外输出(不要添加新的链接到其他页面)。
例如:
{page_example}
您可以通过丰富描述和其他方法(例如，添加布局描述，添加网页效果，添加实用功能，添加按钮等)来丰富页面细节。

以下是你可能要用到的本地图片信息,如果你需要添加图片，请从以下图片中选择(请根据图片的内容，大小跟描述来选择图片，并决定图片的用途):
{local_img_storage}

页面是:
{page_info}(请注意button和link的跳转页面的文件名是它们的链接地址)

{feedback}

输出格式应该如下:
<modified_page>
{{你修改后的页面}}
</modified_page>
"""

page_complete_prompt = """
你是一个网页设计大师，你的任务是完成和完善一个未完成的网页。

其他页面信息如下:
{other_pages_info}

当前页面信息如下:
{page_info}(请注意button和link的跳转页面的文件名是它们的链接地址)

{feedback}

请根据其他页面的信息和当前页面的已知信息(注意页面之间的跳转关系)，完成和完善此页面的信息，并考虑哪些页面需要设计按钮以跳转到当前页面

你的输出应该是以下格式:
思考步骤:
{{你的思考步骤}}

<completed_page>
{{你完成和完善的页面，不要改变或添加或删除页面的原始键，你可以修改键的值，页面应该是dict格式}}
</completed_page>

<page_relationship>
{{需要设计按钮以跳转到当前页面的页面名称，输出格式应该是一个列表。例如:[{{"html_name":"index.html","button_name":"jump"}},{{"html_name":"home.html","button_name":"jump"}}]}}
</page_relationship>

"""

page_complete_prompt_local_img = """
你是一个网页设计大师，你的任务是完成和完善一个未完成的网页。

其他页面信息如下:
{other_pages_info}

当前页面信息如下:
{page_info}(请注意button和link的跳转页面的文件名是它们的链接地址)

{feedback}

以下是你可能要用到的本地图片信息（请注意，这些图片可能需要在你的设计中使用，且你需要尽量使用这些图片）：
{local_img_storage}

请根据其他页面的信息和当前页面的已知信息(注意页面之间的跳转关系)，完成和完善此页面的信息，并考虑哪些页面需要设计按钮以跳转到当前页面

你的输出应该是以下格式:
思考步骤:
{{你的思考步骤}}

<completed_page>
{{你完成和完善的页面，不要改变或添加或删除页面的原始键，你可以修改键的值，页面应该是dict格式}}
</completed_page>

<page_relationship>
{{需要设计按钮以跳转到当前页面的页面名称，输出格式应该是一个列表。例如:[{{"html_name":"index.html","button_name":"jump"}},{{"html_name":"home.html","button_name":"jump"}}]}}
</page_relationship>
"""

if __name__ == "__main__":
    import json
    print(json.loads(local_img_storage_page_example))