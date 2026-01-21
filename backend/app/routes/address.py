from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.controllers.address import (
    create_address,
    delete_address,
    get_address,
    list_addresses,
    update_address,
)
from app.core.database import get_db
from app.schemas.address import AddressCreate, AddressRead, AddressUpdate

router = APIRouter(prefix="/addresses", tags=["Endereco"])


@router.post("/", response_model=AddressRead, status_code=status.HTTP_201_CREATED)
def create(payload: AddressCreate, db: Session = Depends(get_db)):
    return create_address(db, payload)


@router.get("/{address_id}", response_model=AddressRead)
def read(address_id: int, db: Session = Depends(get_db)):
    address = get_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Endereco nao encontrado")
    return address


@router.get("/", response_model=list[AddressRead])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return list_addresses(db, skip=skip, limit=limit)


@router.put("/{address_id}", response_model=AddressRead)
def update(address_id: int, payload: AddressUpdate, db: Session = Depends(get_db)):
    address = get_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Endereco nao encontrado")
    return update_address(db, address, payload)


@router.delete("/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(address_id: int, db: Session = Depends(get_db)):
    address = get_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Endereco nao encontrado")
    delete_address(db, address)
    return None
