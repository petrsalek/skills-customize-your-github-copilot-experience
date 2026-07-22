from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class EchoRequest(BaseModel):
    message: str


class EchoResponse(EchoRequest):
    received: bool


@app.get("/hello")
def hello():
    return {"message": "Hello, world!"}


@app.post("/echo", response_model=EchoResponse)
def echo(req: EchoRequest):
    return {"message": req.message, "received": True}
