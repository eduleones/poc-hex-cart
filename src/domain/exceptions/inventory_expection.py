from .base import DomainException


class InventoryNotFoundException(DomainException):
    pass


class OutOfStockException(DomainException):
    pass
