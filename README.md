<p align="center">
<a href=""><img src="assets/logo.jpg"" width="200px"></a> 
</p>

<h3 align="center">
WebDesignAgent : A web design agent that can help you easily build a website.
</h3>

<p align="center">
<a href="https://opensource.org/license/apache-2-0"><img src="https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg"></a>
<a href="https://github.com/DAMO-NLP-SG"><img src="https://img.shields.io/badge/Institution-DAMO-red"></a>
<a href="[https://github.com/DAMO-NLP-SG](https://github.com/DAMO-NLP-SG/WebDesignAgent/issues)"><img src="https://img.shields.io/bitbucket/issues/DAMO-NLP-SG/WebDesignAgent"></a>
<a><img src="https://hits.dwyl.com/DAMO-NLP-SG/WebDesignAgent.svg?style=flat-square&show=unique"></a>
</p>

# Generation Example Video
### Rely on website images（https://www.heishenhua.com/） and descriptions (黑神话八戒的官方网站，要求有游戏的相关介绍以及介绍游戏科学的发展历史，同时要提供猪八戒智能ai对话功能。游戏科学的成名作是黑神话悟空，它刚获得了2024TGA年度最佳游戏) to generate
[黑八戒.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/f69b1992-4ef0-47e9-91ce-b0b696b581d0)



##  📰 Update
* **[2024.6.28]** WebDesignAgent can arrange your images into a website!
* **[2024.6.27]** WebDesignAgent is now supporting building Chinese Websites!
* **[2024.6.26]**  The first version of WebDesignAgent!
  
## 😊 What is WebDesignAgnet
WebDesignAgnet is an autonomous agent that can help you build a series of websites with one sentence!

### User Input
It supports building webpages with text and images.
1. **Text → Website**: Transform your textual descriptions into fully functional, beautifully designed websites effortlessly.
2. **Images → Website**: Simply upload your images, and watch as they are seamlessly integrated into stunning websites.
3. **Visual Clues → Website**: Bring your visual layout to the websites.
4. **Hybrid Design**: Seamlessly combine text, images and other visual clues to create stunning, cohesive web designs.

### Key Features
1. **Multi-Page Mastery**: Generate and design interconnected web pages with dynamic redirect capabilities for a seamless user experience.
2. **User-specific Add/Delete**: Exercise full control by manually adding, deleting, or modifying web pages, their contents and their relations to tailor your site to perfection.
3. **Iterative Refinement**: Make precise alterations to your website’s code based on your invaluable feedback.
4. **Visual React**: Leverage strong visual models to refine and enhance the webpage layout autonomously.


## Demo Video
### Auto Generation
[autogen_new.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/5c6eee6f-2692-420b-8c3c-681de8323b86)


### Create and Refine a Page
[create_and_refine.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/d2d4dc62-9737-4757-a64a-4730ae048ee8)


### Create a New Page
[add_new_page.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/1fbea13f-dd2f-43a3-8a67-9297fcb733ff)



## 🛠️ Requirements and Installation
```bash
git clone https://github.com/DAMO-NLP-SG/WebDesignAgent.git
cd WebDesignAgent
pip install -r requirements.txt
```

### API config
set config.yaml to use the OpenAI APIs.
```yaml
web_type : "chrome" # "chrome" or "firefox" or "edge"
LLM_TYPE : "openai" # openai

# LLM settings
# azure openai settings
is_auzer : True # set True if you use azure api
AZURE_OPENAI_ENDPOINT : ""
AZURE_OPENAI_KEY : ""
AZURE_OPENAI_API_VERSION : "" # can be blank
AZURE_OPENAI_DALLE_ENDPOINT : ""
AZURE_OPENAI_DALLE_KEY : ""

# openai settings
OPENAI_API_KEY : ""
OPENAI_PROXY_URL : ""


# IMG Generator settings (if not set, it will use the openai settings)
IMG_GEN_TYPE : "dalle3" # "dalle3"
```

## 🚀 Quick Start
We offer two modes for using WebDesignAgent: terminal-based and GUI-based. We recommend trying the GUI mode for its user-friendly interface and greater control.


### 1. Run in GUI
#### Auto Generation
```python
python gui.py
```
Then you will enter the gui as follows:
<img alt="gui" src="assets/gui.png">

For a quick usage of our WebDesignAgent, please following these steps:
1. Config `Select Mode` to `Web Design Mode`.
2. Config `Select Model` according to your APIs. In our demos, we primarily use `gpt-4o`.
3. Select the websites language in `Language` field.
4. Config `CSS Framework` to your favored style, e.g. `Tailwind`.
5. Set `save_file`, which saves your generated websites.
6. **Enter your request in either the `website_description` field for textual requests, the `website_img` field for image requests, or both for a combined input.**
7. Click `Plan` button, which will return the textual descriptions of planned websites, their contents and their relations. You can also change these descriptions if you find them unsuitable.
8. Click `Auto Generate` to generate all the above websites for you. (It may takes some time for the entire websites generation)

#### Human Feedback
If you want to generate a website more human control. You can follow the following steps to proceed：

1. set save file(the generated website will be saved in this file).
2. set the description of the website or give a img for website or both.
3. click plan.
4. click page you want to modify, and modify anything you want to change.
5. click create website.
6. enter feedback if needed and click refine website.

### 2. Run in terminal
Our method support three ways to generate a website: 

1. Depend on a description of a website.
2. Depend on a img of a website.
3. Both on them.


Set save path and img(img path) or text
```bash
python webdesign.py --save_file "saves/shopping/" --text "a shopping website"  --refine_times 2
```



## 💰Cost
| Web Name  | Page Numbers | Refine Times | Image Generation | Total Token Cost | Total Image Cost | Total Time Cost |
|-----------|--------------|--------------|------------------|------------------|------------------|-----------------|
| shopping  | 8            | 2            | open             | $1.14            | $1.48            | 661s            |
| damo      | 6            | 2            | open             | $0.84            | $2.48            | 937s            |
| game      | 9            | 2            | open             | $1.22            | $2.68            | 956s            |


The main cost is img generation cost.
You can choose to set Gen_IMG close, and we will generate the image by replacing the placeholder, which will make your img cost 0.

Also you can replace the drawing model with your own interface to reduce the cost.
Change LLM.py(get_llm()) to replace the drawing model.

## Examples
We provide three website generated by web design agent(We removed all images to reduce the size of the repository).

You can find in examples/

### 1.damo
website generated by an img(damo.png) (examples/damo/index.html)
<p align="center">
<a href=""><img src="assets/damo.png"></a>
</p>

---
---
---

### 2.shopping
website generated by a description(a shopping website) (examples/shopping/index.html)
<p align="center">
<a href=""><img src="assets/shopping.png"></a>
</p>

---
---
---


### 3.game
website generated by an img(damo.png) and a description(An action game company, whose famous work is Black Myth Wukong) (examples/game/index.html)

<p align="center">
<a href=""><img src="assets/game.png"></a>
</p>

## Plan (To do)

1. Generate supporting backend code.
2. Support more LLMs.
3. At present, this is still a relatively rough demo, and we really hope that you can provide feedback to help us improve it. We welcome you to raise issues to point out our shortcomings.
