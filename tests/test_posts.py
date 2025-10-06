import allure
import json
from datetime import datetime
from models.post_models import PostModel


@allure.epic("API regression testing")
@allure.feature("Posts CRUD operations")
class TestPosts:

    @allure.story("GET /posts - Get All")
    @allure.title("Checking receive all posts")
    def test_get_all_products(self, posts_client):
        with allure.step("GET request to receive all posts"):
            response = posts_client.get_all_posts()

        with allure.step("Check status code"):
            assert response.status_code == 200, f"Expect 200, actual: {response.status_code}"

        response_data = response.json()

        with allure.step("Validate pydantic scheme"):
            assert isinstance(response_data, list), "Response body must be a list"
            if response_data:
                PostModel.model_validate(response_data[0])

            assert len(response_data) >= 100, "The list must contain at least 100 posts"

        allure.attach(
            json.dumps(response_data[:2], indent=2, ensure_ascii=False),
            name="Response Body (first 2 items)",
            attachment_type=allure.attachment_type.JSON
        )

    @allure.story("POST /posts - Create Resource")
    @allure.title("Checking the creation of new post")
    def test_create_new_post(self, posts_client):
        timestamp = datetime.now().strftime('%H%M%S%f')
        test_title = f"New Post Title {timestamp}"
        test_body = f"Body content for test {timestamp}"

        with allure.step("Send POST request for post creation"):
            response = posts_client.create_post(test_title, test_body)

        with allure.step("Checking HTTP status code"):
            assert response.status_code == 201, f"Expect 201, actual: {response.status_code}"

        response_data = response.json()

        with allure.step("Pydantic schema validation"):
            created_post = PostModel.model_validate(response_data)

            # JSONPlaceholder return ID = 101 for new post
            assert created_post.id == 101, "ID of new post must be 101"
            assert created_post.title == test_title

    @allure.story("GET /posts/{id} - Get by ID")
    @allure.title("Checking receipt of post by ID")
    def test_get_post_by_id(self, posts_client, created_post: int):
        post_id = created_post  # ID from fixture (id=101)

        with allure.step(f"GET request for id: {post_id}"):
            response = posts_client.get_post_by_id(post_id)

        with allure.step("Check HTTP status code"):
            assert response.status_code == 200, f"Expect 200, actual: {response.status_code}"

        response_data = response.json()

        with allure.step("Schema validation"):
            found_post = PostModel.model_validate(response_data)
            assert found_post.id == post_id

    @allure.story("PUT /posts/{id} - Update Resource")
    @allure.title("Checking for a full post update")
    def test_update_post(self, posts_client, created_post: int):
        post_id = created_post
        new_title = f"UPDATED Title {datetime.now().strftime('%H%M%S%f')}"

        with allure.step(f"Send PUT request for ID: {post_id}"):
            response = posts_client.update_post(post_id, new_title, "Updated Body", user_id=1)

        with allure.step("Checking HTTP status code"):
            assert response.status_code == 200, f"Expect 200, actual {response.status_code}"

        response_data = response.json()

        with allure.step("Validate pydantic schema"):
            updated_post = PostModel.model_validate(response_data)
            assert updated_post.title == new_title
            assert updated_post.id == post_id

    @allure.story("DELETE /posts/{id} - Delete Resource")
    @allure.title("Checking post deletion")
    def test_delete_post(self, posts_client, created_post: int):
        post_id = created_post

        with allure.step(f"Send DELETE request for id: {post_id}"):
            delete_response = posts_client.delete_post(post_id)

        with allure.step("Check HTTP status code"):
            assert delete_response.status_code == 200, f"Expect 200, actual {delete_response.status_code}"
