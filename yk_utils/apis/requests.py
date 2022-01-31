"""HTTP requests module.
"""
import requests
from yk_utils.apis import BaseUrl, Key, YoonikApiException


def request(method, url, data=None, json=None, headers=None, params=None):
    # pylint: disable=too-many-arguments
    """ Universal interface for request."""
    url = BaseUrl.get() + url

    # Setup the headers with default Content-Type and Subscription Key.
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    api_key = Key.get()
    if api_key:
        headers['x-api-key'] = api_key

    response = requests.request(
        method,
        url,
        params=params,
        data=data,
        json=json,
        headers=headers)

    if not response.ok:
        raise YoonikApiException(response.status_code, response.text)

    return response.json() if response.text else {}