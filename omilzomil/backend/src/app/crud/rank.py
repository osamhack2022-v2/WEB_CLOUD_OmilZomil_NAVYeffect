from sqlalchemy.orm import Session
from app.models.rank import Rank


def create_rank(db: Session, rank_id: int, rank: str):
    rank = Rank(rank_id=rank_id, rank=rank)
    db.add(rank)
    db.commit()
    db.refresh(rank)
    return rank


def get_ranks(db: Session):
    return db.query(Rank).filter(Rank.rank_id != 1).order_by(Rank.rank_id).all()
