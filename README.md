# WebDesignAgent
## Demo Video
### Auto Generation
<video>
  <source src="assets/autogen.mp4" type="video/mp4">
</video>


### Human Feedback
<video>
  <source src="assets/feedback.mp4" type="video/mp4">
</video>



## Quick Start

```bash
Make sure you install the google chrome
```

```bash
git clone https://github.com/DAMO-NLP-SG/WebDesignAgent.git
cd WebDesignAgent
pip install -r requirement.txt
```

Add your API_KEY

If you use Azure API
LLM.py line 22
<div style="text-align: center;">
  <img src="assets/azure_api.png"/>
</div>

elif you use Openai API

Set is_azure = False(LLM.py line 18)

LLM.py line 39
<div style="text-align: center;">
  <img src="assets/openai_api.png"/>
</div>


If you want to run in terminal
In webdesign.py line 371 set img(img path) or text

```python
agent.act(img = "1.png",text = "a shopping website")
```

And then
```bash
python webdesign.py
```


If you want to run in GUI
```python
python gui.py
```



