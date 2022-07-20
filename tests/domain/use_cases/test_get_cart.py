import uuid

import pytest

from src.domain.entities import Cart
from src.domain.exceptions.cart_exception import CartNotFoundException


def test_get_cart_use_case(get_cart_use_case, reseller_cart):
    cart = get_cart_use_case.get(cart_id=str(reseller_cart.id))

    assert isinstance(cart, Cart)


def test_fail_get_cart_not_found(get_cart_use_case):

    with pytest.raises(CartNotFoundException):
        get_cart_use_case.get(cart_id=str(uuid.uuid4()))
