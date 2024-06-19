
from LLM import Openai_response

Openai_Models = ["gpt-35-turbo-16k","gpt4-turbo-2024-04-29"]

class BaseAgent:
    # gpt-35-turbo-16k  gpt4-turbo-2024-04-29
    def __init__(self,model = "gpt-35-turbo-16k") -> None:
        self.model = model
    
    def act(self, instruction):
        raise NotImplementedError
    

    def get_LLM_response(self,messages,**kwargs):
        if kwargs.get("model") == None:
            kwargs["model"] = self.model
        return Openai_response(messages,**kwargs)
    
    def get_answer(self,messages,**kwargs):
        response = self.get_LLM_response(messages,model = self.model,**kwargs)
        return response.choices[0].message.content



    


