original_page_template_en = """
[
{
"html_name": {HTML name},
"css_name": {css name},
"js_description": {What JavaScript features need to be designed for this page},
"description": {Description of the page},
"relationship": {
"buttons":[
        {
        "button_name" : {The name of the button},
        "jump_page" : {The name of the page to jump to}
        },
        ...
    ],
"links":[
        {
        "link_name" : {The name of the link},
        "jump_page" : {The name of the page to jump to}
        },
        ...
    ]
},
"practice_features": {practical features that page need to have},
"additional_features": {additional features you want to add to the page},
"page_style": {The style of the page},
"is_main_page" : {true or false,true, if the page is the image we provided}
}
...
]
"""

other_page_template_en = """
[
{
"html_name": {HTML name},
"js_description": {What JavaScript features need to be designed for this page},
"description": {Description of the page},
"relationship": {
"buttons":[
        {
        "button_name" : {The name of the button},
        "jump_page" : {The name of the page to jump to}
        },
        ...
    ],
"links":[
        {
        "link_name" : {The name of the link},
        "jump_page" : {The name of the page to jump to}
        },
        ...
    ]
},
"practice_features": {practical features that page need to have},
"additional_features": {additional features you want to add to the page},
"page_style": {The style of the page},
"is_main_page" : {true or false,true, if the page is the image we provided}
}
...
]
"""

original_page_example_en = """
{
    "html_name": "search_results.html",
    "css_name": "search_results.css",
    "js_description": "Display search results based on the query and dynamically update the results as the user interacts with filters and pagination.",
    "description": "This page shows the search results for the user's query, providing a list of relevant items based on the search term. Users can refine their search using filters and navigate through multiple pages of results.",
    "relationship": {
    "buttons": [
    {"button_name": "Sort by Relevance", "action": "sortResults('relevance')"},
    {"button_name": "Sort by Date", "action": "sortResults('date')"},
    {"button_name": "Sort by Popularity", "action": "sortResults('popularity')"},
    {"button_name": "Back", "jump_page": "previous_page.html"},
    {"button_name": "Next", "jump_page": "next_page.html"}
    ],
    "links": [
    {"link_name": "Main Page", "jump_page": "index.html"}
    ]
    },
    "practice_features": "Search result display, pagination, interactive sorting options.",
    "additional_features": "Filters for search results including categories, date range, and price range. Real-time search suggestions as the user types.",
    "page_style": "Clean and modern design with a focus on usability and readability.",
    "is_main_page": false
    }
"""

other_page_example_en = """
{
    "html_name": "search_results.html",
    "js_description": "Display search results based on the query and dynamically update the results as the user interacts with filters and pagination.",
    "description": "This page shows the search results for the user's query, providing a list of relevant items based on the search term. Users can refine their search using filters and navigate through multiple pages of results.",
    "relationship": {
    "buttons": [
    {"button_name": "Sort by Relevance", "action": "sortResults('relevance')"},
    {"button_name": "Sort by Date", "action": "sortResults('date')"},
    {"button_name": "Sort by Popularity", "action": "sortResults('popularity')"},
    {"button_name": "Back", "jump_page": "previous_page.html"},
    {"button_name": "Next", "jump_page": "next_page.html"}
    ],
    "links": [
    {"link_name": "Main Page", "jump_page": "index.html"}
    ]
    },
    "practice_features": "Search result display, pagination, interactive sorting options.",
    "additional_features": "Filters for search results including categories, date range, and price range. Real-time search suggestions as the user types.",
    "page_style": "Clean and modern design with a focus on usability and readability.",
    "is_main_page": false
    }
"""

plan_output_format_prompt_en = """
Please make sure all pages can be accessed by buttons or links and all pages can ultimately jump back to the main page.
Please output strictly in the following format(no extra information is allowed):
<designed_pages>
{{The pages you designed}}
</designed_pages>

"""

refine_page_prompt_en = """
You are a web design master, and your current task is to modify the details of a website.
{task_info}
The following page is one of the pages of the  website. Please help me enrich its details and be careful not to change the format.
The modified page should be dict format and no extra output(Do not add new links to other page).
For example:
{page_example}
You can enrich the page details by enriching the description and other methods(For example, adding descriptions of layout, adding web page effects, adding practical features, adding buttons and so on)).

The page is:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

{feedback}
The output format should be as follows:
<modified_page>
{{your modified page}}
</modified_page>
"""

page_complete_prompt_en = """
You are a webpage design master, and your task is to complete and refine an unfinished webpage.

The other page information is as follows:
{other_pages_info}

The current page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

{feedback}

Please complete and refine the information on this page based on the information on other pages and the known information on the current page (pay attention to the jump relationship between pages), and consider which pages need to be designed with buttons to jump to the current page

Your output should be in the following format:
Thinking steps:
{{Your thinking steps}}

<completed_page>
{{Your completed and refined page, do not change or add or delete the original key of the page, you can modify the value of the key, and the page should be dict format}}
</completed_page>

<page_relationship>
{{The name of pages that need to be designed with buttons to jump to the current page and the output format should be a list. For example:[{{"html_name":"index.html","button_name":"jump"}},{{"html_name":"home.html","button_name":"jump"}}]}}
</page_relationship>
"""

original_page_template_zh = """
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

other_page_template_zh = """
[
{
"html_name": {HTML文件名},
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

original_page_example_zh = """
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

other_page_example_zh = """
{
    "html_name": "search_results.html",
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

plan_output_format_prompt_zh = """
请确保所有页面都可以通过按钮或链接访问，并且所有页面最终都可以跳转回主页。
请严格按照以下格式输出(不允许额外信息):
<designed_pages>
{{设计的页面}}
</designed_pages>
"""

refine_page_prompt_zh = """
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

page_complete_prompt_zh = """
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




def get_plan_prompt(text = None,img = None ,css_frame = None,feedback = "",language = "en"):
    if language == "en":
        if img and text:
            prompt = f"Your task is to design which pages we should create to design the website for task: {text};The above image is a reference website we have provided to you. Instead of designing the website according to the above image, you need to imitate the image and then design a new website based on your task."
        elif img:
            prompt = "Your task is to design which pages we should create to design the website based on the website images I provided you."
        else:
            prompt = f"Your task is to design which pages we should create to design the website for task: {text};"
        feedback = f"The user's requirements on the website(Very important! You must pay extra attention to the content here and meet user's needs) is : {feedback}" if feedback else ""
        if not css_frame:
            prompt += plan_output_format_prompt_en + original_page_template_en
        else:
            prompt += plan_output_format_prompt_en + other_page_template_en
        return prompt
    elif language == "zh":
        if img and text:
            prompt = f"你的任务是确定我们需要创建哪些页面来设计该任务的网站：{text};上方的图片是我们提供的参考网站。你需要根据该图片进行模仿，但不是完全照搬，而是根据你需要完成的任务设计一个全新的网站。"
        elif img:
            prompt = "你的任务是确定我们需要创建哪些页面来设计基于我提供的网站图片的网站。(需要完全根据图片设计，尽量做到一致)"
        else:
            prompt = f"你的任务是确定我们需要创建哪些页面来设计该任务的网站：{text};"
        feedback = f"用户对网站的需求(非常重要！你必须特别注意这里的内容，并满足用户的需求)是：{feedback}" if feedback else ""
        if not css_frame:
            prompt += plan_output_format_prompt_zh + original_page_template_zh
        else:
            prompt += plan_output_format_prompt_zh + other_page_template_zh
        return prompt


def get_refine_page_prompt(task,page_info,css_frame = None,feedback = "",language = "en"):
    if language == "en":
        task_info = f"The requirements of the website is {task}" if task else ""
        feedback = f"The user feedback on the webpage(Very important! You must pay extra attention to the content here and prioritize making modifications to it) is : {feedback}" if feedback else ""
        if not css_frame:
            page_example = original_page_example_en
        else:
            page_example = other_page_example_en
        return refine_page_prompt_en.format(task_info = task_info,page_info = page_info,page_example = page_example,feedback = feedback)
    elif language == "zh":
        task_info = f"网站的需求是{task}" if task else ""
        feedback = f"用户对网页的反馈(非常重要！你必须特别注意这里的内容，并优先进行修改)是：{feedback}" if feedback else ""
        if not css_frame:
            page_example = original_page_example_zh
        else:
            page_example = other_page_example_zh
        return refine_page_prompt_zh.format(task_info = task_info,page_info = page_info,page_example = page_example,feedback = feedback)

def get_page_complete_prompt(other_pages_info,page_info,feedback = "" ,language = "en"):
    if language == "en":
        feedback = f"The user feedback on how to complete the webpage(Very important! You must pay extra attention to the content here and prioritize making modifications to it) is : {feedback}" if feedback else ""
        return page_complete_prompt_en.format(other_pages_info = other_pages_info,page_info = page_info,feedback = feedback)
    elif language == "zh":
        feedback = f"用户对如何完成网页的反馈(非常重要！你必须特别注意这里的内容，并优先进行修改)是：{feedback}" if feedback else ""
        return page_complete_prompt_zh.format(other_pages_info = other_pages_info,page_info = page_info,feedback = feedback)

if __name__ == "__main__":
    print(get_refine_page_prompt("You are a web design master, and your current task is to modify the details of a website.","2",css_frame = "1"))


