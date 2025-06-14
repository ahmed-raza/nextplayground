from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "mydatabase.db"
SQLITE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(SQLITE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
