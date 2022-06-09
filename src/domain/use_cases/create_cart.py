from src.domain.entities.cart import Cart
from src.domain.ports.input.create_cart import CreateCartInterface


class CreateCartService(CreateCartInterface):
    def create(self, cart: Cart) -> Cart:
        self.cart_repository.save(cart)
        return cart
