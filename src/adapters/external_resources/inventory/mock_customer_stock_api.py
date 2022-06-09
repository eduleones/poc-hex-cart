from src.adapters.dto.error_dto import ErrorDTO
from src.adapters.dto.inventory_dto import InventoryDTO
from src.cross.enums import CartErrorEnum
from src.domain.ports.output.inventory_resource import (
    InventoryResourceInterface,
)


class MockCustomerStockApi(InventoryResourceInterface):
    def get_stock_by_sku(self, sku: str) -> dict:

        inventory = InventoryDTO(sku=sku, quantity=2)

        if sku == "789":
            # Mock error - Invalid Inventory
            error = ErrorDTO(
                message="Invalid Inventory",
                error=CartErrorEnum.CART_ITEM_INVALID_INVENTORY,
            )
            inventory = InventoryDTO(sku=sku, resource_error=error)

        return inventory.dict()
