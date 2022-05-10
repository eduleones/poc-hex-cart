from typing import Optional

from pydantic import BaseModel

from .error_dto import ErrorDTO


class InventoryDTO(BaseModel):
    sku: str
    quantity: Optional[int] = None
    resource_error: Optional[ErrorDTO] = None
