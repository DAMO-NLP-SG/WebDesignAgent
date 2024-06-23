<p align="center">
<a href=""><img src="assets/logo.jpg"" width="150px"></a> 
</p>
<p align="center"">
<b>WebDesignAgent : A web design agent that can help you easily build a website.</b>
</p>
<p align="center">
<a href="https://opensource.org/license/apache-2-0"><img src="https://img.shields.io/badge/License-Alpaca-blue.svg"></a>
<a href="https://github.com/DAMO-NLP-SG"><img src="https://img.shields.io/badge/Institution-DAMO-red"></a>
<a href="[https://github.com/DAMO-NLP-SG](https://github.com/DAMO-NLP-SG/WebDesignAgent/issues)"><img src="https://img.shields.io/bitbucket/issues/DAMO-NLP-SG/WebDesignAgent"></a>
<a><img src="https://hits.dwyl.com/DAMO-NLP-SG/WebDesignAgent.svg?style=flat-square&show=unique"></a>
  
</p>


## Description
A powerful agent can help you with web design and related code generation.

It supports:
1. Generate corresponding websites based on text descriptions.
2. Generate corresponding websites based on the corresponding images.
3. Generate websites based on both text and images simultaneously.
4. Code modifications can be made based on user feedback.
5. Use visual models for React.
6. Support the generation of multiple web pages, and web pages can be connected and redirected between them.
7. Users can manually add or delete web pages and modify their content.

## Demo Video
### Auto Generation
[feedback.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/63641bf7-ffb6-4518-a594-4a7223ec2899)

### Human Feedback
[auto.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/d5f099e0-5a01-44fa-bb26-bf7733fd9608)

## Quick Start
```bash
git clone https://github.com/DAMO-NLP-SG/WebDesignAgent.git
cd WebDesignAgent
pip install -r requirements.txt
```

### Set config

set config.yaml
```yaml
web_type : "chrome" # "chrome" or "firefox" or "edge"

is_auzer : True # set True if you use azure openai api
AZURE_OPENAI_ENDPOINT : ""
AZURE_OPENAI_KEY : ""
AZURE_OPENAI_API_VERSION : ""

OPENAI_API_KEY : ""
OPENAI_PROXY_URL : ""
```


### Run in terminal
Our method support three ways to generate a website: 

1. Depend on a description of a website.
2. Depend on a img of a website.
3. Both on them.


Set save path and img(img path) or text
```bash
python webdesign.py --save_file "saves/shopping/" --text "a shopping website" --img "damo.png"
```



### Run in GUI
```python
python gui.py
```
Then you will enter the gui as follows:
<img width="1597" alt="gui" src="https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/b46d236b-ad18-4b99-9ccf-c4e787fc5048">

You can select the mode between chat and web design, and choose the model.

#### Auto Generation
If you want to auto generate a website. You can follow the following steps to proceed：

1. set save file(the generated website will be saved in this file).
2. set the description of the website or give a img for website or both.
3. click plan.
4. set refine times you want.
5. click auto generation.


#### Human Feedback
If you want to generate a website more human control. You can follow the following steps to proceed：

1. set save file(the generated website will be saved in this file).
2. set the description of the website or give a img for website or both.
3. click plan.
4. click page you want to modify, and modify anything you want to change.
5. click create website.
6. enter feedback if needed and click refine website.

## Cost
We conducted the following tests for each setting, and the specific test results are stored in the example file.
(The time cons is greatly affected by the internet speed, and you can calculate the specific time from the token cost)

Model = "gpt-4o"  page_num = 10  Website_description = "a shopping website"  Web_type = "chrome" OS = "Windows"

refine_augment = Open   each_refine_times = 3: Total token cost = 4.98$, Total delle-3 cost = 1.24$, Total time cost = 8849s(147min)(2.5h) save_path = example/shopping_open_3

refine_augment = Close  each_refine_times = 3: Total token cost = 3.03$, Total delle-3 cost = 1.36$, Total time cost = 6424s(107min)(1.78h) save_path = example/shopping_close_3

refine_augment = Open  each_refine_times = 2: Total token cost = 3.40, Total delle-3 cost = 1.56, Total time cost = 4808s(80min)(1.33h) save_path = example/shopping_open_2

refine_augment = Close   each_refine_times = 2: Total token cost = 2.20$, Total delle-3 cost = 1.48$, Total time cost = 4736s(79min)(1.31h) save_path = example/shopping_close_2

refine_augment = Close  each_refine_times = 0: Total token cost = 0.39$, Total delle-3 cost = 0.48$, Total time cost = 920s(15min)(0.25h)
save_path = example/shopping_0

Model = "gpt-4o"  page_num = 10  Website_image = "alibaba.png"  Web_type = "chrome" OS = "Windows"
refine_augment = Open  each_refine_times = 2: Total token cost = 3.52$, Total delle-3 cost = 1.96$, Total time cost = 5942(99min)(1.65h)
save_path = example/alibaba

Model = "gpt-4o"  page_num = 9  Website_image = "damo.png"  Web_type = "chrome" OS = "Windows"
refine_augment = Open  each_refine_times = 2: Total token cost = 3.52$, Total delle-3 cost = 1.96$, Total time cost = 5942(99min)(1.65h)
save_path = example/alibaba


You can compare the differences in web pages generated by various configurations and choose the configuration that better meets your needs. 

Of course, our suggestion is that you can first roughly generate all web pages, and then use our refine function to refine a single web page.

You can replace the drawing model with your own interface to reduce the cost.

Change LLM.py(_get_openai_imgs) to replace the drawing model.

## Examples
We provide three website generated by web design agent.

You can find in example/

### 1.damo
website generated by an img(damo.png) (example/damo/index.html)
<p align="center">
<a href=""><img src="example/damo.png"></a>
</p>

---
---
---

### 2.shopping
website generated by a description(a shopping website) (example/shopping/index.html)
<p align="center">
<a href=""><img src="example/shopping.png"></a>
</p>

---
---
---


### 3.game
website generated by an img(damo.png) and a description(An action game company, whose famous work is Black Myth Wukong) (example/game/index.html)

<p align="center">
<a href=""><img src="example/game.png"></a>
</p>

## Plan (To do)

1. Generate supporting backend code.
2. At present, this is still a relatively rough demo, and we really hope that you can provide feedback to help us improve it. We welcome you to raise issues to point out our shortcomings.
