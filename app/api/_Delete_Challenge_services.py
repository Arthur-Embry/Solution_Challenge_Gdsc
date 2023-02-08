from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

#parameters for _Delete_Challenge_
class _Delete_Challenge_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# This endpoint allows the user to delete an existing challenge.
def _Delete_Challenge_run(params: _Delete_Challenge_params):
    #TODO: add code
    return "hello world"