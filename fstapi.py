from fastapi import FastAPI
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434",
)
@app.get("/")
def root():
    return {"Hello": "World"}


