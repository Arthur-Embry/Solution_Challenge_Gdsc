from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

#parameters for _Get_Solution_
class _Get_Solution_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# This endpoint allows the user to retrieve the information related to a particular solution.
def _Get_Solution_run(params: _Get_Solution_params):
    #TODO: add code
    return "hello world"