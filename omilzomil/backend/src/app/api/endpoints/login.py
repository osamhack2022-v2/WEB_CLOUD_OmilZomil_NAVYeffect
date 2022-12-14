from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.user import UserReadResponse
from app.schemas.token import TokenResponse
from app.crud import token as crud


router = APIRouter()


@router.post("/access-token/", response_model=TokenResponse)
async def login_access_token(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    return crud.create_token(db, form_data.username, form_data.password)


@router.post("/test-token/", response_model=UserReadResponse)
async def test_token(current_user: UserReadResponse = Depends(deps.get_current_active_user)):
    if not current_user.success:
        return UserReadResponse(success=False, message=current_user.message)

    return current_user
