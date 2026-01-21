from sqlalchemy.orm import Session

from app.models.profile_type import ProfileType
from app.schemas.profile_type import ProfileTypeCreate, ProfileTypeUpdate


def create_profile_type(db: Session, payload: ProfileTypeCreate) -> ProfileType:
    profile_type = ProfileType(**payload.dict())
    db.add(profile_type)
    db.commit()
    db.refresh(profile_type)
    return profile_type


def get_profile_type(db: Session, profile_type_id: int) -> ProfileType | None:
    return db.query(ProfileType).filter(ProfileType.id == profile_type_id).first()


def list_profile_types(db: Session, skip: int = 0, limit: int = 100) -> list[ProfileType]:
    return db.query(ProfileType).offset(skip).limit(limit).all()


def update_profile_type(
    db: Session, profile_type: ProfileType, payload: ProfileTypeUpdate
) -> ProfileType:
    data = payload.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(profile_type, key, value)
    db.commit()
    db.refresh(profile_type)
    return profile_type


def delete_profile_type(db: Session, profile_type: ProfileType) -> None:
    db.delete(profile_type)
    db.commit()
