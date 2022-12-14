from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.db.base_schema import Response


class InspectionLogBase(BaseModel):
    guardhouse: int = Field(None, description="guardhouse")
    affiliation: int = Field(None, description="affiliation")
    rank: int = Field(None, description="rank")
    name: str = Field(None, description="name")
    uniform: int = Field(None, description="uniform")
    image_path: str = Field(None, description="image path")

    class Config:
        schema_extra = {
            "example": {
                "guardhouse": 1,
                "affiliation": 3,
                "rank": 5,
                "name": "정의철",
                "uniform": 2,
                "image_path": "image_path_url",
            }
        }


class InspectionLogCreate(InspectionLogBase):
    pass


class InspectionLogRead(InspectionLogBase):
    inspection_id: int = Field(None, description="primary key")
    access_time: datetime = Field(None, description="access time")
    military_unit: int = Field(None, description="military unit")
    is_checked: bool = Field(None, description="is_checked")

    class Config:
        schema_extra = {
            "example": {
                "inspection_id": 1,
                "guardhouse": 1,
                "access_time": datetime.now(),
                "affiliation": 3,
                "military_unit": 1,
                "rank": 5,
                "name": "정의철",
                "uniform": 2,
                "image_path": "image_path_url",
                "is_checked": False,
            }
        }
        orm_mode = True


class InspectionLogUpdateInformation(BaseModel):
    affiliation: Optional[int] = Field(None, description="affiliation")
    military_unit: Optional[int] = Field(None, description="military unit")
    rank: Optional[int] = Field(None, description="rank")
    name: Optional[str] = Field(None, description="name")
    uniform: Optional[int] = Field(None, description="uniform")

    class Config:
        schema_extra = {
            "example": {
                "military_unit": 2,
                "name": "정의철",
                "uniform": 2,
            }
        }


class InspectionLogUpdateCheck(BaseModel):
    is_checked: bool = Field(None, description="is_checked")

    class Config:
        schema_extra = {
            "example": {
                "is_checked": True,
            }
        }


class InspectionLogResponse(Response):
    pass
