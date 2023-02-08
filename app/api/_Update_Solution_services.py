from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

#parameters for _Update_Solution_
class _Update_Solution_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# This endpoint allows the user to update the existing solution.
def _Update_Solution_run(params: _Update_Solution_params):
    #TODO: add code
    return "hello world"