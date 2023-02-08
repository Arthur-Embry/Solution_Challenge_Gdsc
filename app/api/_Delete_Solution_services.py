from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

#parameters for _Delete_Solution_
class _Delete_Solution_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# This endpoint allows the user to delete an existing solution.1
def _Delete_Solution_run(params: _Delete_Solution_params):
    #TODO: add code
    return "hello world"