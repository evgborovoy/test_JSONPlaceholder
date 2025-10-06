from api_client.base_client import BaseClient
from models.post_models import CreatePostRequest
import requests


class PostsClient:
    ENDPOINT = "/posts"

    def __init__(self, base_client: BaseClient):
        self.client = base_client

    def get_all_posts(self) -> requests.Response:
        """GET /posts"""
        return self.client.get(self.ENDPOINT)

    def get_post_by_id(self, post_id: int) -> requests.Response:
        """GET /posts/{id}"""
        path = f"{self.ENDPOINT}/{post_id}"
        return self.client.get(path)

    def create_post(self, title: str, body: str, user_id: int = 1) -> requests.Response:
        """POST /posts"""
        post_data = CreatePostRequest(title=title, body=body, user_id=user_id)

        return self.client.post(
            path=self.ENDPOINT,
            json=post_data.to_dict()
        )

    def update_post(self, post_id: int, title: str, body: str, user_id: int) -> requests.Response:
        """PUT /posts/{id}"""
        path = f"{self.ENDPOINT}/{post_id}"
        update_data = {
            "id": post_id,  # JSONPlaceholder required ID in body
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self.client.put(path, json=update_data)

    def delete_post(self, post_id: int) -> requests.Response:
        """DELETE /posts/{id}"""
        path = f"{self.ENDPOINT}/{post_id}"
        return self.client.delete(path)
