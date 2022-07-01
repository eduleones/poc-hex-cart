from typing import List

from pydantic import BaseModel

from src.domain.entities.cart import Cart


class ItemResponsePresenter(BaseModel):
    sku: str
    quantity: int
    price: float


class CartResponsePresenter(BaseModel):
    id: str
    status: str
    channel: str
    cart_type: str
    total_amount: float
    items: List[ItemResponsePresenter] = []

    @classmethod
    def build_from_entity(cls, cart: Cart) -> dict:
        cart_response = cls(
            id=str(cart.id),
            channel=cart.channel,
            status=cart.status,
            cart_type=cart.cart_type,
            total_amount=cart.total_amount,
        )
        if cart.items:
            cart_response.items = [
                ItemResponsePresenter(
                    sku=item.sku, quantity=item.quantity, price=item.price
                )
                for item in cart.items
            ]

        return cart_response.dict()
