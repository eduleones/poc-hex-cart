from src.domain.entities import Cart
from src.domain.exceptions.cart_exception import CartNotFoundException
from src.domain.ports.input.get_cart import GetCartInterface


class GetCartUseCase(GetCartInterface):
    def get(self, cart_id: str) -> Cart:
        cart = self.cart_repository.get_by_id(cart_id)
        if not cart:
            raise CartNotFoundException()

        return cart
