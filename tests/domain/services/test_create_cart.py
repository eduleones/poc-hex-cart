from uuid import UUID

from src.domain.services.create_cart import CreateCartService


def test_create_reseller_cart_service(
    create_reseller_cart_dto, cart_repository_service
):
    cart = CreateCartService(cart_repository_service).create(
        create_reseller_cart_dto.to_cart()
    )

    assert isinstance(cart.id, UUID)
    assert cart.channel == create_reseller_cart_dto.channel
    assert cart.cart_type == create_reseller_cart_dto.cart_type


def test_create_customer_cart_service(
    create_customer_cart_dto, cart_repository_service
):
    cart = CreateCartService(cart_repository_service).create(
        create_customer_cart_dto.to_cart()
    )

    assert isinstance(cart.id, UUID)
    assert cart.channel == create_customer_cart_dto.channel
    assert cart.cart_type == create_customer_cart_dto.cart_type
