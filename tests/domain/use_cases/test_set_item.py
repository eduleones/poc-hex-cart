import pytest

from src.domain.entities import Cart
from src.domain.exceptions import (
    InventoryNotFoundException,
    OutOfStockException,
    ProductNotFoundException,
)
from src.domain.value_objects.item import Item


def test_reseller_set_item_service(reseller_set_item_use_case, reseller_cart):

    cart = reseller_set_item_use_case.set_item(
        cart=reseller_cart, sku="123", quantity=1
    )

    assert isinstance(cart, Cart)
    assert isinstance(cart.items[0], Item)


def test_customer_set_item_service(customer_set_item_use_case, customer_cart):

    cart = customer_set_item_use_case.set_item(
        cart=customer_cart, sku="123", quantity=1
    )

    assert isinstance(cart, Cart)
    assert isinstance(cart.items[0], Item)


def test_fail_set_item_out_of_stock(customer_set_item_use_case, reseller_cart):

    with pytest.raises(OutOfStockException):
        customer_set_item_use_case.set_item(
            cart=reseller_cart, sku="123", quantity=1000
        )


def test_fail_set_item_product_not_found(
    customer_set_item_use_case, reseller_cart
):

    with pytest.raises(ProductNotFoundException):
        customer_set_item_use_case.set_item(
            cart=reseller_cart, sku="78910", quantity=1
        )


def test_fail_set_item_invalid_inventory(
    customer_set_item_use_case, reseller_cart
):

    with pytest.raises(InventoryNotFoundException):
        customer_set_item_use_case.set_item(
            cart=reseller_cart, sku="789", quantity=1
        )
