from abc import ABC, abstractmethod

from src.domain.ports.commom.result import Result
from src.domain.ports.dtos import ProductDto


class ProductResourceInterface(ABC):
    @abstractmethod
    def search_product_by_sku(self, sku: str) -> Result[ProductDto]:
        ...
