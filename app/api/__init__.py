from fastapi import APIRouter
from . import authors, blogs, categories, tags, users

api_router = APIRouter()
api_router.include_router(authors.router, prefix="/authors", tags=["authors"])
api_router.include_router(blogs.router, prefix="/blogs", tags=["blogs"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(tags.router, prefix="/tags", tags=["tags"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
