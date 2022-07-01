import logging

from src.domain.entities.cart import Cart
from src.domain.ports.dtos import InventoryDto, ProductDto
from src.domain.ports.input.set_item import SetItemInterface

logger = logging.getLogger(__name__)


class BaseSetItemService(SetItemInterface):
    def _get_product(self, sku: str) -> ProductDto:
        result = self.product_resource.search_product_by_sku(sku)
        if result.data:
            return result.data

        result.error.raise_error()

    def _get_stock(self, sku: str) -> InventoryDto:
        result = self.inventory_resource.get_stock_by_sku(sku)
        if result.data:
            return result.data

        result.error.raise_error()

    def set_item(self, cart: Cart, sku: str, quantity: int) -> Cart:
        product = self._get_product(sku)
        stock = self._get_stock(sku)

        cart.set_item(sku, quantity, product, stock)
        self.cart_repository.save(cart)

        return cart
