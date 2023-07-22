from typing import Union
from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse,PlainTextResponse
from pydantic import BaseModel
from datetime import date

        # "username": "john_doe",
        # "name": "John Doe",
        # "dob": "1995-06-15",
        # "gender": "Male",
        # "age": 28

class User(BaseModel):
    username: str
    name: str
    dob: date
    gender: str
    age: int

app = FastAPI()

users_list = []

def returnUser(username):
    for user in users_list:
        if user.username == username:
            return user
        else:
            return "<h1> Status 404 Not Found </h1>"

@app.get("/")
async def redirect_response_example():
    return RedirectResponse(url="/users")

@app.get("/users", response_class=JSONResponse)
async def getUsers():
    return {"usersList": users_list}

@app.get("/users/{username}", response_class=JSONResponse)
async def getUser(username: str):
    user = returnUser(username)
    # return user user: {}

@app.post("/users/", response_class=HTMLResponse)
async def createUser(request: Request, data: User = Body(...)):
    
    users_list.append({
        "username": data.username,
        "name" : data.name,
        "dob": data.dob,
        "gender": data.gender,
        "age": data.age
    })

    return "<h1> Status 201 Created </h1>"

@app.put("/users/{username}", response_class=HTMLResponse)
async def updateUser(username: str, request: Request, data: User = Body(...)):

    if not username:
        return "<h1> Status 400 Bad Request </h1>"
    
    temp = returnUser(data.username)

    if data.username:
        temp.username = data.username

    if data.name:
        temp.name = data.name

    if data.dob:
        temp.dob = data.dob

    if data.gender:
        temp.gender = data.gender

    if data.age:
        temp.age = data.age

    return "<h1> Status 200 OK </h1>"

@app.delete("/users/{username}", response_class=HTMLResponse)
async def updateUser(username: Union[str, None] = None):
    
    if not username:
        return "<h1> Status 400 Bad Request </h1>"

    temp = returnUser({username})
    
    try:
        users_list.remove(temp)
    except:
        return "<h1> Status 404 Not Found </h1>"
    
    return "<h1> Status 204 No Content </h1>"

@app.get("/{randomString}}")
async def randomUserNotFoundRequest():
    content = "<h1> Status 404 Not Found </h1>"
    headers = {"X-Custom-Header": "CustomHeaderValue"}
    return PlainTextResponse(content, status_code=404, headers=headers)

@app.get("/users/{randomString}")
async def randomUserNotFoundRequest():
    content = "<h1> Status 404 Not Found </h1>"
    headers = {"X-Custom-Header": "CustomHeaderValue"}
    return PlainTextResponse(content, status_code=404, headers=headers)