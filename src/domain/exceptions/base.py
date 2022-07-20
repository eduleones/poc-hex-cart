from typing import Optional

from src.cross.enums import CartErrorEnum


class DomainException(Exception):
    def __init__(
        self,
        error_code: CartErrorEnum = CartErrorEnum.CART_GENERIC_ERROR,
        message: str = "An unhandled error ocurred.",
    ):
        self.error_code = error_code
        self.message = message
