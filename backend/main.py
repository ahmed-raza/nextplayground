from fastapi import FastAPI
from api import router as api_router
from db.base import Base
from db.connection import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(api_router, prefix="/api")
