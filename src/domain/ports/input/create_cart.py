from abc import ABCMeta, abstractmethod

from src.domain.entities.cart import Cart
from src.domain.ports.output.cart_repository import CartRepositoryInterface


class CreateCartInterface(metaclass=ABCMeta):
    def __init__(self, cart_repository: CartRepositoryInterface):
        self.cart_repository = cart_repository

    @abstractmethod
    def create(self, cart) -> Cart:
        ...