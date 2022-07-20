from src.cross.enums import CartErrorEnum
from src.domain.ports.commom.result import BaseError, Result
from src.domain.ports.dtos import ProductDto
from src.domain.ports.output.product_resource import ProductResourceInterface


class MockProductApi(ProductResourceInterface):
    def search_product_by_sku(self, sku: str) -> Result[ProductDto]:
        product = ProductDto(
            sku="123",
            name="Product 1",
            description="Product 1 description",
            price=10.0,
        )
        result = Result[ProductDto](data=product)

        if sku == "78910":
            result.error = BaseError(
                error_code=CartErrorEnum.CART_ITEM_NOT_FOUND,
                message=f"Sku {sku} not found on Mock Product API",
            )
            result.data = None

        return result
