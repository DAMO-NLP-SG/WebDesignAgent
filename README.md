# WebDesignAgent
## Demo Video
### Auto Generation
<video controls src="assets/autogen.mp4" title="Auto generate a website"></video>

### Human Feedback
<video controls src="assets/feedback.mp4" title="Create a website by human feedback"></video>

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
```python
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["AZURE_OPENAI_KEY"] = ""
os.environ["AZURE_OPENAI_API_VERSION"] = ""
```

elif you use Openai API

Set is_azure = False(LLM.py line 18)

LLM.py line 39
```python
os.environ["OPENAI_API_KEY"] = ""
os.environ["OPENAI_PROXY_URL"] = ""
```


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



