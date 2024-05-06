from typing import List, Union
from pydantic import BaseModel, Field
from models import KindEnum


class UserSchema(BaseModel):
    username: str = Field(min_length=3)
    email: str = Field(min_length=3)
    fullname: str = Field(min_length=3)
    password: str = Field(min_length=3)
    token: str = Field(min_length=3)
    status: bool = Field(default=True)
    class Config:  
        from_attributes = True

class TaskSchema(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=500)
    status: bool = Field(default=True)
    typeTask: str = Field(default=KindEnum.active)
    user_id: int
    user: Union[UserSchema, None] = None

    class Config:  
        use_enum_values = True
        from_attributes = True
