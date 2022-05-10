import logging
from http import HTTPStatus
from uuid import UUID

from fastapi.exceptions import HTTPException

from src.domain.exceptions.cart_exception import CartNotFoundException
from src.domain.exceptions.inventory_expection import (
    InventoryNotFoundException,
    OutOfStockException,
)
from src.domain.exceptions.product_exception import ProductNotFoundException

logger = logging.getLogger(__name__)


class GlobalExceptionHandler:
    def handler_get_cart_exceptions(error, cart_id: UUID):
        errors = (
            (
                CartNotFoundException,
                HTTPStatus.NOT_FOUND,
                f"Cart {cart_id} not found",
            ),
        )

        for exception, error_response, detail in errors:
            if isinstance(error, exception):
                logger.error(
                    detail,
                    extra=dict(
                        event="get_cart",
                        event_error=exception,
                        cart_id=cart_id,
                    ),
                )
                raise HTTPException(status_code=error_response, detail=detail)

    def handler_set_item_exceptions(error, cart_id: str, sku: str):
        errors = (
            (
                InventoryNotFoundException,
                HTTPStatus.INTERNAL_SERVER_ERROR,
                "Inventory is not accessible",
            ),
            (
                OutOfStockException,
                HTTPStatus.BAD_REQUEST,
                f"Sku {sku} out of stock",
            ),
            (
                ProductNotFoundException,
                HTTPStatus.NOT_FOUND,
                f"Sku {sku} not found",
            ),
        )

        for exception, error_response, detail in errors:
            if isinstance(error, exception):
                logger.error(
                    detail,
                    extra=dict(
                        event="set_item",
                        event_error=exception,
                        cart_id=cart_id,
                        sku=sku,
                    ),
                )
                raise HTTPException(status_code=error_response, detail=detail)
