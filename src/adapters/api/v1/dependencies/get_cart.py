from uuid import UUID

from src.adapters.api.global_exception_handler import GlobalExceptionHandler
from src.adapters.api.v1.dependencies.services import get_cart_service
from src.domain.entities.cart import Cart


async def get_cart_by_id(cart_id: UUID) -> Cart:
    try:
        cart = get_cart_service.get(str(cart_id))
        return cart
    except Exception as error:
        GlobalExceptionHandler.handler_get_cart_exceptions(error, cart_id)
