from abc import ABCMeta, abstractmethod

from src.domain.entities.cart import Cart
from src.domain.ports.output.cart_repository import CartRepositoryInterface
from src.domain.ports.output.inventory_resource import (
    InventoryResourceInterface,
)
from src.domain.ports.output.product_resource import ProductResourceInterface


class SetItemInterface(metaclass=ABCMeta):
    def __init__(
        self,
        cart_repository: CartRepositoryInterface,
        inventory_resource: InventoryResourceInterface,
        product_resource: ProductResourceInterface,
    ):
        self.cart_repository = cart_repository
        self.inventory_resource = inventory_resource
        self.product_resource = product_resource

    @abstractmethod
    def set_item(self, cart: Cart, sku: str, quantity: int) -> Cart:
        ...
