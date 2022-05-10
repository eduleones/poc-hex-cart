from src.adapters.api.v1.dto.create_cart_dto import CreateCartDTO
from src.cross.containers import RepositoryContainer
from src.cross.enums import CartTypeEnum, ChannelEnum
from src.domain.entities.cart import Cart
from src.domain.services.create_cart import CreateCartService

cart_repository = RepositoryContainer.mock_cart_repository()


def make_cart(
    channel: ChannelEnum = ChannelEnum.APP,
    cart_type: CartTypeEnum = CartTypeEnum.RESELLER,
) -> Cart:
    cart_dto = CreateCartDTO(channel=channel, cart_type=cart_type)
    return CreateCartService(cart_repository).create(cart_dto.to_cart())
