from uuid import UUID

from src.adapters.api.v1.dependencies.services import get_cart_service
from src.domain.entities.cart import Cart


async def get_cart_by_id(cart_id: UUID) -> Cart:
    cart = get_cart_service.get(str(cart_id))
    return cart
