from src.domain.entities.cart import Cart
from src.domain.ports.input.create_cart_service import ICreateCartService


class CreateCartService(ICreateCartService):
    def create(self, cart: Cart) -> Cart:
        self.cart_repository.save(cart)
        return cart
