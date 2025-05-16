import math
from http import HTTPStatus
import pytest
import requests


# Тест общего числа пользователей и размера страницы
@pytest.fixture
def users_list(app_url):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data["total"] == len(data["items"])


# Тест на проверку страницы и размера
@pytest.mark.parametrize("page, size", [
    (1, 12),
    (2, 6),
    (4, 3)
])
def test_page_size(app_url, page, size):
    response = requests.get(f"{app_url}/api/users/", params={"page": page,"size": size})
    data = response.json()
    assert page == data['page']
    assert size == data['size']
    assert len(data["items"]) == size


# Тест на ожидаемое количество страниц
@pytest.mark.parametrize("size", [12, 6, 3])
def test_expected_pages(app_url, size):
    response = requests.get(f"{app_url}/api/users/", params={"size": size})
    data = response.json()
    expected_pages = math.ceil(data['total'] / size)
    assert data['pages'] == expected_pages
