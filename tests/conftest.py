import pytest
from api_client.base_client import BaseClient


BASE_URL = "https://jsonplaceholder.typicode.com/"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def api_client(base_url):
    client = BaseClient(base_url=base_url)
    return client
