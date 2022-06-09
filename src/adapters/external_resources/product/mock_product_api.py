from src.adapters.dto.error_dto import ErrorDTO
from src.adapters.dto.product_dto import ProductDTO
from src.cross.enums import CartErrorEnum
from src.domain.ports.output.product_resource import ProductResourceInterface


class MockProductApi(ProductResourceInterface):
    def search_product_by_sku(self, sku: str) -> dict:
        product = ProductDTO(
            sku="123",
            name="Product 1",
            description="Product 1 description",
            price=10.0,
        )

        if sku == "78910":
            # Mock error - Product not found
            error = ErrorDTO(
                message="Product not found",
                error=CartErrorEnum.CART_ITEM_NOT_FOUND,
            )
            product = ProductDTO(sku=sku, resource_error=error)

        return product.dict()
