from sqlalchemy import Column, Integer, String, ForeignKey, Table,Text
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.core.database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)  # Specify length, e.g., 100

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)  # Specify length

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)  # Specify length

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Specify length
    content = Column(Text())  # No length needed for TEXT type fields
    author_id = Column(Integer, ForeignKey("authors.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    author = relationship("Author")
    category = relationship("Category")
    tags = relationship("Tag", secondary="blog_tags")

    blog_tags = Table(
        "blog_tags",
        Base.metadata,
        Column("blog_id", Integer, ForeignKey("blogs.id")),
        Column("tag_id", Integer, ForeignKey("tags.id"))
    )

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(191), unique=True, index=True)  # Adjusted length
    hashed_password = Column(String(255))  # Specify length for hashed password

# Pydantic models for validation and serialization
class AuthorCreate(BaseModel):
    name: str
    class Config:
        orm_mode = True

class AuthorRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class CategoryCreate(BaseModel):
    name: str

class CategoryRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class TagCreate(BaseModel):
    name: str

class TagRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class BlogCreate(BaseModel):
    title: str
    content: str
    author_id: int
    category_id: int
    tag_ids: list[int]

    class Config:
        orm_mode = True

class BlogRead(BaseModel):
    id: int
    title: str
    content: str
    author: AuthorRead
    category: CategoryRead
    tags: list[TagRead]

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: str
    password: str

class UserRead(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
