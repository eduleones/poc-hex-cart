import uuid

import pytest

from src.domain.entities.cart import Cart
from src.domain.exceptions.cart_exception import CartNotFoundException
from src.domain.services.get_cart import GetCartService


def test_get_cart_service(cart_repository_service, reseller_cart):

    cart = GetCartService(cart_repository_service).get(
        cart_id=str(reseller_cart.id)
    )

    assert isinstance(cart, Cart)


def test_fail_get_cart_not_found(cart_repository_service):

    with pytest.raises(CartNotFoundException):
        GetCartService(cart_repository_service).get(cart_id=str(uuid.uuid4()))
