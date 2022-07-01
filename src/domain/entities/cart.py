from typing import List
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field

from src.cross.enums import CartStatusEnum, CartTypeEnum, ChannelEnum
from src.domain.exceptions.inventory_expection import OutOfStockException
from src.domain.ports.dtos import InventoryDto, ProductDto
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

    def set_item(
        self,
        sku: str,
        quantity: int,
        product_dto: ProductDto,
        stock_dto: InventoryDto,
    ):
        if quantity > stock_dto.quantity:
            raise OutOfStockException

        self.items.append(
            Item(
                sku=sku,
                name=product_dto.name,
                description=product_dto.description,
                quantity=quantity,
                price=product_dto.price,
            )
        )
