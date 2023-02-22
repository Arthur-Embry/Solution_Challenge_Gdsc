from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import types
import re
import markdown
import dotenv

os.environ["OPENAI_API_KEY"]="foo"

#load environment variables
for i in os.listdir(os.getcwd()):
    if i.endswith(".env"):
        dotenv.load_dotenv(os.path.join(os.getcwd(), i))


description = """
Solution Challenge GDSC API helps you do awesome stuff.

## Benefits of an API
An API is a great way to provide a solution challenge with a program that can be easily integrated into a wide variety of applications. The API allows the program to be used by developers and end users alike, providing an easy-to-use interface and access to the program's functionality. This allows developers to quickly and easily build applications that can interact with the program, while end users can benefit from the program's functionality without needing to understand the underlying code. Additionally, an API makes it possible to keep the program up-to-date with the latest changes and improvements, as well as integrate with other applications. With an API, the program can be quickly and easily adapted to meet the needs of a wide variety of users.

## Pages


# Restfull Endpoints
"""

app = FastAPI(
    title="Solution_Challenge_Gdsc",
    description=description,
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#exposure template
def expose(endpoint,service):
    
    #import the service and define the function and parameters
    service_import=__import__("app.api."+service+'_services')
    function_import=service_import.__dict__['api'].__dict__[service+'_services'].__dict__[endpoint+'_run']
    function_params=service_import.__dict__['api'].__dict__[service+'_services'].__dict__[endpoint+'_params']

    # Decorate it with your decorator and then pass it to FastAPI
    def template(item: function_params):
        """TODO: add comments to this function"""
        #catch special case of default parameters changing from string to tuple
        for i in item:
            if type(i[1])==tuple:
                setattr(item, i[0].split("=")[0], i[1][0])

        return function_import(item)

    globals()[endpoint+"_global"] = types.FunctionType(template.__code__, {}, name=template.__name__, argdefs=template.__defaults__, closure=template.__closure__)
    globals()[endpoint+"_global"].__name__ = service + " - " + endpoint
    globals()[endpoint+"_global"].__annotations__ = {"item": function_params}
    if function_import.__doc__!=None:
        first_pass=markdown.markdown(str(function_import.__doc__))
        #isolate the code block
        code_block=first_pass.split("<code>")[1].split("</code>")[0]
        second_pass=markdown.markdown(code_block)
        app.post("/"+endpoint, description=second_pass)(globals()[endpoint+"_global"])
    else:
        app.post("/"+endpoint)(globals()[endpoint+"_global"])

        # Define special streaming catch
    def template_static(item: function_params):
        """This is a static function - it returns a promise, not a stream"""
        #catch special case of default parameters changing from string to tuple
        for i in item:
            if type(i[1])==tuple:
                setattr(item, i[0].split("=")[0], i[1][0])
        output=""
        #check for generator output and convert to string
        try:
            for i in function_import(item):
                output+=i
        except:
            output=function_import(item)
        return output
    globals()[endpoint+"_static_global"] = types.FunctionType(template_static.__code__, {}, name=template_static.__name__, argdefs=template_static.__defaults__, closure=template_static.__closure__)
    globals()[endpoint+"_static_global"].__name__ = service + " - " + endpoint + " static"
    globals()[endpoint+"_static_global"].__annotations__ = {"item": function_params}
    app.post("/static/"+endpoint, include_in_schema=False)(globals()[endpoint+"_static_global"])

#find all files in os.getcwd() app/api
for i in os.listdir(os.getcwd()+"/app/api"):
    #find all files that end with _services.py
    if i.endswith("_services.py"):
        #list all functions in the file that end with _run
        actions_ref=""
        with open("app/api/"+i) as f:
            actions_ref=f.read()
        for j in re.findall("def (.*):",actions_ref):
            if("_run" in j):
                expose(j.split("_run")[0],i.split("_services")[0])

#[notebook-paper](../notebook-paper/index.html)
pages_string=""
#find all files in os.getcwd() app/api
for i in os.listdir(os.getcwd()+"/app/public"):
    #check if dist folder in i
    if "dist" in os.listdir(os.getcwd()+"/app/public/"+i):
        #add static folder to app
        app.mount("/"+i, StaticFiles(directory=os.getcwd()+"/app/public/"+i+"/dist"), name=i)
        pages_string+="["+i+"](../"+i+"/index.html)\n<br>"

app.description=description.replace("## Pages","## Pages\n"+pages_string)


def remap(path, new_path):
    path = "app/"+path if "/code" in os.getcwd() else path
    @app.get("/"+new_path, response_class=HTMLResponse)
    async def serve_page():
        with open(path) as f:
            lines = f.readlines()
        return ''.join(lines)

#remap Devkits/sdk.js
remap("public/DevKits/sdk.js","sdk.js")