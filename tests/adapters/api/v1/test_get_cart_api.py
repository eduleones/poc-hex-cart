import uuid
from http import HTTPStatus

import pytest

pytestmark = pytest.mark.anyio


async def test_get_cart_api(
    reseller_cart,
    async_client,
):

    response = await async_client.get(f"/v1/carts/{reseller_cart.id}")

    response_json = response.json()

    assert response.status_code == HTTPStatus.OK
    assert response_json["id"] == str(reseller_cart.id)


async def test_fail_get_cart_not_found(
    async_client,
):
    cart_id = uuid.uuid4()

    response = await async_client.get(f"/v1/carts/{cart_id}")

    assert response.status_code == HTTPStatus.NOT_FOUND
