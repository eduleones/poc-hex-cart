from pydantic import BaseModel

from src.cross.enums import CartErrorEnum


class ErrorDTO(BaseModel):
    message: str
    error: CartErrorEnum
