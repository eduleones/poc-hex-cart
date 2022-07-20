from src.cross.enums import CartErrorEnum
from src.domain.ports.commom.result import BaseError, Result
from src.domain.ports.dtos import InventoryDto
from src.domain.ports.output.inventory_resource import (
    InventoryResourceInterface,
)


class MockCustomerStockApi(InventoryResourceInterface):
    def get_stock_by_sku(self, sku: str) -> Result[InventoryDto]:
        inventory = InventoryDto(sku=sku, quantity=2)
        result = Result[InventoryDto](data=inventory)

        if sku == "789":
            result.error = BaseError(
                error_code=CartErrorEnum.CART_ITEM_OUT_OF_STOCK,
                message=f"Sku {sku} not found on Costumers Stock API",
            )
            result.data = None

        return result
