from src.cross.enums import CartErrorEnum
from src.domain.ports.commom.result import BaseError, Result
from src.domain.ports.dtos import InventoryDto
from src.domain.ports.output.inventory_resource import (
    InventoryResourceInterface,
)


class MockResellerStockApi(InventoryResourceInterface):
    def get_stock_by_sku(self, sku: str) -> Result[InventoryDto]:
        result = Result[InventoryDto](data=InventoryDto(sku=sku, quantity=10))

        if sku == "789":
            result.error = BaseError(
                CartErrorEnum.CART_ITEM_OUT_OF_STOCK,
                message=f"Sku {sku} not found on Costumers Stock API",
            )
            result.data = None

        return result
