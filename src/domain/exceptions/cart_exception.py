from .base import DomainException


class CartNotFoundException(DomainException):
    pass


class CartGenericError(DomainException):
    ...
