from typing import Dict, Type

from src.cross.enums import CartErrorEnum
from src.domain.exceptions import CartGenericError
from src.domain.exceptions.inventory_expection import (
    InventoryNotFoundException,
)
from src.domain.exceptions.product_exception import ProductNotFoundException

ErrorMap: Dict[CartErrorEnum, Type[Exception]] = {
    CartErrorEnum.CART_GENERIC_ERROR: CartGenericError,
    CartErrorEnum.CART_ITEM_NOT_FOUND: ProductNotFoundException,
    CartErrorEnum.CART_ITEM_OUT_OF_STOCK: InventoryNotFoundException,
}
