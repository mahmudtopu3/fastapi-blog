from fastapi import FastAPI
from app.api import api_router
from app.api.users import router as users_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)
app.include_router(users_router, prefix="/users", tags=["users"])
