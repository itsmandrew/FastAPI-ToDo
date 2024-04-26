from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "Hello World!"}


todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos" : todos}

# Get single todo


# Create a todo

# updata a todo


#delete a todo