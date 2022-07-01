from abc import ABC, abstractmethod

from src.domain.ports.commom.result import Result
from src.domain.ports.dtos import InventoryDto


class InventoryResourceInterface(ABC):
    @abstractmethod
    def get_stock_by_sku(self, sku: str) -> Result[InventoryDto]:
        ...
