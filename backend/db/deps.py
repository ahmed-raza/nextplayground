from sqlalchemy.orm import Session
from db.connection import SessionLocal
from typing import Generator

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
