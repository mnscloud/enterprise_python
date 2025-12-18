from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4

class User(BaseModel):
    id: UUID = uuid4()
    email: EmailStr
    is_active: bool = True
    
    class Config:
        from_attributes = True