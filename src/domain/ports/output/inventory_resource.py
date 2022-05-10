from abc import ABC, abstractmethod


class IInventoryResource(ABC):
    @abstractmethod
    def get_stock_by_sku(self, sku: str) -> int:
        ...
