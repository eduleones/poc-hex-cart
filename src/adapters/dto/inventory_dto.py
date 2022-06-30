from typing import Optional

from pydantic import BaseModel

from .base import BaseResultDTO, ErrorDTO


class InventoryDTO(BaseModel):
    sku: str
    quantity: Optional[int] = None


class InventoryResultDTO(BaseResultDTO):
    data: Optional[InventoryDTO] = None
