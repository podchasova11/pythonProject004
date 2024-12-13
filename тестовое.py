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


