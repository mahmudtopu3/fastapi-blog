from fastapi import APIRouter, HTTPException, Depends,Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.models import Blog, BlogCreate, BlogRead, User
from app.core.crud import create_blog, get_blog, get_user_blogs, delete_blog, update_blog
from app.core.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=BlogRead)
def create_blog_endpoint(blog: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_blog(db, blog, current_user.id)

# @router.get("/", response_model=list[BlogRead])
# def read_user_blogs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return get_user_blogs(db, current_user.id)


@router.get("/", response_model=list[BlogRead])
def read_user_blogs(db: Session = Depends(get_db), 
                    current_user: User = Depends(get_current_user), 
                    skip: int = Query(0, ge=0), 
                    limit: int = Query(10, ge=1, le=100)):
    """
    Retrieve paginated blogs created by the current user.
    
    - **skip**: int - Number of entries to skip (for pagination).
    - **limit**: int - Maximum number of entries to return (for pagination).
    """
    blogs = get_user_blogs(db, current_user.id, skip=skip, limit=limit)
    return blogs

@router.put("/{blog_id}", response_model=BlogRead)
def update_blog_endpoint(blog_id: int, blog: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_blog = get_blog(db, blog_id)
    if db_blog is None or db_blog.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this blog")
    return update_blog(db, blog_id, blog)

@router.delete("/{blog_id}")
def delete_blog_endpoint(blog_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_blog = get_blog(db, blog_id)
    if db_blog is None or db_blog.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this blog")
    delete_blog(db, blog_id)
    return {"message": "Blog deleted successfully"}
