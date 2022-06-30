from typing import Optional

from pydantic import BaseModel

from src.adapters.dto.base import ErrorDTO


class ProductDTO(BaseModel):
    sku: str
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    resource_error: Optional[ErrorDTO] = None
