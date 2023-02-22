from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]


class suggest_goal_params(BaseModel):
    #TODO: implement params
    pass

def suggest_goal_run(params: suggest_goal_params):
    #TODO: implement function
    pass
    
class gpt_params(BaseModel):
    #TODO: implement params
    pass

def gpt_run(params: gpt_params):
    #TODO: implement function
    pass
    
class whisper_params(BaseModel):
    #TODO: implement params
    pass

def whisper_run(params: whisper_params):
    #TODO: implement function
    pass
    
class tacotron_params(BaseModel):
    #TODO: implement params
    pass

def tacotron_run(params: tacotron_params):
    #TODO: implement function
    pass

class chat_response_params(BaseModel):
    #TODO: implement params
    pass

def chat_response_run(params: chat_response_params):
    #TODO: implement function
    pass