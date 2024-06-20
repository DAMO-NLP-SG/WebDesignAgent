# WebDesignAgent
## Demo Video
### Auto Generation
[auto.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/d5f099e0-5a01-44fa-bb26-bf7733fd9608)

### Human Feedback
[feedback.webm](https://github.com/DAMO-NLP-SG/WebDesignAgent/assets/109561120/63641bf7-ffb6-4518-a594-4a7223ec2899)

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



