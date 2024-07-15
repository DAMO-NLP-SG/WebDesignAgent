<p align="center">
<a href=""><img src="logo.jpg"" width="200px"></a> 
</p>

<h3 align="center">
WebDesignAgent :  Towards Effortless Website Creation
</h3>

<p align="center">
<a href="https://opensource.org/license/apache-2-0"><img src="https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg"></a>
<a href="https://github.com/DAMO-NLP-SG"><img src="https://img.shields.io/badge/Institution-DAMO-red"></a>
<a><img src="https://hits.dwyl.com/DAMO-NLP-SG/WebDesignAgent.svg?style=flat-square&show=unique"></a>
<a><img src="https://img.shields.io/badge/PRs-Welcome-red"></a>
</p>

[harry 1.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/d7ddd748-00d3-47e1-96aa-5a022e857df8)

该网站基于以下提示构建：
* 简单描述：*哈利波特官方网站，充满魔幻元素*
* Dalle3生成的图像
* 人工反馈

[黑八戒.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/f69b1992-4ef0-47e9-91ce-b0b696b581d0)

该网站基于以下提示构建：
* 参考网站布局：*wukong.png*
* 简单描述：*请为《黑神话：八戒》构建官方网站。它需要详细介绍游戏以及 Game Science 的开发历史。此外，它还应提供与八戒的智能 AI 对话功能。Game Science 的著名作品是《黑神话：悟空》，它刚刚获得了 2024 年 TGA 年度游戏奖。*
* 本地图像
* 人工反馈

[taobao.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/62f96da3-6b10-4d91-9ccb-fb2c408163bf)

该网站基于以下提示构建：
* 参考网站布局：*taobao.png*
* Dalle3生成的图像
* 人工反馈

##  📰 最近更新
* **[2024.7.15]** WebDesignAgent 可以支持 Qwen 模型(不支持视觉模型，同时异步调用存在一些问题，生成速度较慢，欢迎 PR 解决这个问题) 和 cogview-3 以及 sd3(完全免费！)。
* **[2024.7.5]** WebDesignAgent 可以支持 Claude 和 chatglm(不支持视觉模型) 模型！
* **[2024.6.28]** WebDesignAgent 现已支持搭建中文网站，并且可以把本地图片排版成网站！
* **[2024.6.26]** WebDesignAgent 发布了第一个版本！
  
## 😊 什么是 WebDesignAgent
WebDesignAgnet 是一个强力的智能体，可以根据您的需要自动帮助您构建一系列网站。

它支持如下方式构建网站：
* **文本 → 网站**：根据您的文本描述生成对应网站。
* **图像 → 网站**：根据您上传的图像，生成对应网站。
* **文本+图像 → 网站**：根据你提供的图像，模仿其布局生成符合你文本描述的网站。

主要支持以下功能：
* **多网页生成**：生成多个网页，并且支持多网页间跳转。
* **用户指定网页添加/删除**：通过手动添加、删除或修改网页内容及其关系来定制您的网站。
* **人工反馈**：支持根据您的反馈对网站代码进行精确修改。
* **视觉反射**：利用强大的视觉模型自主改进和增强网页布局。

<!--
 ## Demo Video
 ### Auto Generation
 [autogen_new.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/5c6eee6f-2692-420b-8c3c-681de8323b86)


 ### Create and Refine a Page
 [create_and_refine.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/d2d4dc62-9737-4757-a64a-4730ae048ee8)


 ### Create a New Page
 [add_new_page.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/1fbea13f-dd2f-43a3-8a67-9297fcb733ff)
-->





## 🛠️ 运行条件
```bash
git clone https://github.com/DAMO-NLP-SG/WebDesignAgent.git
cd WebDesignAgent
pip install -r requirements.txt
```

### API config
set config.yaml to use the OpenAI APIs.
```yaml
web_type : "chrome" # "chrome" or "firefox" or "edge"
LLM_TYPE : "openai" # openai or claude or glm or qwen

# LLM settings
# openai settings
is_azure : True
AZURE_OPENAI_ENDPOINT : ""
AZURE_OPENAI_KEY : ""
AZURE_OPENAI_API_VERSION : ""

AZURE_OPENAI_DALLE_ENDPOINT : ""
AZURE_OPENAI_DALLE_KEY : ""

OPENAI_API_KEY : ""
OPENAI_PROXY_URL : ""
OPENAI_BASE_URL : ""

# claude settings
CLAUDE_API_KEY : ""

# glm settings and congview settings
GLM_API_KEY : ""

# qwen settings
DASHSCOPE_API_KEY : ""

# sd3 settings
SD3_API_KEY : ""

# IMG Generator settings (if not set, it will use the openai settings)
IMG_GEN_TYPE : "dalle3" # "dalle3" or "cogview-3" or "sd3"
```

## 🚀 快速开始
我们提供两种使用 WebDesignAgent 的方法：基于终端和基于 GUI。我们建议您尝试使用GUI，因为它具有用户友好的界面和更好的控制能力。


### 1. GUI使用

```python
python gui.py
```
然后你会得到以下GUI界面
<img alt="gui" src="gui.png">

#### 自动生成
要快速使用我们的 WebDesignAgent，请按照以下步骤操作：
1. 将 `Select Mode` 配置为 `W​​eb Design Mode`。
2. 根据您的 API 配置 `Select Model`。在我们的演示中，我们主要使用 `gpt-4o`。
3. 在 `Language` 字段中选择网站语言。
4. 将 `CSS Framework` 配置为您喜欢的样式，例如 `Tailwind`。
5. 设置 `save_file`，该路径用于保存您生成的网站。
. **在 `website_description` 字段中输入网站的文本描述、`website_template_path` 字段输入网站的图像模版（图像路径）或两者同时输入。**
7. 如果您想使用本地图像构建您的网站，请指明我们的智能体要加载的图像存储路径 `local_img_storage_path`，然后单击 `load`。
8. 点击`Plan`按钮，将返回计划网站、其内容及其关系的文本描述。如果您发现这些描述不合适，也可以更改它们。
9. 点击`Auto Generate`按钮为您生成上述所有网站。您创建​​的网站的屏幕截图将显示在GUI工具的右侧。（整个网站生成可能需要一些时间）
10. 将 Vision 设置为`Close`可以降低成本，但会降低质量。

#### 人工反馈
如果您想精细化控制生成网站。
按照**自动生成**中的步骤1-7获取自动生成的计划。然后使用以下方式自定义您的网站：
* 您可以通过直接输入自己的想法来修改计划结果。
* 您还可以添加/删除不满意的网页。
* 您还可以在`feedback`字段中提供一些反馈，以全局控制创建的网站。


### 2. 终端上运行
```bash
python webdesign.py --save_file "saves/shopping/" --text "a shopping website"  --refine_times 2
```

## 👀 样例

### 1.阿里巴巴达摩院官网
根据阿里巴巴达摩院官网图片生成: examples/damo/index.html
<p align="center">
<a href=""><img src="damo.png"></a>
</p>

---

### 2.Shopping
根据文字描述（一个购物网站）生成: examples/shopping/index.html
<p align="center">
<a href=""><img src="shopping.png"></a>
</p>

---

### 3.Game
根据描述（一个游戏网站）跟达摩院官网图片共同生成: examples/game/index.html

<p align="center">
<a href=""><img src="game.png"></a>
</p>

## 📑 未来计划
1. 支持更多 LLM。
2. 支持本地代码修改。
3. 生成支持后端代码。
4. 目前这还是一个比较粗糙的 demo，非常希望大家能提供反馈帮助我们改进，欢迎大家提出问题，指出我们的不足。


## WeChat
如果有任何问题，欢迎加入我们的群聊。
<p align="center">
<a href=""><img src="wechat.png"></a>
</p>