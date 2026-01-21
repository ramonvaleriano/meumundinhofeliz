from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.controllers.profile_type import (
    create_profile_type,
    delete_profile_type,
    get_profile_type,
    list_profile_types,
    update_profile_type,
)
from app.core.database import get_db
from app.schemas.profile_type import ProfileTypeCreate, ProfileTypeRead, ProfileTypeUpdate

router = APIRouter(prefix="/profile-types", tags=["Perfil"])


@router.post("/", response_model=ProfileTypeRead, status_code=status.HTTP_201_CREATED)
def create(payload: ProfileTypeCreate, db: Session = Depends(get_db)):
    return create_profile_type(db, payload)


@router.get("/{profile_type_id}", response_model=ProfileTypeRead)
def read(profile_type_id: int, db: Session = Depends(get_db)):
    profile_type = get_profile_type(db, profile_type_id)
    if not profile_type:
        raise HTTPException(status_code=404, detail="Perfil nao encontrado")
    return profile_type


@router.get("/", response_model=list[ProfileTypeRead])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return list_profile_types(db, skip=skip, limit=limit)


@router.put("/{profile_type_id}", response_model=ProfileTypeRead)
def update(profile_type_id: int, payload: ProfileTypeUpdate, db: Session = Depends(get_db)):
    profile_type = get_profile_type(db, profile_type_id)
    if not profile_type:
        raise HTTPException(status_code=404, detail="Perfil nao encontrado")
    return update_profile_type(db, profile_type, payload)


@router.delete("/{profile_type_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(profile_type_id: int, db: Session = Depends(get_db)):
    profile_type = get_profile_type(db, profile_type_id)
    if not profile_type:
        raise HTTPException(status_code=404, detail="Perfil nao encontrado")
    delete_profile_type(db, profile_type)
    return None
