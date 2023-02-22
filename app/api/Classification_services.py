from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

class goal_completion_params(BaseModel):
    #TODO: implement params
    pass

def goal_completion_run(params: goal_completion_params):
    #TODO: implement function
    pass
    
class mnli_params(BaseModel):
    #TODO: implement params
    pass

def mnli_run(params: mnli_params):
    #TODO: implement function
    pass
