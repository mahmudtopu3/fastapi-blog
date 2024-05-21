from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.models import Author, AuthorCreate, AuthorRead
from app.core.crud import create_author, get_author

router = APIRouter()

@router.post("/", response_model=AuthorRead)
def create_author_endpoint(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = get_author(db, author.name)
    if db_author:
        raise HTTPException(status_code=400, detail="Author already registered")
    return create_author(db, author)
