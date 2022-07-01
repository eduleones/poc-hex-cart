from typing import Optional

from pydantic import BaseModel


class InventoryDto(BaseModel):
    sku: str
    quantity: int


class ProductDto(BaseModel):
    sku: str
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
