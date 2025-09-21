from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import User
from schemas import User as UserSchema, ShowUser
from hashing import Hash

router = APIRouter(tags=["users"])

@router.post("/user", response_model=ShowUser)
def create_user(request: UserSchema, db: Session = Depends(get_db)):
    new_user = User(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/user/{id}", response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User {id} not found")
    return user
