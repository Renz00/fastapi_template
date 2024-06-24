from fastapi import FastAPI

from backend.db import engine
from backend.routes import post, user
import backend.models as models

app = FastAPI()

models.Base.metadata.create_all(bind=engine) # initializing db connection and creating tables

app.include_router(user.router)
app.include_router(post.router)