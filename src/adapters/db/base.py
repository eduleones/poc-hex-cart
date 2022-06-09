from src.adapters.db.serializers import JsonSerializer
from src.cross.settings import settings
from src.domain.entities.cart import Cart
from src.domain.ports.output.cart_repository import CartRepositoryInterface


class BaseCartRepository(CartRepositoryInterface):
    serializer = JsonSerializer()

    def __init__(self, db: int):
        self.db = db
        self.client = self.create_client()

    def create_client(self):
        pass

    def get_by_id(self, cart_id: str) -> Cart:
        raw = self.client.get(cart_id)
        if not raw:
            return None

        _cart = self.serializer.loads(raw)
        return Cart(**_cart)

    def save(self, cart: Cart) -> bool:
        _ttl = settings.CART_TTL
        _key = str(cart.id)
        _obj = self.serializer.dumps(cart.dict())

        return self.client.set(_key, _obj, ex=_ttl)

    def delete(self, cart_id: str) -> bool:
        return self.client.delete(cart_id)
