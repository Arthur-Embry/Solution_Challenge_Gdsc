from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

#parameters for _Create_Challenge_
class _Create_Challenge_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# This endpoint allows the user to create a new challenge.
def _Create_Challenge_run(params: _Create_Challenge_params):
    #TODO: add code
    return "hello world"