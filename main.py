from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "Hello World!"}


todos = []

# Get all todos


# Get single todo


# Create a todo

# updata a todo


#delete a todo