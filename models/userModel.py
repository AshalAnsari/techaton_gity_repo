from pydantic import BaseModel, Field
from typing import Optional

class userBase(BaseModel):
    fullname: str
    email: str

class userCreate(userBase):
    pass 

class userUpdate(BaseModel):
    fullname: Optional[str] = Field(None, example="John Doe")
    email: Optional[str] = Field(None, example="john@example.com")

class userSchema(userBase):
    id: str = Field(None, example="507f1f77bcf86cd799439011")

class userDelete(BaseModel):
    message: str
