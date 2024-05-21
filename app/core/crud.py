from sqlalchemy.orm import Session
from app.core.models import Author, Blog, Category, Tag, User, AuthorCreate, BlogCreate, CategoryCreate, TagCreate, UserCreate
from app.core.security import get_password_hash, verify_password

def get_author(db: Session, name: str):
    return db.query(Author).filter(Author.name == name).first()

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_blog(db: Session, title: str):
    return db.query(Blog).filter(Blog.title == title).first()

def create_blog(db: Session, blog: BlogCreate, user_id: int):
    db_blog = Blog(
        title=blog.title,
        content=blog.content,
        author_id=user_id,
        category_id=blog.category_id,
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    for tag_id in blog.tag_ids:
        tag = db.query(Tag).get(tag_id)
        if tag:
            db_blog.tags.append(tag)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_category(db: Session, name: str):
    return db.query(Category).filter(Category.name == name).first()

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_tag(db: Session, name: str):
    return db.query(Tag).filter(Tag.name == name).first()

def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# def get_user_blogs_w_p(db: Session, user_id: int):
#     return db.query(Blog).filter(Blog.author_id == user_id).all()

def get_user_blogs(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Blog).filter(Blog.author_id == user_id).offset(skip).limit(limit).all()


def update_blog(db: Session, blog_id: int, blog: BlogCreate):
    db_blog = db.query(Blog).get(blog_id)
    if db_blog:
        db_blog.title = blog.title
        db_blog.content = blog.content
        db_blog.category_id = blog.category_id
        db_blog.tags = []
        for tag_id in blog.tag_ids:
            tag = db.query(Tag).get(tag_id)
            if tag:
                db_blog.tags.append(tag)
        db.commit()
        db.refresh(db_blog)
    return db_blog

def delete_blog(db: Session, blog_id: int):
    db_blog = db.query(Blog).get(blog_id)
    if db_blog:
        db.delete(db_blog)
        db.commit()
