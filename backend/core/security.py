from datetime import datetime, timedelta
import jwt
from core.config import JWT_SECRET, JWT_ALGORITHM

def create_access_token(data: dict, expires_minutes=15):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)

def create_refresh_token(data: dict, expires_minutes=60*24*7):  # 7 days
    return create_access_token(data, expires_minutes=expires_minutes)

def decode_token(token: str):
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
