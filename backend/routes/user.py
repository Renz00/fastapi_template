from fastapi import APIRouter, HTTPException, status
from backend.schema import UserBase

from ..dependencies import db_dependency
from ..models import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


# user routes
@router.post('/store/', status_code=status.HTTP_201_CREATED)
async def store_user(user: UserBase, db: db_dependency):
    # serialize user model into dict using pydantic basemodel
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    return {'success': True}
    

@router.get('/show/{user_id}', status_code=status.HTTP_200_OK)
async def show_user(user_id: int, db: db_dependency):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return {'success': True, 'user': user}