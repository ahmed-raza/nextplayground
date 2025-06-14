from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from db.deps import get_db
from models.user import User
from core.security import hash_password
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.auth.signup import SignUpRequest

router = APIRouter()

@router.post("/signup")
def signup(payload: SignUpRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        name=payload.name,
        email=payload.email,
        password=hash_password(payload.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully"}
