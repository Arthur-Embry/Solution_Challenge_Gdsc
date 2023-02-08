from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

#parameters for _Submit_Solution_
class _Submit_Solution_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# This endpoint allows the user to submit a solution for a particular challenge.
def _Submit_Solution_run(params: _Submit_Solution_params):
    #TODO: add code
    return "hello world"