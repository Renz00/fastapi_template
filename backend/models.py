from sqlalchemy import Boolean, Column, Integer, String
from .db import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True)
    
    
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(String(200))
    user_id = Column(Integer)