from pydantic import BaseModel, Field


class AddressBase(BaseModel):
    cep: str = Field(..., example="01310-200")
    estado: str = Field(..., example="SP")
    bairro: str = Field(..., example="Bela Vista")
    tipo_logradouro: str = Field(..., example="Avenida")
    logradouro: str = Field(..., example="Paulista")
    numero: str = Field(..., example="1000")
    complemento: str | None = Field(default=None, example="Apto 101")
    referencia: str | None = Field(default=None, example="Proximo ao MASP")


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    cep: str | None = Field(default=None, example="01310-200")
    estado: str | None = Field(default=None, example="SP")
    bairro: str | None = Field(default=None, example="Bela Vista")
    tipo_logradouro: str | None = Field(default=None, example="Avenida")
    logradouro: str | None = Field(default=None, example="Paulista")
    numero: str | None = Field(default=None, example="1000")
    complemento: str | None = Field(default=None, example="Apto 101")
    referencia: str | None = Field(default=None, example="Proximo ao MASP")


class AddressRead(AddressBase):
    id: int

    class Config:
        from_attributes = True
