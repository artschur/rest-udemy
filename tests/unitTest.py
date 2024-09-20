import pytest
import requests

# Base URL for your Flask app running in Docker
baseurl = "http://192.168.15.14:5005"


@pytest.fixture(scope="module")
def client():
    """
    Fixture to set up an HTTP session client using the requests library.
    """
    with requests.Session() as client:
        yield client  # Yield the client for use in tests


@pytest.fixture(scope="module")
def first_store(client):
    """
    Fetch the first store from the store endpoint.
    """
    response = client.get(baseurl + "/store")
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list), "Response should be a list of stores"
    assert len(response_data) > 0, "The store list should not be empty"

    return response_data[0]  # Return the first store


def test_get_storeby_id(client, first_store):
    # Extract the store ID from the first store fixture
    store_id = first_store['id']
    response = client.get(f'{baseurl}/store/{store_id}/items')
    response_data = response.json()

    # Debug print with clear formatting
    print(f"Store ID: {store_id}, Items: {response_data}")
    assert response.status_code == 200
    assert isinstance(response_data, list), "Response should be a list of items"


def test_add_item_to_store(client, first_store):
    storeId = first_store["id"]
    url = f"{baseurl}/store/{storeId}/items"

    item_data = {
       "item": {
           "name": "testing this item!",
           "price": 6
       }
    }

    response = client.post(url, json=item_data)

    assert response.status_code == 200

    assert storeId in response.text

