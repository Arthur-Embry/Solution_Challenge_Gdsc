from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

#parameters for _List_Solutions_
class _List_Solutions_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# This endpoint allows the user to list all the solutions in the system.
def _List_Solutions_run(params: _List_Solutions_params):
    #TODO: add code
    return "hello world"