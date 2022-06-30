from src.adapters.dto.base import ErrorDTO
from src.adapters.dto.inventory_dto import InventoryDTO, InventoryResultDTO
from src.cross.enums import CartErrorEnum
from src.domain.ports.output.inventory_resource import (
    InventoryResourceInterface,
)


class MockResellerStockApi(InventoryResourceInterface):
    def get_stock_by_sku(self, sku: str) -> dict:
        result = InventoryResultDTO(
            is_success=True, data=InventoryDTO(sku=sku, quantity=10)
        )

        if sku == "789":
            # Mock error - Invalid Inventory
            result = InventoryResultDTO(
                is_success=False,
                error=ErrorDTO(
                    message="Invalid Inventory",
                    error=CartErrorEnum.CART_ITEM_INVALID_INVENTORY,
                ),
            )
        return result.dict()
