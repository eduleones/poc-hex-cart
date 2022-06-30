import logging

from src.cross.enums import CartErrorEnum
from src.domain.entities.cart import Cart
from src.domain.exceptions import (
    InventoryNotFoundException,
    OutOfStockException,
    ProductNotFoundException,
)
from src.domain.ports.input.set_item import SetItemInterface
from src.domain.value_objects.item import Item

logger = logging.getLogger(__name__)


class BaseSetItemService(SetItemInterface):
    def _exception_resource(self, errors: dict, resource_error: dict):
        error: CartErrorEnum = resource_error["error"]
        exception = errors[error]

        logger.exception(exception)
        raise exception(message=error.value)

    def _validate_product_resource(self, product: dict):
        _mapper = {
            CartErrorEnum.CART_ITEM_NOT_FOUND: ProductNotFoundException,
        }

        resource_error = product.get("resource_error")
        if not resource_error:
            return

        self._exception_resource(_mapper, resource_error)

    def _validate_stock_resource(self, stock: dict):
        _mapper = {
            CartErrorEnum.CART_ITEM_INVALID_INVENTORY: (
                InventoryNotFoundException
            ),
        }

        if stock["is_success"]:
            return

        resource_error = stock.get("error")
        self._exception_resource(_mapper, resource_error)

    def _get_product(self, sku: str):
        product = self.product_resource.search_product_by_sku(sku)
        self._validate_product_resource(product)
        return product

    def _get_stock(self, sku: str) -> dict:
        stock = self.inventory_resource.get_stock_by_sku(sku)
        self._validate_stock_resource(stock)
        return stock

    def _validate_set_item(self, stock, quantity):
        if quantity > stock["data"]["quantity"]:
            raise OutOfStockException

    def set_item(self, cart: Cart, sku: str, quantity: int) -> Cart:
        product = self._get_product(sku)
        stock = self._get_stock(sku)

        self._validate_set_item(stock, quantity)

        item = Item(
            sku=sku,
            name=product.get("name"),
            description=product.get("description"),
            quantity=quantity,
            price=product.get("price"),
        )

        cart.items.append(item)
        self.cart_repository.save(cart)

        return cart
