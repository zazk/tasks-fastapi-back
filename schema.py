from pydantic import BaseModel, Field
from models import KindEnum

class TaskSchema(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=500)
    status: bool = Field(default=True)
    typeTask: str = Field(default=KindEnum.active)
    class Config:  
        use_enum_values = True