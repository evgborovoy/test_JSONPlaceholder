import requests
import json
from utils.logger_config import logger


class BaseClient:

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.logger = logger

    def _request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{path}"

        request_body = kwargs.get('json') or kwargs.get('data')

        self.logger.info(f"--- START REQUEST ---")
        self.logger.info(f"Method: {method} | URL: {url}")
        self.logger.debug(f"Headers: {kwargs.get('headers')}")
        self.logger.debug(f"Body: {json.dumps(request_body, indent=2) if request_body else 'None'}")

        try:
            response = requests.request(method, url, **kwargs)

            try:
                response_body = response.json()
            except requests.exceptions.JSONDecodeError:
                response_body = response.text

            self.logger.info(f"Status: {response.status_code} | Time: {response.elapsed.total_seconds():.3f}s")
            self.logger.debug(f"Response Headers: {response.headers.get('Content-Type')}")

            body_log = (json.dumps(response_body, indent=2, ensure_ascii=False)
                        if isinstance(response_body, (dict, list))
                        else str(response_body)[:500] + '...' if len(str(response_body)) > 500 else str(response_body))

            self.logger.debug(f"Response Body: {body_log}")
            self.logger.info(f"--- END REQUEST ---")

            return response

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed for {url}: {e}")
            self.logger.info(f"--- END REQUEST (FAILED) ---")
            raise

    def get(self, path: str, **kwargs) -> requests.Response:
        return self._request('GET', path, **kwargs)

    def post(self, path: str, json: dict = None, **kwargs) -> requests.Response:
        return self._request('POST', path, json=json, **kwargs)

    def put(self, path: str, json: dict = None, **kwargs) -> requests.Response:
        return self._request('PUT', path, json=json, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self._request('DELETE', path, **kwargs)
