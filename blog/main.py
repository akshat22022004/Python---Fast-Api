from fastapi import FastAPI
from database import engine
from models import Base
from routers import blog, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)


