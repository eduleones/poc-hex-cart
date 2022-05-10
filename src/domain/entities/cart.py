from typing import List
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field

from src.cross.enums import CartStatusEnum, CartTypeEnum, ChannelEnum
from src.domain.value_objects.item import Item


class Cart(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)

    channel: ChannelEnum = ChannelEnum.APP
    status: CartStatusEnum = CartStatusEnum.OPEN
    cart_type: CartTypeEnum = CartTypeEnum.RESELLER

    items: List[Item] = []

    @property
    def total_amount(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
