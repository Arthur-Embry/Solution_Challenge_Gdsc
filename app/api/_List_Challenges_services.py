from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

#parameters for _List_Challenges_
class _List_Challenges_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# This endpoint allows the user to list all the challenges in the system.
def _List_Challenges_run(params: _List_Challenges_params):
    #TODO: add code
    return "hello world"