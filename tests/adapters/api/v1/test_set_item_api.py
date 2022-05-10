from http import HTTPStatus

import pytest

pytestmark = pytest.mark.anyio


async def test_set_item_reseller_cart_api(
    reseller_cart,
    async_client,
):

    sku = "123"
    response = await async_client.put(
        f"v1/carts/{reseller_cart.id}/items/{sku}",
        json={"quantity": 1},
    )

    response_json = response.json()

    assert response.status_code == HTTPStatus.OK
    assert response_json["id"] == str(reseller_cart.id)
    assert response_json["items"][0]["sku"] == sku


async def test_set_item_customer_cart_api(
    customer_cart,
    async_client,
):

    sku = "3434"
    response = await async_client.put(
        f"v1/carts/{customer_cart.id}/items/{sku}",
        json={"quantity": 1},
    )

    response_json = response.json()

    assert response.status_code == HTTPStatus.OK
    assert response_json["id"] == str(customer_cart.id)
    assert response_json["items"][0]["sku"] == sku


async def test_fail_out_stock_in_set_item_customer_cart_api(
    customer_cart,
    async_client,
):

    sku = "3434"
    response = await async_client.put(
        f"v1/carts/{customer_cart.id}/items/{sku}",
        json={"quantity": 10000},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST


async def test_fail_product_not_found_in_set_item_customer_cart_api(
    customer_cart,
    async_client,
):

    sku = "78910"
    response = await async_client.put(
        f"v1/carts/{customer_cart.id}/items/{sku}",
        json={"quantity": 1},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
