from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка опций для Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Запуск в фоновом режиме (без GUI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Создание экземпляра драйвера
driver = webdriver.Chrome(service=Service(), options=chrome_options)

try:
    # Открытие страницы (замените на нужный URL)
    url = "https://example.com"  # Здесь укажите URL, где находится элемент с классом alert
    driver.get(url)

    # Добавление задержки для полноты загрузки страницы (если необходимо)
    time.sleep(2)  # Замените на подходящее значение или используйте явное ожидание

    # Ожидание появления элемента с классом .alert
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

    # 1. Найти элемент через CSS-селектор
    element_css = driver.find_element(By.CSS_SELECTOR, ".alert")
    print(f"Найден элемент через CSS-селектор: {element_css.text}")

    # 2. Найти элемент через XPath
    element_xpath = driver.find_element(By.XPATH, "//*[@class='alert']")
    print(f"Найден элемент через XPath: {element_xpath.text}")

    # 3. Найти элемент через класс
    element_class = driver.find_element(By.CLASS_NAME, "alert")
    print(f"Найден элемент через класс: {element_class.text}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()
#
