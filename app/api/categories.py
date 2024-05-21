from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.models import Category, CategoryCreate, CategoryRead
from app.core.crud import create_category, get_category

router = APIRouter()

@router.post("/", response_model=CategoryRead)
def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = get_category(db, category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return create_category(db, category)

@router.get("/{category_id}", response_model=CategoryRead)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(Category).get(category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.get("/", response_model=list[CategoryRead])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    categories = db.query(Category).offset(skip).limit(limit).all()
    return categories
