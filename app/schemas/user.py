from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationInfo
from enum import Enum
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)     # bcrypt byte limit 72

class UserRead(BaseModel):
    id: UUID
    email: EmailStr
    created_at: datetime

class UserPatch(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
