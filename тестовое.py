# Задание 1:
# Используя Selenium и DevTools, напишите тест, который:
# •	Открывает страницу (сайт можно выбрать самостоятельно);
# •	Использует DevTools для получения консольных ошибок (если таковые имеются);
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Настройка опций для Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# Создание экземпляра драйвера
driver = webdriver.Chrome(service=Service(), options=chrome_options)
try:
    # Открытие страницы Vikunja
    url = "https://try.vikunja.io"
    driver.get(url)
    # Печать HTML-кода страницы для отладки
    print(driver.page_source)
    # Ожидание, пока элемент будет доступен
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'head > title'))) 
    # Получение логов консоли
    logs = driver.get_log('browser')
    # Вывод консольных ошибок
    errors = [log for log in logs if log['level'] == 'SEVERE']
    if errors:
        print("Консольные ошибки:")
        for error in errors:
            print(f"Время: {error['timestamp']}, Сообщение: {error['message']}")
    else:
        print("Консольные ошибки отсутствуют.")
finally:
    # Закрытие браузера
    driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Настройка опций для Chrome
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Запуск в фоновом режиме (без GUI)
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
#
# # Создание экземпляра драйвера
# driver = webdriver.Chrome(service=Service(), options=chrome_options)
#
# try:
#     # Открытие страницы (замените на нужный URL)
#     url = "https://example.com"  # Здесь укажите URL, где находится элемент с классом alert
#     driver.get(url)
#
#     # Добавление задержки для полноты загрузки страницы (если необходимо)
#     time.sleep(2)  # Замените на подходящее значение или используйте явное ожидание
#
#     # Ожидание появления элемента с классом .alert
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))
#
#     # 1. Найти элемент через CSS-селектор
#     element_css = driver.find_element(By.CSS_SELECTOR, ".alert")
#     print(f"Найден элемент через CSS-селектор: {element_css.text}")
#
#     # 2. Найти элемент через XPath
#     element_xpath = driver.find_element(By.XPATH, "//*[@class='alert']")
#     print(f"Найден элемент через XPath: {element_xpath.text}")
#
#     # 3. Найти элемент через класс
#     element_class = driver.find_element(By.CLASS_NAME, "alert")
#     print(f"Найден элемент через класс: {element_class.text}")
#
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
#
# finally:
#     # Закрытие браузера
#     driver.quit()
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

FIRST_PRODUCT = (By.CSS_SELECTOR, "#catalog_section_list > div.item.product.sku.productDC.productDC-602272.product-coxo > div")
BUTTON_CLICK = (By.CSS_SELECTOR, "#smallElementTools > div > div.mainTool > div.columnRowWrap > div > a")


def test_add_to_cart():
    """Тест для проверки добавления товара в корзину на сайте Coxo."""

    # Настройка WebDriver для автоматизации браузера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)  # Установка неявного ожидания

    try:
        # 1. Перейти на сайт интернет-магазина
        driver.get("https://www.coxo.ru/")

        # 2. Принять куки, если возникает такое окно
        try:
            wait = WebDriverWait(driver, 5)
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='UseCookieBtn']")))
            accept_cookies_button.click()
        except Exception as e:
            print("Кнопка принятия куки не найдена или не доступна:", e)

        # 3. Перейти в раздел каталога «Бытовая техника» //*[@id="catalogMenuHeading"]

        try:
            # Явное ожидание для элемента
            wait = WebDriverWait(driver, 5)  # Увеличиваем время ожидания до 5 секунд
            category_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='catalogMenuHeading']")))
            category_button.click()
        except Exception as e:
            print("Не удалось перейти в раздел 'Бытовая техника':", e)
        try:
            # Явное ожидание для элемента
            wait = WebDriverWait(driver, 10)  # Увеличиваем время ожидания до 10 секунд
            category_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leftMenu']/li[4]/a/span/span[2]")))
            category_button.click()
        except Exception as e:
            print("Не удалось перейти в раздел 'Бытовая техника':", e)

        # Check presenting link
        if len(driver.find_elements(*FIRST_PRODUCT)) == 0:
            msg = f"The  block don't have link [FIRST_PRODUCT] in DOM"
            print(f"{datetime.now()}   => {msg}")
        print(f"{datetime.now()}   The  block "
              f" have link [FIRST_PRODUCT] in DOM\n")

        # Scroll to the link
        driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            driver.find_elements(*FIRST_PRODUCT)[0])

        # driver.find_element(*FIRST_PRODUCT).click()
        # print(f"\n{datetime.now()}   Link is clicked\n")

        # 4. Добавить первый товар из списка в корзину
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 ".productDC-602272.product-coxo .productTable div.productColImage a")))  # Ожидание видимости первого товара
        first_product = driver.find_elements(
            By.CSS_SELECTOR, ".productDC-602272.product-coxo .productTable div.productColImage a")[0]
        product_name = first_product.text  # Получение названия товара
        product_price = driver.find_elements(
            By.CSS_SELECTOR, "#b4194ec9982fad9d59127e9a4b5ff3bf_price > div.priceBlock")[0].text  # Получение цены товара

        # Кликаем по кнопке «В корзину»
        first_product.click()
        # Scroll to the link
        # driver.execute_script(
        #     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #     driver.find_elements(*BUTTON_CLICK)[0])
        button_click = driver.find_elements(
            By.CSS_SELECTOR, "#smallElementTools > div > div.mainTool > div.columnRowWrap > div > a")[0]
        button_click.click()

        # driver.find_element(*BUTTON_CLICK).click()

        # 5. Перейти на страницу корзины
        driver.get("https://www.coxo.ru/cart")  # URL страницы корзины

        # 6. Убедиться, что добавленный товар присутствует в корзине
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#catalog_section_list > div.item.product.sku.productDC.productDC-602272.product-coxo > div")))  # Ожидание видимости элементов корзины

        # Проверка названия товара в корзине
        cart_product_name = driver.find_element(By.CSS_SELECTOR, "#catalog_section_list > div.item.product.sku.productDC.productDC-602272.product-coxo > div").text
        assert product_name in cart_product_name, "Добавленный товар отсутствует в корзине или название некорректно."

        # Проверка цены товара в корзине
        cart_product_price = driver.find_element(
            By.CSS_SELECTOR, "//*[@id='1cf681852018492c79ebf36bf8f93b9a_price']/div[2]/a/span[1]/span").text
        assert product_price in cart_product_price, "Цена товара в корзине некорректна."

    finally:
        # Закрытие браузера после выполнения теста
        driver.quit()


if __name__ == "__main__":
    test_add_to_cart()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Настройка опций для Chrome
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Запуск в фоновом режиме (без GUI)
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
#
# # Создание экземпляра драйвера
# driver = webdriver.Chrome(service=Service(), options=chrome_options)
#
# try:
#     # Открытие страницы (замените на нужный URL)
#     url = "https://example.com"  # Здесь укажите URL, где находится элемент с классом alert
#     driver.get(url)
#
#     # Добавление задержки для полноты загрузки страницы (если необходимо)
#     time.sleep(2)  # Замените на подходящее значение или используйте явное ожидание
#
#     # Ожидание появления элемента с классом .alert
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))
#
#     # 1. Найти элемент через CSS-селектор
#     element_css = driver.find_element(By.CSS_SELECTOR, ".alert")
#     print(f"Найден элемент через CSS-селектор: {element_css.text}")
#
#     # 2. Найти элемент через XPath
#     element_xpath = driver.find_element(By.XPATH, "//*[@class='alert']")
#     print(f"Найден элемент через XPath: {element_xpath.text}")
#
#     # 3. Найти элемент через класс
#     element_class = driver.find_element(By.CLASS_NAME, "alert")
#     print(f"Найден элемент через класс: {element_class.text}")
#
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
#
# finally:
#     # Закрытие браузера
#     driver.quit()
#
# Задание 1:
# Используя Selenium и DevTools, напишите тест, который:
# •	Открывает страницу (сайт можно выбрать самостоятельно);
# •	Использует DevTools для получения консольных ошибок (если таковые имеются);
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # Настройка опций для Chrome
# chrome_options = Options()
# # chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# # Создание экземпляра драйвера
# driver = webdriver.Chrome(service=Service(), options=chrome_options)
# try:
#     # Открытие страницы Vikunja
#     url = "https://try.vikunja.io"
#     driver.get(url)
#     # Печать HTML-кода страницы для отладки
#     print(driver.page_source)
#     # Ожидание, пока элемент будет доступен
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'head > title')))
#     # Получение логов консоли
#     logs = driver.get_log('browser')
#     # Вывод консольных ошибок
#     errors = [log for log in logs if log['level'] == 'SEVERE']
#     if errors:
#         print("Консольные ошибки:")
#         for error in errors:
#             print(f"Время: {error['timestamp']}, Сообщение: {error['message']}")
#     else:
#         print("Консольные ошибки отсутствуют.")
# finally:
#     # Закрытие браузера
#     driver.quit()
# Задание 2:
# Напишите тест на Python с использованием библиотеки requests, который проверяет,
#  что при отправке POST-запроса на конечную точку /orders с корректными данными:
# •	Ответ должен быть с кодом 201 (Created);
# •	В теле ответа должен быть возвращен ID нового заказа;
# •	Если отправлены некорректные данные (например, недопустимый product_id), API должен вернуть ошибку с кодом 400 (Неверный запрос).
#
# import requests
# import pytest
#
# # Замените на свой базовый URL API
# BASE_URL = "https://try.vikunja.io"
#
#
# def test_create_order_success():
#     """Тест успешного создания заказа с корректными данными."""
#     endpoint = f"{BASE_URL}/orders"
#     valid_data = {
#         "product_id": 1,  # допустимый product_id
#         "quantity": 2
#     }
#
#     response = requests.post(endpoint, json=valid_data)
#
#     # Проверка кода ответа
#     assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"
#
#     # Проверка в теле ответа
#     response_data = response.json()
#     assert "id" in response_data, "Response should contain 'id'"
#     assert isinstance(response_data["id"], int), "'id' should be an integer"
#
#
# def test_create_order_invalid_product_id():
#     """Тест на обработку некорректного product_id при создании заказа."""
#     endpoint = f"{BASE_URL}/orders"
#     invalid_data = {
#         "product_id": 9999,  # явно некорректный product_id
#         "quantity": 2
#     }
#
#     response = requests.post(endpoint, json=invalid_data)
#
#     # Логирование ответа для отладки
#     print("Response Status Code:", response.status_code)
#     print("Response Body:", response.text)
#
#     # Проверка кода ответа
#     assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"
#
#     # Проверка сообщения об ошибке (если доступно)
#     response_data = response.json()
#     assert "error" in response_data, "Response should contain an 'error' message"
#
#
# if __name__ == "__main__":
#     pytest.main()


# Задание 3:
# Напишите автотест на Python и Selenium, который проверяет, что на странице (сайт можно выбрать самостоятельно
# с формой регистрации):
# •	Кнопка с текстом "Войти (в зависимости как её назвали на выбранном сайте, например Sign On тд)" видна;
# •	После нажатия кнопки «Войти» пользователь переходит на страницу входа (URL должен измениться на сайт,
# который выбрали).

#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
#
# @pytest.fixture(scope="class")
# def browser():
#     """Фикстура для настройки WebDriver."""
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture(scope="class", params=["demo"])
# def cur_login(request):
#     """Фикстура для логина."""
#     print(f"Current login - {request.param}")
#     return request.param
#
#
# @pytest.fixture(scope="class", params=["demo"])
# def cur_password(request):
#     """Фикстура для пароля."""
#     print(f"Current password - {request.param}")
#     return request.param
#
#
# @pytest.mark.usefixtures("browser")
# class TestLoginPage:
#     """Класс для тестирования страницы входа."""
#
#     def test_login_redirect_and_input(self, browser, cur_login, cur_password):
#         """Проверка перехода на страницу входа и ввода логина и пароля."""
#         browser.get("https://try.vikunja.io")
#
#         # Ожидание загрузки страницы входа
#         time.sleep(5)  #
#
#         # Проверка URL после нажатия на кнопку
#         expected_url = "https://try.vikunja.io/login"  # Ожидаемый URL страницы входа
#         assert browser.current_url == expected_url, f"Ожидался URL {expected_url}, но получен {browser.current_url}"
#
#         # Ввод логина и пароля
#         email_input = browser.find_element(By.CSS_SELECTOR, "#username")  # актуальное имя поля ввода для логина
#         password_input = browser.find_element(By.CSS_SELECTOR, "#password")  # актуальное имя поля ввода для пароля
#
#         # Используем send_keys для ввода значений
#         email_input.send_keys(cur_login)
#         password_input.send_keys(cur_password)
#
#         #  можно добавить попытку входа
#         submit_button = browser.find_element(By.XPATH, "//*[@id='loginform']/button")  # актуальный селектор кнопки входа
#         submit_button.click()
#
#         # Проверка, произошел ли вход
#         time.sleep(5)
#         assert "try.vikunja" in browser.current_url, "Не удалось войти: текущий URL не содержит 'dashboard'"
#
#
# if __name__ == "__main__":
#     pytest.main()



# Задание 4:
# Предположим, у вас есть страница с формой регистрации на сайте. Напишите класс PageObject для этой страницы, который включает:
# •	Метод для ввода имени пользователя;
# •	Метод для ввода пароля;
# •	Метод для отправки формы.
#

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
#
# class LoginPage:
#     """Page Object для страницы входа."""
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def enter_username(self, username):
#         """Метод для ввода имени пользователя."""
#         username_input = self.driver.find_element(By.CSS_SELECTOR, "#username")  # Актуальное имя поля ввода для логина
#         username_input.send_keys(username)
#
#     def enter_password(self, password):
#         """Метод для ввода пароля."""
#         password_input = self.driver.find_element(By.CSS_SELECTOR, "#password")  # Актуальное имя поля ввода для пароля
#         password_input.send_keys(password)
#
#     def submit_form(self):
#         """Метод для отправки формы."""
#         submit_button = self.driver.find_element(By.XPATH, "//*[@id='loginform']/button")  # Актуальный селектор кнопки входа
#         submit_button.click()
#
#
# @pytest.fixture(scope="class")
# def browser():
#     """Фикстура для настройки WebDriver."""
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture(scope="class", params=["demo"])
# def cur_login(request):
#     """Фикстура для логина."""
#     print(f"Current login - {request.param}")
#     return request.param
#
#
# @pytest.fixture(scope="class", params=["demo"])
# def cur_password(request):
#     """Фикстура для пароля."""
#     print(f"Current password - {request.param}")
#     return request.param
#
#
# @pytest.mark.usefixtures("browser")
# class TestLoginPage:
#     """Класс для тестирования страницы входа."""
#
#     def test_login_redirect_and_input(self, browser, cur_login, cur_password):
#         """Проверка перехода на страницу входа и ввода логина и пароля."""
#         browser.get("https://try.vikunja.io")
#
#         # Ожидание загрузки страницы
#         time.sleep(5)
#
#         # Проверка URL после нажатия на кнопку
#         expected_url = "https://try.vikunja.io/login"  # Ожидаемый URL страницы входа
#         assert browser.current_url == expected_url, f"Ожидался URL {expected_url}, но получен {browser.current_url}"
#
#         # Создание экземпляра страницы входа
#         login_page = LoginPage(browser)
#
#         # Ввод логина и пароля
#         login_page.enter_username(cur_login)
#         login_page.enter_password(cur_password)
#
#         # Отправка формы
#         login_page.submit_form()
#
#         # Проверка, произошел ли вход
#         time.sleep(5)
#         assert "try.vikunja" in browser.current_url, "Не удалось войти: текущий URL не содержит 'dashboard'"
#
#
# if __name__ == "__main__":
#     pytest.main()
import time
import unittest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

#
# class TestCoxoShopping(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         """Настройка WebDriver для автоматизации браузера."""
#         cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         cls.driver.implicitly_wait(10)  # Установка неявного ожидания
#
#     def test_add_to_cart(self):
#         """Тест для проверки добавления товара в корзину на сайте Coxo."""
#
#         # 1. Перейти на сайт интернет-магазина
#         self.driver.get("https://www.coxo.ru/")
#
#         # 2. Перейти в раздел каталога «Бытовая техника»
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leftMenu']/li[4]/a/span/span[2]"))).click()
#
#         # 3. Добавить первый товар из списка в корзину
#         wait.until(
#             EC.visibility_of_element_located(
#                 (By.CSS_SELECTOR, ".productDC-602272.product-coxo .productTable div.productColImage a")))  # Ожидание видимости первого товара
#         first_product = self.driver.find_elements(
#             By.CSS_SELECTOR, ".productDC-602272.product-coxo .productTable div.productColImage a")[0]
#         product_name = first_product.text  # Получение названия товара
#         product_price = self.driver.find_elements(
#             By.CSS_SELECTOR, "#b4194ec9982fad9d59127e9a4b5ff3bf_price > div.priceBlock")[0].text  # Получение цены товара
#
#         # Кликаем по кнопке «В корзину»
#         first_product.find_element(
#             By.CSS_SELECTOR, "#b4194ec9982fad9d59127e9a4b5ff3bf_price > div.priceBlock > div.wp-buttons > div.wp-basket > a").click()
#
#         # 4. Перейти на страницу корзины
#         self.driver.get("https://www.coxo.ru/cart")  # URL страницы корзины
#
#         # 5. Убедиться, что добавленный товар присутствует в корзине
#         wait.until(EC.visibility_of_element_located(
#             (By.XPATH, "//*[@id='basketProductList']/div[1]/div/div[2]")))  # Ожидание видимости элементов корзины
#
#         # Проверка названия товара в корзине
#         cart_product_name = self.driver.find_element(By.XPATH, "//*[@id='basketProductList']/div[1]/div/div[2]").text
#         self.assertIn(product_name, cart_product_name,
#                       "Добавленный товар отсутствует в корзине или название некорректно.")
#
#         # Проверка цены товара в корзине
#         cart_product_price = self.driver.find_element(
#             By.CSS_SELECTOR, "//*[@id='1cf681852018492c79ebf36bf8f93b9a_price']/div[2]/a/span[1]/span").text
#         self.assertIn(product_price, cart_product_price, "Цена товара в корзине некорректна.")
#
#     @classmethod
#     def tearDownClass(cls):
#         """Закрытие браузера после выполнения тестов."""
#         cls.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()
#
#

# Автоматизировать следующий сценарий:
# 1.	Перейти на сайт интернет-магазина https://www.coxo.ru/.
# 2.	Перейти в раздел каталога «Бытовая техника».
# 3.	Добавить первый товар из списка в корзину.
# 4.	Перейти на страницу корзины.
# 5.	Убедиться, что добавленный товар присутствует в корзине с правильным названием и ценой.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

FIRST_PRODUCT = (By.CSS_SELECTOR, "#catalog_section_list > div.item.product.sku.productDC.productDC-602272.product-coxo > div")


def test_add_to_cart():
    """Тест для проверки добавления товара в корзину на сайте Coxo."""

    # Настройка WebDriver для автоматизации браузера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)  # Установка неявного ожидания

    try:
        # 1. Перейти на сайт интернет-магазина
        driver.get("https://www.coxo.ru/")

        # 2. Принять куки, если возникает такое окно
        try:
            wait = WebDriverWait(driver, 5)
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='UseCookieBtn']")))
            accept_cookies_button.click()
        except Exception as e:
            print("Кнопка принятия куки не найдена или не доступна:", e)

        # 3. Перейти в раздел каталога «Бытовая техника» //*[@id="catalogMenuHeading"]

        try:
            # Явное ожидание для элемента
            wait = WebDriverWait(driver, 5)  # Увеличиваем время ожидания до 5 секунд
            category_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='catalogMenuHeading']")))
            category_button.click()
        except Exception as e:
            print("Не удалось перейти в раздел 'Бытовая техника':", e)
        try:
            # Явное ожидание для элемента
            wait = WebDriverWait(driver, 10)  # Увеличиваем время ожидания до 10 секунд
            category_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leftMenu']/li[4]/a/span/span[2]")))
            category_button.click()
        except Exception as e:
            print("Не удалось перейти в раздел 'Бытовая техника':", e)

        # Check presenting link
        if len(driver.find_elements(*FIRST_PRODUCT)) == 0:
            msg = f"The  block don't have link [FIRST_PRODUCT] in DOM"
            print(f"{datetime.now()}   => {msg}")
        print(f"{datetime.now()}   The  block "
              f" have link [FIRST_PRODUCT] in DOM\n")

        # Scroll to the link
        driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            driver.find_elements(*FIRST_PRODUCT)[0])

        # driver.find_element(*FIRST_PRODUCT).click()
        # print(f"\n{datetime.now()}   Link is clicked\n")

        # 4. Добавить первый товар из списка в корзину
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 ".productDC-602272.product-coxo .productTable div.productColImage a")))  # Ожидание видимости первого товара
        first_product = driver.find_elements(
            By.CSS_SELECTOR, ".productDC-602272.product-coxo .productTable div.productColImage a")[0]
        product_name = first_product.text  # Получение названия товара
        product_price = driver.find_elements(
            By.CSS_SELECTOR, "#b4194ec9982fad9d59127e9a4b5ff3bf_price > div.priceBlock")[0].text  # Получение цены товара

        # Кликаем по кнопке «В корзину»
        first_product.click()
        # Scroll to the link
        driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            driver.find_elements(*FIRST_PRODUCT)[0])
        button_click = driver.find_elements(
            By.CSS_SELECTOR, "#smallElementTools > div > div.mainTool > div.columnRowWrap > div > a")[0]
        button_click.click()

        # 5. Перейти на страницу корзины
        driver.get("https://www.coxo.ru/cart")  # URL страницы корзины

        # 6. Убедиться, что добавленный товар присутствует в корзине
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#catalog_section_list > div.item.product.sku.productDC.productDC-602272.product-coxo > div")))  # Ожидание видимости элементов корзины

        # Проверка названия товара в корзине
        cart_product_name = driver.find_element(By.CSS_SELECTOR, "#catalog_section_list > div.item.product.sku.productDC.productDC-602272.product-coxo > div").text
        assert product_name in cart_product_name, "Добавленный товар отсутствует в корзине или название некорректно."

        # Проверка цены товара в корзине
        cart_product_price = driver.find_element(
            By.CSS_SELECTOR, "//*[@id='1cf681852018492c79ebf36bf8f93b9a_price']/div[2]/a/span[1]/span").text
        assert product_price in cart_product_price, "Цена товара в корзине некорректна."

    finally:
        # Закрытие браузера после выполнения теста
        driver.quit()


if __name__ == "__main__":
    test_add_to_cart()


