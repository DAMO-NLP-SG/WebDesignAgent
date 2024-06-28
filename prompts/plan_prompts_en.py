original_page_template = """
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


original_page_example = """
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
    "page_style": "Simple and modern design with rich background colors, emphasizing usability and readability.",
    "is_main_page": false
    }
"""
local_img_storage_page_template = """
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
"imgs": [
    {
    "src": {The path of the image, must be a local image},
    "alt": {The alternative text of the image},
    "description": {The role of the image on this page}
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

local_img_storage_page_example = """
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
],
"imgs": [
{
"src": "search_icon.png",
"alt": "Search icon",
"description": "The search icon is used in the user input box to indicate the search function."
},
{
"src": "filter_icon.png",
"alt": "Filter icon",
"description": "The filter icon is used to filter search results. Users can filter by category and price range."
}
]
},
"practice_features": "Search result display, pagination, interactive sorting options.",
"additional_features": "Filters for search results including categories, date range, and price range. Real-time search suggestions as the user types.",
"page_style": "Clean and modern design with a focus on usability and readability.",
"is_main_page": false
}
"""



plan_output_format_prompt = """
Please make sure all pages can be accessed by buttons or links and all pages can ultimately jump back to the main page.
Here is an example of the page format:
{page_template}

Please output strictly in the following format(no extra information is allowed):
<designed_pages>
{{The pages you designed}}
</designed_pages>
"""

plan_output_format_prompt_local_img = """
Here is the local image information you may need to use (please note that these images may need to be used in your design, and you should try to use these images as much as possible,You also need to consider the size of the image):
{local_img_storage}

Please make sure all pages can be accessed by buttons or links and all pages can ultimately jump back to the main page.
Here is an example of the page format:
{page_template}

Please output strictly in the following format(no extra information is allowed):
<designed_pages>
{{The pages you designed}}
</designed_pages>
"""


refine_page_prompt = """
You are a web design master, and your current task is to modify the details of a website.
{task_info}
The following page is one of the pages of the  website. Please help me enrich its details and be careful not to change the format.
The modified page should be dict format and no extra output(Do not add new links to other page).
For example:
{page_example}
You can enrich the page details by enriching the description and other methods(For example, adding descriptions of layout, adding web page effects, adding practical features, adding buttons and so on)).

The page is:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses and do not change the html_name)

{feedback}
The output format should be as follows:
<modified_page>
{{your modified page}}
</modified_page>
"""

refine_page_local_img_prompt = """
You are a web design master, and your current task is to modify the details of a website.
{task_info}
The following page is one of the pages of the  website. Please help me enrich its details and be careful not to change the format.
The modified page should be dict format and no extra output(Do not add new links to other page).
For example:
{page_example}
You can enrich the page details by enriching the description and other methods(For example, adding descriptions of layout, adding web page effects, adding practical features, adding buttons and so on)).

The following are local image information that you may need. If you need to add an image, please select from the following images:
{local_img_storage}

The page is:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses and do not change the html_name)

{feedback}

The output format should be as follows:
<modified_page>
{{Your modified page}}
</modified_page>
"""

page_complete_prompt = """
You are a webpage design master, and your task is to complete and refine an unfinished webpage.
{task_info}
The other page information is as follows:
{other_pages_info}

The current page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses and do not change the html_name)

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

page_complete_prompt_local_img = """
You are a webpage design master, and your task is to complete and refine an unfinished webpage.
{task_info}
The other page information is as follows:
{other_pages_info}

The current page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses and do not change the html_name)

{feedback}

Please complete and refine the information on this page based on the information on other pages and the known information on the current page (pay attention to the jump relationship between pages), and consider which pages need to be designed with buttons to jump to the current page

The following are local image information that you may need. If you need to add an image, please select from the following images(Please select images based on their content, size and description, and decide the purpose of the images.):
{local_img_storage}

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


if __name__ == "__main__":
    import json
    print(json.loads(local_img_storage_page_example))