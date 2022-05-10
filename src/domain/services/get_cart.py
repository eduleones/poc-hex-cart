from src.domain.entities.cart import Cart
from src.domain.exceptions.cart_exception import CartNotFoundException
from src.domain.ports.input.get_cart_service import IGetCartService


class GetCartService(IGetCartService):
    def get(self, cart_id: str) -> Cart:
        cart = self.cart_repository.get_by_id(cart_id)
        if not cart:
            raise CartNotFoundException()

        return cart
