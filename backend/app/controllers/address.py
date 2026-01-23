from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.address import Address
from app.schemas.address import AddressCreate, AddressUpdate


async def create_address(db: AsyncSession, payload: AddressCreate) -> Address:
    address = Address(**payload.model_dump())
    db.add(address)
    await db.commit()
    await db.refresh(address)
    return address


async def get_address(db: AsyncSession, address_id: int) -> Address | None:
    result = await db.execute(select(Address).where(Address.id == address_id))
    return result.scalar_one_or_none()


async def list_addresses(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> list[Address]:
    result = await db.execute(select(Address).offset(skip).limit(limit))
    return list(result.scalars().all())


async def update_address(
    db: AsyncSession, address: Address, payload: AddressUpdate
) -> Address:
    data = payload.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(address, key, value)
    await db.commit()
    await db.refresh(address)
    return address


async def delete_address(db: AsyncSession, address: Address) -> None:
    await db.delete(address)
    await db.commit()
