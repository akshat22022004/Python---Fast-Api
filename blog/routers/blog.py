from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Blog
from schemas import ShowBlog, Blog as BlogSchema

router = APIRouter(tags=["blogs"])

@router.get("/blog", response_model=List[ShowBlog])
def all_blogs(db: Session = Depends(get_db)):
    return db.query(Blog).all()

@router.post("/blog", status_code=status.HTTP_201_CREATED, response_model=ShowBlog)
def create_blog(request: BlogSchema, db: Session = Depends(get_db)):
    new_blog = Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/blog/{id}", response_model=ShowBlog)
def show_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog {id} not found")
    return blog

@router.put("/blog/{id}", response_model=ShowBlog)
def update_blog(id: int, request: BlogSchema, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog {id} not found")
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return blog.first()

@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
