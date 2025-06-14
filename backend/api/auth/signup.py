from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.connection import SessionLocal
from models.user import User
from core.security import hash_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(name: str, email: str, password: str, db: Session = Depends(get_db)):
    if db.query(User).filter_by(email=email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(name=name, email=email, password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "User created", "user_id": user.id}
