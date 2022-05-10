from abc import ABC, abstractmethod


class IProductResource(ABC):
    @abstractmethod
    def search_product_by_sku(self, sku: str) -> int:
        ...
