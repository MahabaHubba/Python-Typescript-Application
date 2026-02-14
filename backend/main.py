from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Import the models
from database import engine, SessionLocal
from models import Message, Base

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

# What this line does is that it tells the library to generate all defined database tables 
# and associated schema with specified database.
# Base refers to the base class created by SQL Alchemy
# Metadata is an attribute of the Base class that acts as a container object that holds onto the information
# create all is the method that performs the actual operation.It looks at the table sotred in the meta-data and issues the create table statement to the database
# On side note, if the table already exists it wont create it
Base.metadata.create_all(bind=engine)

class MessageCreate(BaseModel):
    text:str

def get_db():
    # This is to establish the connection to connect to a specific database
    db = SessionLocal()
    try:
        # Alloed the db to called as a function
        yield db
    finally:
        # it closes the database session releasing the connection back to the connection pool
        db.close()


messages: list[str] = []



@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/messages")
def get_messages(db: Session = Depends(get_db)):
    messages = db.query(Message).all()
    return {"messages": [m.text for m in messages]}

@app.post("/messages")
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    db_message = Message(text = message.text)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return{"status": "ok"}


