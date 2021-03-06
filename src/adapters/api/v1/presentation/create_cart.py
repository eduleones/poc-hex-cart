from pydantic import BaseModel

from src.cross.enums import CartTypeEnum, ChannelEnum
from src.domain.entities import Cart


class CreateCartPresenter(BaseModel):
    channel: ChannelEnum
    cart_type: CartTypeEnum

    def to_cart(self) -> Cart:
        return Cart(
            channel=self.channel,
            cart_type=self.cart_type,
        )
