from datetime import datetime
from typing import List, Optional
from fastapi_pagination import paginate, Page
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import vacation as crud
from app.schemas.military_unit import MilitaryUnitRead
from app.schemas.CustomParams import CustomParams
from app.schemas import vacation as schema
from app.api import deps
from app.schemas.user import UserReadResponse


router = APIRouter()


@router.post("/user/{user_id}", response_model=schema.VacationResponse)
async def create_vacation(
    user_id: int,
    vacation: schema.VacationCreate = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_user),
):
    if not current_user.success:
        return schema.VacationResponse(success=False, message=current_user.message)

    return crud.create_vacation(db, user_id, vacation)


@router.get("/user/{user_id}", response_model=Page[schema.VacationRead])
async def get_vacations(
    user_id: int, params: CustomParams = Depends(), db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_active_user)
):
    if not current_user.success:
        return list()

    return paginate(crud.get_vacations(db, user_id=user_id), params)


@router.get("/unit/", response_model=Page[schema.VacationRead])
async def get_vacations_from_unit(
    params: CustomParams = Depends(), db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_active_admin)
):
    if not current_user.success:
        return list()

    return paginate(crud.get_vacations(db, unit_id=current_user.military_unit), params)


@router.get("/name/", response_model=List[MilitaryUnitRead])
def get_unit_names_from_user(
    access_time: datetime,
    affiliation: Optional[int] = None,
    rank: Optional[int] = None,
    name: Optional[str] = None,
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_admin),
):
    if not current_user.success:
        return list()

    return crud.get_unit_names_from_user(db, access_time=access_time, affiliation=affiliation, rank=rank, name=name)


@router.put("/approval/{vacation_id}", response_model=schema.VacationResponse)
async def update_vacation_approval(
    vacation_id: int,
    is_approved: schema.VacationUpdateApproval = Body(),
    db: Session = Depends(deps.get_db),
    current_user: UserReadResponse = Depends(deps.get_current_active_admin),
):
    if not current_user.success:
        return schema.VacationResponse(success=False, message=current_user.message)

    return crud.update_vacation_approval(db, vacation_id, is_approved)


@router.delete("/{vacation_id}", response_model=schema.VacationResponse)
def delete_vacation(vacation_id: int, db: Session = Depends(deps.get_db), current_user: UserReadResponse = Depends(deps.get_current_active_user)):
    if not current_user.success:
        return schema.VacationResponse(success=False, message=current_user.message)

    return crud.delete_vacation(db, vacation_id)
