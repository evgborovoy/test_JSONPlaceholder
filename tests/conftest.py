import pytest
from datetime import datetime
from api_client.base_client import BaseClient
from api_client.clients.posts_client import PostsClient

BASE_URL = "https://jsonplaceholder.typicode.com/"
POSTS_ENDPOINT = "/posts"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def api_client(base_url):
    client = BaseClient(base_url=base_url)
    return client


@pytest.fixture(scope="class")
def posts_client(api_client):
    return PostsClient(api_client)


@pytest.fixture(scope="function")
def created_post(api_client):
    posts_client = PostsClient(api_client)

    timestamp = datetime.now().strftime('%H%M%S%f')
    title = f"Test Post for CRUD {timestamp}"
    body = "Test body content"
    user_id = 1

    response = posts_client.create_post(title, body, user_id)

    # jsonplaceholder always return 201 and id=101 for POST
    if response.status_code != 201:
        pytest.fail(f"Failed to create post for setup. Status: {response.status_code}")

    post_id = response.json().get('id')

    yield post_id

    # simulating DELETE
    delete_response = posts_client.delete_post(post_id)

    if delete_response.status_code == 200:
        api_client.logger.info(f"Cleanup: Successfully 'deleted' post ID: {post_id} (Status 200)")
    else:
        api_client.logger.error(
            f"Cleanup: Failed to 'delete' post ID: {post_id}. Status: {delete_response.status_code}")
