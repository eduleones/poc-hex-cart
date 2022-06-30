from typing import Optional

from pydantic import BaseModel

from src.cross.enums import CartErrorEnum


class ErrorDTO(BaseModel):
    message: str
    error: CartErrorEnum


class BaseResultDTO(BaseModel):
    is_success: bool = True
    error: Optional[ErrorDTO] = None
