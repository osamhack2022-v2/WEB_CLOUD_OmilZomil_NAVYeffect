from sqlalchemy.orm import Session
from app.models.appearance import Appearance


def create_appearance(db: Session, appearance_id: int, appearance: str):
    appearance = Appearance(appearance_id=appearance_id, appearance=appearance)
    db.add(appearance)
    db.commit()
    db.refresh(appearance)
    return appearance


def get_appearances(db: Session):
    return db.query(Appearance).order_by(Appearance.appearance_id).all()
