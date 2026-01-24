from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ValidationInfo
from typing import Optional

class ConvoCreate(BaseModel):
    name : str
    user_id: UUID

    @ValidationInfo("name")
    @classmethod
    def not_empty(cls, text: str, info: ValidationInfo):
        if not text.strip():
            raise ValueError(f"{info.field_name} must not be empty")
        return text
    
class ConvoRead(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    created_at: datetime

class ConvoPatch(BaseModel):
    name: Optional[str] = None