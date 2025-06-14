from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from core.config import JWT_SECRET, JWT_ALGORITHM

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")

@router.get("/settings")
def get_settings(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")
        return {"msg": f"Settings for user {user_id}"}
    except jwt.PyJWTError:
        raise HTTPException(status_code=403, detail="Invalid token")
