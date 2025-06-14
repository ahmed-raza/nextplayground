from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserSettingsUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Ahmed")
    email: Optional[EmailStr] = Field(None, example="ahmed@example.com")
    password: Optional[str] = Field(None, example="newpassword123")
