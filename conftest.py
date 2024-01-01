import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# @pytest.fixture(autouse=True)
# def browser(request):
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     request.cls.driver = driver
#     yield # Ваш тест
#     driver.quit()

@pytest.fixture()
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username_field = driver.find_element("xpath", "//input[@name='username']")
    password_field = driver.find_element("xpath", "//input[@name='password']")
    submit_button = driver.find_element("xpath", "//*[@type='submit']")

    username_field.send_keys("admin")
    password_field.send_keys("admin123")
    submit_button.click()
    

    yield driver
    driver.quit()