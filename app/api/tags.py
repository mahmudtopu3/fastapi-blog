from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.models import Tag, TagCreate, TagRead
from app.core.crud import create_tag, get_tag

router = APIRouter()

@router.post("/", response_model=TagRead)
def create_tag_endpoint(tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = get_tag(db, tag.name)
    if db_tag:
        raise HTTPException(status_code=400, detail="Tag already exists")
    return create_tag(db, tag)

@router.get("/{tag_id}", response_model=TagRead)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = db.query(Tag).get(tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

@router.get("/", response_model=list[TagRead])
def read_tags(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tags = db.query(Tag).offset(skip).limit(limit).all()
    return tags
