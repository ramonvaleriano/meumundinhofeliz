from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

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
async def create(payload: AddressCreate, db: AsyncSession = Depends(get_db)):
    return await create_address(db, payload)


@router.get("/{address_id}", response_model=AddressRead)
async def read(address_id: int, db: AsyncSession = Depends(get_db)):
    address = await get_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Endereco nao encontrado")
    return address


@router.get("/", response_model=list[AddressRead])
async def list_all(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    return await list_addresses(db, skip=skip, limit=limit)


@router.put("/{address_id}", response_model=AddressRead)
async def update(
    address_id: int, payload: AddressUpdate, db: AsyncSession = Depends(get_db)
):
    address = await get_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Endereco nao encontrado")
    return await update_address(db, address, payload)


@router.delete("/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(address_id: int, db: AsyncSession = Depends(get_db)):
    address = await get_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Endereco nao encontrado")
    await delete_address(db, address)
    return None
