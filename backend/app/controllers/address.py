from sqlalchemy.orm import Session

from app.models.address import Address
from app.schemas.address import AddressCreate, AddressUpdate


def create_address(db: Session, payload: AddressCreate) -> Address:
    address = Address(**payload.dict())
    db.add(address)
    db.commit()
    db.refresh(address)
    return address


def get_address(db: Session, address_id: int) -> Address | None:
    return db.query(Address).filter(Address.id == address_id).first()


def list_addresses(db: Session, skip: int = 0, limit: int = 100) -> list[Address]:
    return db.query(Address).offset(skip).limit(limit).all()


def update_address(db: Session, address: Address, payload: AddressUpdate) -> Address:
    data = payload.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(address, key, value)
    db.commit()
    db.refresh(address)
    return address


def delete_address(db: Session, address: Address) -> None:
    db.delete(address)
    db.commit()
