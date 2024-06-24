from fastapi import APIRouter, HTTPException, status
from backend.schema import PostBase, GenericBase

from typing import Dict

from ..dependencies import db_dependency
from ..models import Post

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
    responses={404: {"description": "Not found"}}, # set a custom json response for 404 error
)


# post routes
@router.post('/store/', status_code=status.HTTP_201_CREATED, response_model=GenericBase)
async def store_post(post: PostBase, db: db_dependency):
    new_post = Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    return {'success': True}
    

@router.get('/show/{post_id}', status_code=status.HTTP_200_OK, response_model=Dict[str, bool | PostBase])
async def show_post(post_id: int, db: db_dependency):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    return {'success': True, 'post': post}


@router.delete('/destroy/{post_id}', status_code=status.HTTP_200_OK, response_model=GenericBase)
async def destroy_post(post_id: int, db: db_dependency):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    db.delete(post)
    db.commit()
    return {'success': True}