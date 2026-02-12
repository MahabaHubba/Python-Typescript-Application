from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS allows for the interaction to happen between front end and backend.
# You may get Error or wont be able to fetch because it wont allows for access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

messages: list[str] = []

class MessageCreate(BaseModel):
    text:str

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/messages")
def get_messages():
    return{"mesages": messages}

@app.post("/messages")
def create_message(message: MessageCreate):
    messages.append(message.text)
    return {"status": "ok"}


