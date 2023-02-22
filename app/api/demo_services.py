from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]


class foo_params(BaseModel):
    echo: Union[str,None]="",


def foo_run(params: foo_params):
    if(params.echo==None):
        return "hello world"
    else:
        return params.echo
    
class bar_params(BaseModel):
    echo: Union[str,None]="",

def bar_run(params: bar_params):
    if(params.echo==None):
        return "hello world"
    else:
        return params.echo

class baz_params(BaseModel):
    echo: Union[str,None]="",

def baz_run(params: baz_params):
    if(params.echo==None):
        return "hello world"
    else:
        return params.echo