from src.domain.entities.cart import Cart
from src.domain.exceptions.cart_exception import CartNotFoundException
from src.domain.ports.input.get_cart import GetCartInterface


class GetCartService(GetCartInterface):
    def get(self, cart_id: str) -> Cart:
        cart = self.cart_repository.get_by_id(cart_id)
        if not cart:
            raise CartNotFoundException()

        return cart
