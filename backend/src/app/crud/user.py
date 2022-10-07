import sqlalchemy.exc
from sqlalchemy.orm import Session
from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdateInformation, UserUpdatePassword, UserUpdateRole


def create_user(db: Session, user: UserCreate):
    try:
        user = User(
            full_name=user.full_name,
            dog_number=user.dog_number,
            affiliation=user.affiliation,
            military_unit=user.military_unit,
            rank=user.rank,
            username=user.username,
            password=get_password_hash(user.password),
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except sqlalchemy.exc.IntegrityError:
        return None


def get_user(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).get(user_id)


def update_user_information(db: Session, user_id: int, information: UserUpdateInformation):
    try:
        res = db.query(User).filter_by(user_id=user_id).update(information.dict())
        db.commit()
    except sqlalchemy.exc.IntegrityError:
        res = None
    return res


def update_user_password(db: Session, user_id: int, password: UserUpdatePassword):
    user = get_user_by_id(user_id)
    if user is not None and verify_password(password.old_password, user.password):
        res = None
    else:
        res = user.update({"password": get_password_hash(password.new_password)})
        db.commit()
    return res


def update_user_role(db: Session, user_id: int, role: UserUpdateRole):
    res = db.query(User).filter_by(user_id=user_id).update(role.dict())
    db.commit()
    return res