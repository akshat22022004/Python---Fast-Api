from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    body: str
    published: bool = True

class ShowBlog(BaseModel):
    title: str
    body: str

    class Config:
      from_attributes = True  # or from_attributes=True if Pydantic v2

class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
       from_attributes= True

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[ShowBlog] = []

    class Config:
       from_attributes = True
