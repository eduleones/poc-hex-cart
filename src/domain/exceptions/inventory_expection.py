from .base import BaseException


class InventoryNotFoundException(BaseException):
    pass


class OutOfStockException(BaseException):
    pass
