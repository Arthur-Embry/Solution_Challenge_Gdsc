from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

#parameters for _Get_Challenge_
class _Get_Challenge_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# This endpoint allows the user to retrieve the information related to a particular challenge.
def _Get_Challenge_run(params: _Get_Challenge_params):
    #TODO: add code
    return "hello world"