from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

class points_params(BaseModel):
    #TODO: implement params
    pass

def points_run(params: points_params):
    #TODO: implement function
    pass
    
class leaderboard_params(BaseModel):
    #TODO: implement params
    pass

def leaderboard_run(params: leaderboard_params):
    #TODO: implement function
    pass
    
class friends_params(BaseModel):
    #TODO: implement params
    pass

def friends_run(params: friends_params):
    #TODO: implement function
    pass
    
class streaks_params(BaseModel):
    #TODO: implement params
    pass

def streaks_run(params: streaks_params):
    #TODO: implement function
    pass