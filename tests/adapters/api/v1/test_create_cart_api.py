from http import HTTPStatus

import pytest

pytestmark = pytest.mark.anyio


async def test_create_reseller_cart_api(
    async_client,
    create_reseller_cart_payload,
):
    response = await async_client.post(
        "/v1/carts", json=create_reseller_cart_payload
    )

    response_json = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert response_json["channel"] == create_reseller_cart_payload["channel"]
    assert (
        response_json["cart_type"] == create_reseller_cart_payload["cart_type"]
    )


async def test_create_customer_cart_api(
    async_client,
    create_customer_cart_payload,
):

    response = await async_client.post(
        "/v1/carts", json=create_customer_cart_payload
    )

    response_json = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert response_json["channel"] == create_customer_cart_payload["channel"]
    assert (
        response_json["cart_type"] == create_customer_cart_payload["cart_type"]
    )
