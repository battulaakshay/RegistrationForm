from fastapi import APIRouter
from fastapi import FastAPI, Form, Request

from modals.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="templates")


# @router.get("/")
# async def get_todos():
#     todos = list_serial(collection_name.find())
#     return todos
@router.get("/", response_class=HTMLResponse)
async def get_todos(request: Request):
    # todos = list_serial(collection_name.find())
    return templates.TemplateResponse("index.html", {"request": request})


# @router.post("/")
# async def post_todo(todo: Todo):
#     collection_name.insert_one(dict(todo))


@router.post("/submit/")
async def submit_form(
        fullname: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        gender: str = Form(...),
        phonenumber: str = Form(...),
):
    # Create a dictionary with user data
    user_data = {
        "fullname": fullname,
        "email": email,
        "password": password,
        "gender": gender,
        "phonenumber": phonenumber,
    }

    # Insert user data into the MongoDB collection
    result = collection_name.insert_one(user_data)

    # Return a response indicating success
    # return {"message": f"Data saved to MongoDB - User ID: {str(result.inserted_id)}"}
    return {"message": "Data saved to MongoDB", "user_data": {str(user_data)}}


@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})


@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
