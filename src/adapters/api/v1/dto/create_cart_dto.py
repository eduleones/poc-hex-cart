from pydantic import BaseModel

from src.cross.enums import CartTypeEnum, ChannelEnum
from src.domain.entities.cart import Cart


class CreateCartDTO(BaseModel):
    channel: ChannelEnum
    cart_type: CartTypeEnum

    def to_cart(self) -> Cart:
        return Cart(
            channel=self.channel,
            cart_type=self.cart_type,
        )
