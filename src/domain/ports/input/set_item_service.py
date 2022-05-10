from abc import ABCMeta, abstractmethod

from src.domain.entities.cart import Cart
from src.domain.ports.output.cart_repository import ICartRepository
from src.domain.ports.output.inventory_resource import IInventoryResource
from src.domain.ports.output.product_resource import IProductResource


class ISetItemService(metaclass=ABCMeta):
    def __init__(
        self,
        cart_repository: ICartRepository,
        inventory_resource: IInventoryResource,
        product_resource: IProductResource,
    ):
        self.cart_repository = cart_repository
        self.inventory_resource = inventory_resource
        self.product_resource = product_resource

    @abstractmethod
    def set_item(self, cart: Cart, sku: str, quantity: int) -> Cart:
        ...
