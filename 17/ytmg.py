from http import HTTPStatus
import pytest
import requests
from models.user import User
from tests.test_smoke import get_and_check_response


# Вспомогательная функция для проверки полей пользователя
def check_user_fields(user):
    assert 'id' in user
    assert 'email' in user
    assert 'first_name' in user
    assert 'last_name' in user
    assert 'avatar' in user


@pytest.mark.parametrize("page, size", [
    (1, 5),  # Первая страница, 5 пользователей на странице
    (2, 5),  # Вторая страница, 5 пользователей на странице
    (1, 10),  # Первая страница, 10 пользователей на странице
    (3, 4),  # Третья страница, 4 пользователя на странице
])
def test_users_with_pagination(app_url, page, size):
    url = f"{app_url}/api/users/"
    data = get_and_check_response(url, {"page": page, "size": size})
    assert 'total' in data
    assert 'items' in data
    # Проверка количества пользователей на странице
    assert len(data["items"]) == size
    for user in data["items"]:
        check_user_fields(user)


# Тест на разные данные при разных значениях page
@pytest.mark.parametrize("page1, page2, size", [
    (1, 2, 5),
    (2, 3, 5),
    (1, 2, 10),
])
def test_users_different_pages(app_url, page1, page2, size):
    url = f"{app_url}/api/users/"
    data1 = get_and_check_response(url, {"page": page1, "size": size})
    data2 = get_and_check_response(url, {"page": page2, "size": size})
    items1 = data1.get('items', [])
    items2 = data2.get('items', [])
    assert items1 != items2


# Тест для проверки уникальности данных
def test_users_no_duplicates(app_url):
    url = f"{app_url}/api/users/"
    data = get_and_check_response(url)
    users_list = data.get('items', [])
    users_ids = [user["id"] for user in users_list]
    assert len(users_ids) == len(set(users_ids))


# Дополнительный тест для проверки количества страниц с параметризацией size
@pytest.mark.parametrize("size", [5, 10, 20])
def test_total_pages(app_url, size):
    url = f"{app_url}/api/users/"
    data = get_and_check_response(url)
    total = data['total']
    expected_pages = (total + size - 1) // size  # Округление вверх
    data = get_and_check_response(url, {"size": size})
    data_pages = data.get('pages', 0)
    assert data_pages == expected_pages


# Тест на соответствие response модели pydantic
@pytest.mark.parametrize("user_id", [1, 6, 12])
def test_user(app_url, user_id):
    url = f"{app_url}/api/users/{user_id}"
    data = get_and_check_response(url)
    User.model_validate(data)


# Проверка на несуществующего пользователя
@pytest.mark.parametrize("user_id", [13])
def test_user_nonexistent_values(app_url, user_id):
    url = f"{app_url}/api/users/{user_id}"
    response = requests.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND


# Проверка на некорректный ввод user_id
@pytest.mark.parametrize("user_id", [-1, 0, "fafaf"])
def test_user_invalid_values(app_url, user_id):
    url = f"{app_url}/api/users/{user_id}"
    response = requests.get(url)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
