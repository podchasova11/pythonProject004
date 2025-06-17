from http import HTTPStatus
import pytest
import requests
from models.app_status import AppStatus


@pytest.fixture
def users_list(app_url):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    return data.get('items', [])


# Вспомогательная функция для выполнения GET-запроса и проверки статуса
def get_and_check_response(url, params=None):
    response = requests.get(url, params=params)
    assert response.status_code == HTTPStatus.OK
    return response.json()


# Smoke тест для эндпоинта /status
def test_status_endpoint(app_url):
    url = f"{app_url}/status/"
    data = get_and_check_response(url)
    assert data == {'users': True}
    assert 'users' in data
    AppStatus.model_validate(data)


# Тест на недоступность методов POST, PUT, DELETE, PATCH для эндпоинта /status
@pytest.mark.parametrize("method", ["post", "put", "delete", "patch"])
def test_status_invalid_methods(app_url, method):
    url = f"{app_url}/status/"
    response = getattr(requests, method)(url)
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
  
