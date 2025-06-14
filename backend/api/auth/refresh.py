from fastapi import APIRouter, HTTPException
from core.security import decode_token, create_access_token

router = APIRouter()

@router.post("/refresh-token")
def refresh_token(refresh_token: str):
    try:
        payload = decode_token(refresh_token)
        user_id = payload.get("sub")
        new_access_token = create_access_token({"sub": user_id})
        return {"access_token": new_access_token}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
