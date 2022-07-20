from uuid import UUID


def test_create_reseller_cart_use_case(
    create_reseller_cart_presenter, create_cart_use_case
):
    cart = create_cart_use_case.create(
        create_reseller_cart_presenter.to_cart()
    )

    assert isinstance(cart.id, UUID)
    assert cart.channel == create_reseller_cart_presenter.channel
    assert cart.cart_type == create_reseller_cart_presenter.cart_type


def test_create_customer_cart_use_case(
    create_customer_cart_presenter, create_cart_use_case
):
    cart = create_cart_use_case.create(
        create_customer_cart_presenter.to_cart()
    )

    assert isinstance(cart.id, UUID)
    assert cart.channel == create_customer_cart_presenter.channel
    assert cart.cart_type == create_customer_cart_presenter.cart_type
