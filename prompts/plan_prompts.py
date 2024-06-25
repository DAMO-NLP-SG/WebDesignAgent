original_page_template = """
[
{
"html_name": {HTML name},
"css_name": {css name},
"js_name" : {js name},
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
"is_main_page" : {true or false,true, if the page is the image we provided}
}
...
]
"""

other_page_template = """
[
{
"html_name": {HTML name},
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
"is_main_page" : {true or false,true, if the page is the image we provided}
}
...
]
"""

original_page_example = """
{
    "html_name": "search_results.html",
    "css_name": "search_results.css",
    "js_name": "search_results.js",
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
    "is_main_page": false
    }
"""

other_page_example = """
{
    "html_name": "search_results.html",
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
    "is_main_page": false
    }
"""

plan_output_format_prompt = """
Please make sure all pages can be accessed by buttons or links and all pages can ultimately jump back to the main page.
Please output strictly in the following format(no extra information is allowed):
Designed pages:

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
{page_info}

The output format should be as follows:
modified_page:
{{your modified page}}
"""

page_complete_prompt = """
You are a webpage design master, and your task is to complete and refine an unfinished webpage.

The other page information is as follows:
{other_pages_info}

The current page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

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



def get_plan_prompt(text = None,img = None ,css_frame = None):
    if img and text:
        prompt = f"Your task is to design which pages we should create to design the website for task: {text};The above image is a reference website we have provided to you. "
    elif img:
        prompt = "Your task is to design which pages we should create to design the website based on the website images I provided you."
    else:
        prompt = f"Your task is to design which pages we should create to design the website for task: {text};"
    if not css_frame:
        prompt += plan_output_format_prompt + original_page_template
    else:
        prompt += plan_output_format_prompt + other_page_template
    return prompt

def get_refine_page_prompt(task_info,page_info,css_frame = None):
    if not css_frame:
        page_example = original_page_example
    else:
        page_example = other_page_example
    return refine_page_prompt.format(task_info = task_info,page_info = page_info,page_example = page_example)

if __name__ == "__main__":
    print(get_refine_page_prompt("You are a web design master, and your current task is to modify the details of a website.","2",css_frame = "1"))


