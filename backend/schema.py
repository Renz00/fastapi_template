from pydantic import BaseModel

# data validation using pydantic, similar to typescript interface
class PostBase(BaseModel):
    title: str
    content: str
    user_id: int
    

class UserBase(BaseModel):
    username: str
    

class GenericBase(BaseModel):
    success: bool