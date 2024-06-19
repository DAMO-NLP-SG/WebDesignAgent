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
Your task is to write the HTML, CSS and js code for the page based on the image information I provided you. 
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
        "jump_page" : {The name of the page to jump to},
        },
        ...
    ]
},
"useful_buttons": [
{
"button_name":{The name of the button},
"button_description":{The description of the button}
},
...
],
"additional_features": {additional features you want to add to the page},
"is_main_page" : {true or false,true, if the page is the image we provided}
},
{
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
"useful_buttons": [
{
"button_name" : {The name of the button},
"button_function" : {The function of the button}
},
...
],
"additional_features": {additional features you want to add to the page},
"is_main_page" : {true or false,true, if the page is the image we provided}
},
......
]
"""

refine_page_prompt = """
You are a web design master, and your current task is to modify the details of a website.{task_info}
The following page is one of the pages of the  website. Please help me enrich its details and be careful not to change the format(the modified page should be dict format and no extra output)(Do not add new links. You can enrich the page details by enriching the description and other methods(such as layout)).
The page is:
{page_info}
please output your thinking steps firstly and then output the modified page.
The output format should be as follows:
Thinking steps:
{{your thinking steps}}

modified_page:
{{your modified page}}
"""

refine_img_text_prompt = """
You are a code modification master, and your goal is to modify the HTML, CSS and js code to meet my needs.
The page requirement: {text};

The first page is a reference page we have provided to you, You need to refer to his content layout and layout format to build a new webpage. The current HTML code website is the second website. 

Please analyze which excellent aspects the second webpage can learn from the first webpage to improve oneself and think how to improve the code to refine the second page.

Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.
3.If you want to add images through JavaScript, please define img as the following format: {{imgSrc: "product1. jpg", description: 'Description for product 1, such as a black phone',... }}.If there is no specific explanation in the img, you can fabricate it according to your needs.
4.You must think extra about how to improve the functionality of the page and how to improve its practicality by modifying the code.
5.You need to pay strict attention to the page layout, maintain aesthetics, and try to have a sense of symmetry.For example, you need to control the relative size of IMG(The image size should be reasonable and not too large) by controlling its CSS format to make the layout more reasonable.
6.Encourage you to use more colors(Must match the theme of the page and not be too abrupt), more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
7.Try to make the page appear rich and not boring. 
8.Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.


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
Please list the advantages of the first page, the strawback of second page and provide a modification plan and then output the modified html, css and js code of second page.
The output format is as follows:
Advantages of first page:
1.
2.
...

Strawbacks of sencond page:
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

refine_img_prompt = """
You are a code modification master, and your goal is to modify the HTML, CSS and js code to meet my needs.
My target page is the first page, and the current HTML code page is the second page. Please analyze the differences between the first page and the second page.
Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.
3.If you want to add images through JavaScript, please define img as the following format: {{imgSrc: "product1. jpg", description: 'Description for product 1, such as a black phone',... }}.If there is no specific explanation in the img, you can fabricate it according to your needs.
4.You must think extra about how to improve the functionality of the page and how to improve its practicality by modifying the code.
5.You need to pay strict attention to the page layout, maintain aesthetics, and try to have a sense of symmetry.For example, you need to control the relative size of IMG(The image size should be reasonable and not too large) by controlling its CSS format to make the layout more reasonable.
6.Encourage you to use more colors(Must match the theme of the page and not be too abrupt), more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
7.Try to make the page appear rich and not boring. 
8.Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.

The page information is as follows:
{page_info}(Note that the file names of the jump pages of the bottom and link are their link addresses)

Please think about how to modify the code to make the page meet our needs (such as adding images, adding buttons, increasing animation effectsincreasing animation effects or add some text content, detailed content etc.).
Please think about how to modify the code to make the page more consistent with the target page.
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
You are a code modification master, and your goal is to modify the HTML, CSS and js code to meet my needs.
The page requirement: {text};
The current HTML code page effect is above(The above img)).
Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.
3.If you want to add images through JavaScript, please define img as the following format: {{imgSrc: "product1. jpg", description: 'Description for product 1, such as a black phone',... }}.If there is no specific explanation in the img, you can fabricate it according to your needs.
4.You must think extra about how to improve the functionality of the page and how to improve its practicality by modifying the code.
5.You need to pay strict attention to the page layout, maintain aesthetics, and try to have a sense of symmetry.For example, you need to control the relative size of IMG(The image size should be reasonable and not too large) by controlling its CSS format to make the layout more reasonable.
6.Encourage you to use more colors(Must match the theme of the page and not be too abrupt), more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
7.Try to make the page appear rich and not boring. 
8.Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.

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
Please list the strawback of current page and provide a modification plan and then output the modified html, css and js code.
The output format is as follows:
Strawback of current page:
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

refine_prompt = """
You are a code modification master, and your goal is to modify the HTML, CSS and js code to meet my needs.
The current HTML code page effect is above(The above img)).
Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.
3.If you want to add images through JavaScript, please define img as the following format: {{imgSrc: "product1. jpg", description: 'Description for product 1, such as a black phone',... }}.If there is no specific explanation in the img, you can fabricate it according to your needs.
4.You must think extra about how to improve the functionality of the page and how to improve its practicality by modifying the code.
5.You need to pay strict attention to the page layout, maintain aesthetics, and try to have a sense of symmetry.For example, you need to control the relative size of IMG(The image size should be reasonable and not too large) by controlling its CSS format to make the layout more reasonable.
6.Encourage you to use more colors(Must match the theme of the page and not be too abrupt), more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
7.Try to make the page appear rich and not boring. 
8.Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.

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
Please list the strawback of current page and provide a modification plan and then output the modified html, css and js code.
The output format is as follows:
Strawback of current page:
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

refine_layout_text_prompt = """
You are a web design master, and your task is to optimize the HTML and CSS code of web pages to make their layout more exquisite and harmonious.
The current HTML code page effect is above(The above img)).

Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.If there is no specific explanation in the img, you can fabricate it according to your needs.
3.You need to pay strict attention to the page layout, maintain aesthetics, and try to have a sense of symmetry.For example, you need to control the relative size of IMG(The image size should be reasonable and not too large) by controlling its CSS format to make the layout more reasonable.
4.Please analyze the current page's header, navigation, content arrangement, sidebars, footers, visual elements, layout, call to action, responsiveness, and any other features, and analyze how to optimize these to make the layout more beautiful and harmonious.
5.Encourage you to use more colors(Must match the theme of the page and not be too abrupt), more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
6.Try to make the page appear rich and not boring. 
7.Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.

{feedback}

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

refine_layout_img_prompt = """
You are a web design master, and your task is to compare two web pages and modify the HTML and CSS code of the second web page to make its layout consistent with the first web page.
Please analyze the differences of layout between the first page and the second page and modify the code to improve the second page.
Here are some precautions:
1.The size of IMG needs to be strictly controlled using CSS to avoid layout changes caused by inconsistent image sizes. 
2.You must add a description field to briefly explain the content of the image, for example:<img src="demo banner 1. jpg" alt="Promotional Banner 1" description="This is the logo of a shopping website, resembling a little dog">.If there is no specific explanation in the img, you can fabricate it according to your needs.
3.You need to pay strict attention to the page layout, maintain aesthetics, and try to have a sense of symmetry.For example, you need to control the relative size of IMG(The image size should be reasonable and not too large) by controlling its CSS format to make the layout more reasonable.
4.Please analyze the page layout pattern of the first page, then analyze the page layout pattern of the second page, and compare the differences between the two (the key is to ensure that each block is located in the same layout position, for example, the layout of the first page is divided into left and right columns, with the username in the first column, and the second page does not have such a layout. You need to analyze according to this pattern)
5.To compare the layouts of two web pages, analyze their header, navigation, content arrangement, sidebars, footers, visual elements, typography, calls to action, responsiveness, and any additional features, noting similarities and differences.
6.You should pay special attention to the block structure of the page layout. Please analyze the page layout block of the first image and block it with the page layout block of the second image, and ensure that the block structure of the two is consistent.
7.Encourage you to use more colors(Must match the theme of the page and not be too abrupt), more buttons, and more exquisite layout, and try adding more special effects, such as wave effects, gradient effects, scrolling effects, and so on. 
8.Try to make the page appear rich and not boring. 
9.Attention should be paid to coordination, for example, technology websites should be designed with a sense of technology, while shopping websites should have a sense of freshness.

{feedback}

Please think about how to modify the code to make the second page more consistent with the first page.
The code of second page are as follows:
{html_code}

The CSS code is: 
{css_code}
Please list the differences and provide a modification plan and then output the modified html, css code.
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
"""


page_complete_prompt = """
You are a webpage design master, and your task is to complete and refine a unfinished webpage.

The other page information is as follows:
{other_pages_info}

The current page information is as follows:
{page_info}

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
        prompt = refine_prompt.format(html_code=html_code,css_code=css_code,js_code = js_code,feedback=feedback,page_info=page_info)
    return prompt


def get_refine_layout_prompt(text = None,img = None,html_code = None,css_code = None,feedback = ""):
    if img:
        prompt = refine_layout_img_prompt.format(html_code=html_code,css_code=css_code,feedback=feedback)
    else:
        prompt = refine_layout_text_prompt.format(html_code=html_code,css_code=css_code,feedback=feedback)
    return prompt