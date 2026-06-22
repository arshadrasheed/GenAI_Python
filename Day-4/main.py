from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to my first FastAPI application!"
    }


@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}