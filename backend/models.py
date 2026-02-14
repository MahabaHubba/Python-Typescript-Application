from sqlalchemy import Column, Integer, String
from database import Base


# Creating a class called Message 
class Message(Base):
    __tablename__ = "messages"

# Created primary ket for id and ensured nothing is nullable.
    id = Column(Integer, primary_key=True, index= True)
    text = Column(String, nullable = False)