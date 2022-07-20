from abc import ABC, abstractmethod

from src.domain.entities import Cart


class CartRepositoryInterface(ABC):
    @abstractmethod
    def get_by_id(self, cart_id: str) -> Cart:
        ...

    @abstractmethod
    def save(self, cart: Cart) -> bool:
        ...

    @abstractmethod
    def delete(self, cart_id: str) -> bool:
        ...
