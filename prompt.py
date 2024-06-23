plan_output_format_prompt = """
Please make sure all pages can be accessed by buttons or links and all pages can ultimately jump back to the main page.
Output your thinking steps firstly and then output the designed pages.
Please output strictly in the following format(no extra information is allowed):
Thinking steps:

Designed pages:
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
    ]
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

refine_page_prompt = """
You are a web design master, and your current task is to modify the details of a website.
{task_info}
The following page is one of the pages of the  website. Please help me enrich its details and be careful not to change the format.
The modified page should be dict format and no extra output(Do not add new links to other page).
For example:{{
    "html_name": "search_results.html",
    "css_name": "search_results.css",
    "js_name": "search_results.js",
    "js_description": "Display search results based on the query and dynamically update the results as the user interacts with filters and pagination.",
    "description": "This page shows the search results for the user's query, providing a list of relevant items based on the search term. Users can refine their search using filters and navigate through multiple pages of results.",
    "relationship": {{
    "buttons": [
    {{"button_name": "Sort by Relevance", "action": "sortResults('relevance')"}},
    {{"button_name": "Sort by Date", "action": "sortResults('date')"}},
    {{"button_name": "Sort by Popularity", "action": "sortResults('popularity')"}},
    {{"button_name": "Back", "jump_page": "previous_page.html"}},
    {{"button_name": "Next", "jump_page": "next_page.html"}}
    ],
    "links": [
    {{"link_name": "Main Page", "jump_page": "index.html"}}
    ]
    }},
    "practice_features": "Search result display, pagination, interactive sorting options.",
    "additional_features": "Filters for search results including categories, date range, and price range. Real-time search suggestions as the user types.",
    "is_main_page": false
    }}
You can enrich the page details by enriching the description and other methods(For example, adding descriptions of layout, adding web page effects, adding practical features, adding buttons and so on)).

The page is:
{page_info}
please output your thinking steps firstly and then output the modified page.
The output format should be as follows:
Thinking steps:
{{your thinking steps}}

modified_page:s
{{your modified page}}
"""

page_complete_prompt = """
You are a webpage design master, and your task is to complete and refine a unfinished webpage.

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


write_original_website_img_text_prompt =  """
Your goal is to design a page for task: {text};
The above image is a reference page we have provided to you. You need to build the target page according to the layout format of the page.
Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.
3.If you want to add images through JavaScript, please define img as the following format: {{imgSrc: "product1. jpg", description: 'Description for product 1, such as a black phone',... }}.If there is no specific explanation in the img, you can fabricate it according to your needs.
4.Encourage you to use more colors(Must match the theme of the page and not be too abrupt), more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
5.Try to make the page appear rich and not boring. 
6.Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.


The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Please first state your plan and how you will complete this task step by step and then output the html, css and js code.
    """

write_original_website_img_prompt = """
You are a web code master, and your task is to write HTML, CSS, and JavaScript code to reproduce the above web page images I provided you with.
Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.
3.If you want to add images through JavaScript, please define img as the following format: {{imgSrc: "product1. jpg", description: 'Description for product 1, such as a black phone',... }}.If there is no specific explanation in the img, you can fabricate it according to your needs.

The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

You must ensure that the page you generate is completely consistent with the page we provide(Layout, Format, Text, Content)!
Please output the html, css and js code.
"""

write_original_website_text_prompt = """
Your task is to design a page for task: {text};
Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.
3.If you want to add images through JavaScript, please define img as the following format: {{imgSrc: "product1. jpg", description: 'Description for product 1',... }}.If there is no specific explanation in the img, you can fabricate it according to your needs.
4.Encourage you to use more colors, more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. At the same time, try to make the page appear rich and not boring. At the same time, attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.

The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Please first state your plan and how you will complete this task step by step and then output the html, css and js code."""

write_original_website_prompt = """
Your task is to design a page for a website.
Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.
3.If you want to add images through JavaScript, please define img as the following format: {{imgSrc: "product1. jpg", description: 'Description for product 1',... }}.If there is no specific explanation in the img, you can fabricate it according to your needs.
4.Encourage you to use more colors(Must match the theme of the page and not be too abrupt), more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
5.Try to make the page appear rich and not boring. 
6.Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.


The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Please first state your plan and how you will complete this task step by step and then output the html, css and js code.
"""


refine_img_text_prompt = """
You are a web design master, and your goal is to modify the HTML, CSS and js code to meet my needs.
The page requirement: {text};

The first page is a reference page we have provided to you, You need to refer to his content layout and layout format to build a new webpage. The current HTML code website is the second website. 

Please analyze which excellent aspects the second webpage can learn from the first webpage to improve oneself and think how to improve the code to refine the second page.

Here are some precautions:
1. Strict Control of Image Sizes: Ensure that the size of <img> elements is strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. The image size should be reasonable and not too large.
2. Image Description Field: Add a description field to briefly explain the content of the image. For example: <img src="demo banner 1.jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">
3. JavaScript Image Definition: If adding images through JavaScript, define the image object in the following format: {{imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone', ... }}.If there is no specific explanation in the image object, you can fabricate it according to your needs.
4. Page Layout and Aesthetics: Pay strict attention to the page layout to maintain aesthetics and symmetry. Control the relative size of images via CSS to ensure a reasonable and consistent layout.
5. Enhanced Functionality and Practicality: Think about how to improve the functionality and practicality of the page by modifying the code.
6. Visual Appeal and Richness: Use more colors (matching the theme of the page and not too abrupt), more buttons, and a more exquisite layout. Try adding special effects such as wave effects, gradient effects, and scrolling effects to make the page appear rich and not boring.
7. Coordination with Theme: Ensure coordination with the theme of the website. For example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.
8. Page Layout Analysis: Analyze the page layout patterns of the first and the second pages, comparing differences in header, navigation, content arrangement, sidebars, footers, visual elements, typography, calls to action, responsiveness, and additional features. Ensure each block is located in the same layout position where applicable.
9. Block Structure Consistency: Pay special attention to the block structure of page layouts. Analyze and compare the block structure of the first page with that of the second page, ensuring the block structures are consistent.


The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Please think about how to modify the code to make the page meet our needs (such as adding images, adding buttons, increasing animation effectsincreasing animation effects or add some text content, detailed content etc.).

The code of second page are as follows:
The HTML code is: 
{html_code}
The CSS code is: 
{css_code}
The js code is: 
{js_code}

{feedback}
Please provide a modification plan and then output the modified html, css and js code of second page.
The output format is as follows:
Modify plan:
1.
2.
...

modified html:

modified css:

modified js:

            """

refine_img_prompt = """
You are a web design master, and your goal is to modify the HTML, CSS and js code to meet my needs.
The first image is the page we expected, and the second image is the result of our current code implementation. Our goal is to generate an effect that is exactly the same as the first image(at least consistent layout). Please analyze how to improve the code to make the effect consistent with the first image.
Here are some precautions:
1. Strict Control of Image Size with CSS: Ensure that the size of IMG elements is controlled using CSS to avoid layout changes caused by inconsistent image sizes. The image size should be reasonable and not too large to maintain a more balanced layout.
2. Description Field for Images: Each image must include a description field to briefly explain its content. For example: <img src="demo_banner1.jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">. If there isn't a specific explanation provided, you can create one according to your needs.
3. Adding Images via JavaScript: If you need to add images through JavaScript, define the img object in the following format: {{imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone'}}. Create descriptions if they are not specified.

The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Please think about how to modify the code to make the page more consistent with the target page(Require complete consistency, at least consistent layout).
The code of second page are as follows:
The HTML code is: 
{html_code}
The CSS code is:
{css_code}
The js code is: 
{js_code}

{feedback}
Please list the differences and provide a modification plan and then output the modified html, css and js code.
The output format is as follows:
Difference:
1.
2.
...
Modify plan:
1.
2.
...
modified html:

modified css:

modified js:
"""

refine_text_prompt = """
You are a web design master, and your goal is to modify the HTML, CSS and js code to meet my needs.
The page requirement: {text};
The current HTML code page effect is above(The above img)).
Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. Control the relative size of IMG (the image size should be reasonable and not too large) to make the layout more reasonable.
2.You must add a description field to briefly explain the content of the image. For example: <img src="demo banner 1.jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">. If there is no specific explanation in the img, you can fabricate it according to your needs.
3.If you want to add images through JavaScript, please define img as the following format: {{imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone',... }}.
4.You need to pay strict attention to the page layout, maintain aesthetics, and try to have a sense of symmetry.
5.Please analyze the current page's header, navigation, content arrangement, sidebars, footers, visual elements, layout, call to action, responsiveness, and any other features, and analyze how to optimize these to make the layout more beautiful and harmonious.
6.Encourage you to use more colors (must match the theme of the page and not be too abrupt), more buttons, and more exquisite layout. Try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on.
7.Try to make the page appear rich and not boring.
8.Attention should be paid to coordination; for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.

The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Please think about the strawback of current page and how to modify the code to make the page meet our needs (such as adding images, adding buttons, increasing animation effectsincreasing animation effects or add some text content, detailed content etc.).

The code of the page are as follows:
The HTML code is: 
{html_code}
The CSS code is: 
{css_code}
The js code is: 
{js_code}

{feedback}
Please list the strawbacks of current page and provide a modification plan and then output the modified html, css and js code.
The output format is as follows:
The strawback of current page:
1.
2.
...

Modify plan:
1.
2.
...

modified html:

modified css:

modified js:

"""

refine_raw_prompt = """
You are a web design master, and your goal is to modify the HTML, CSS and js code to meet my needs.
The current HTML code page effect is above(The above img)).
Here are some precautions:
1. Size Control and Aesthetics of Images:The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. Ensure that the image size is reasonable and not too large to maintain a harmonious layout.
Control the relative size of IMG to make the layout more aesthetically pleasing and balanced.
2. Image Descriptions and Addition Through JavaScript:You must add a description field to briefly explain the content of the image. For example: <img src="demo banner 1.jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">. If there is no specific description provided, feel free to fabricate one according to your needs.
If you want to add images through JavaScript, define the img object in the following format: {{imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone',... }}.
3. Page Layout and Aesthetics:Pay strict attention to the page layout to maintain aesthetics and achieve a sense of symmetry.
Analyze the current page's header, navigation, content arrangement, sidebars, footers, visual elements, layout, call to action, responsiveness, and any other features. Optimize these elements to create a more beautiful and harmonious layout.
4. Use of Colors, Buttons, and Effects: Encourage the use of more colors, ensuring they match the theme of the page and are not too abrupt.
Incorporate more buttons and an exquisite layout. Add special effects such as wave effects, gradient effects, scrolling effects, and others to enhance the visual appeal.
5. Richness and Practicality: Strive to make the page appear rich and engaging, avoiding a monotonous look. Think extra about how to improve the functionality and practicality of the page by modifying the code accordingly.
6. Coordination and Thematic Design: Pay attention to overall coordination; for example, technology websites should be imbued with a sense of technological sophistication, whereas shopping websites should convey a sense of freshness and appeal.

The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Please think about the strawback of current page and how to modify the code to make the page meet our needs (such as adding images, adding buttons, increasing animation effectsincreasing animation effects or add some text content, detailed content etc.).

The code of the page are as follows:
The HTML code is: 
{html_code}
The CSS code is: 
{css_code}
The js code is: 
{js_code}

{feedback}
Please list the strawbacks of current page and provide a modification plan and then output the modified html, css and js code.
The output format is as follows:
The strawback of current page:
1.
2.
...

Modify plan:
1.
2.
...

modified html:

modified css:

modified js:

"""

refine_augument_img_prompt = """
You are a web design master. The first image is the desired web page rendering, and the second image is the current actual web page rendering. Your task is to modify the code of the second web page to make it consistent with the first one.

The page information is as follows: {page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses);

{user_feedback}

Current code is as follows:
The HTML code is:
{html_code}
The CSS code is:
{css_code}
The js code is:
{js_code}

Please list the strawbacks of current page and provide a modification plan and then output the modified html, css and js code.
The output format is as follows:
The strawback of current page:
1.
2.
...

Modify plan:
1.
2.
...

modified html:

modified css:

modified js:
"""

refine_augument_prompt = """
You are a web design maestro. The images provided show the current implementation of the webpage. Please analyze them thoroughly and identify areas for improvement. 

Specifically, focus on:
1. Aesthetic Layout and Design:Evaluate whether the page layout is visually appealing. Identify any areas where the layout could be modified for better aesthetics or symmetry. Suggest improvements in the arrangement of elements to create a more balanced and pleasing design.
2. Functionality and Completeness:Assess if the page's existing functionality is complete and appropriate. Identify any essential features that are currently missing and need to be added. Provide suggestions on enhancements or additional functionalities that could improve the overall effectiveness of the webpage.
3. User Experience Enhancement: Explore opportunities to enhance user experience by adding special effects, such as animations, hover effects, or scrolling effects. Recommend the inclusion of buttons, interactive elements, or other UI components that can make the page more engaging. Suggest ways to utilize colors and typography effectively to elevate the user experience without disrupting the theme and cohesiveness of the design.

The page information is as follows: {page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses);

{user_feedback}

Current code is as follows:
The HTML code is:
{html_code}
The CSS code is:
{css_code}
The js code is:
{js_code}

Please list the strawback of current page and provide a modification plan and then output the modified html, css and js code.
The output format is as follows:
The strawback of current page:
1.
2.
...

Modify plan:
1.
2.
...

modified html:

modified css:

modified js:
"""

refine_css_prompt = """
You are a web design master, and your task is to modify the HTML and CSS code of the web page to make the layout more exquisite.
The above image shows the current rendering of our web page.

The page information is as follows: {page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses);

You need to focus on:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.If there is no specific explanation in the img, you can fabricate it according to your needs.
3.You need to pay strict attention to the page layout, maintain aesthetics, and try to have a sense of symmetry.For example, you need to control the relative size of IMG(The image size should be reasonable and not too large) by controlling its CSS format to make the layout more reasonable.
4.Please analyze the current page's header, navigation, content arrangement, sidebars, footers, visual elements, layout, call to action, responsiveness, and any other features, and analyze how to optimize these to make the layout more beautiful and harmonious.
5.Encourage you to use more colors(Must match the theme of the page and not be too abrupt), more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
6.Try to make the page appear rich and not boring. 
7.Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.


Please think about the strawback of the current page and how to modify the code to make the page more beautiful and harmonious.
The code of page are as follows:
{html_code}

The CSS code is: 
{css_code}
Please  list the strawback of current page and provide a modification plan and then output the modified html, css code.
The output format is as follows:
The strawback of current page:
1.
2.
...

Modify plan:
1.
2.
...
modified html:

modified css:
"""

def get_plan_prompt(text = None,img = None):
    if img and text:
        prompt = f"Your task is to design which pages we should create to design the website for task: {text};The above image is a reference website we have provided to you. "
    elif img:
        prompt = "Your task is to design which pages we should create to design the website based on the website images I provided you."
    else:
        prompt = f"Your task is to design which pages we should create to design the website for task: {text};"
    prompt += plan_output_format_prompt
    return prompt


def get_write_original_website_prompt(text = None,img = None,page_info = None):
    if img and text:
        prompt = write_original_website_img_text_prompt.format(text=text,page_info=page_info)
    elif img:
        prompt = write_original_website_img_prompt.format(page_info=page_info)
    elif text:
        prompt = write_original_website_text_prompt.format(text=text,page_info=page_info)
    else:
        prompt = write_original_website_prompt.format(page_info=page_info)
    return prompt

def get_refine_prompt(text = None,img = None,html_code = None,css_code = None,js_code = None,page_info = None,feedback = ""):
    if img and text:
        prompt = refine_img_text_prompt.format(text=text,html_code=html_code,css_code=css_code,js_code = js_code,feedback=feedback,page_info=page_info)
    elif img:
        prompt = refine_img_prompt.format(html_code=html_code,css_code=css_code,js_code = js_code,feedback=feedback,page_info=page_info)
    elif text:
        prompt = refine_text_prompt.format(text=text,html_code=html_code,css_code=css_code,js_code = js_code, feedback=feedback,page_info=page_info)
    else:
        prompt = refine_raw_prompt.format(html_code=html_code,css_code=css_code,js_code = js_code,feedback=feedback,page_info=page_info)
    return prompt

# def get_refine_layout_prompt(text = None,img = None,html_code = None,css_code = None,feedback = ""):
#     if img:
#         prompt = refine_layout_img_prompt.format(html_code=html_code,css_code=css_code,feedback=feedback)
#     else:
#         prompt = refine_layout_text_prompt.format(html_code=html_code,css_code=css_code,feedback=feedback)
#     return prompt