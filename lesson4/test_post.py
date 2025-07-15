import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class TestDependens:
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

    def test_post_to_buzz(driver):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
        
    # Здесь выполняются действия для выкладывания поста

        assert "post_success" in driver.page_source

    @pytest.mark.dependency(depends=["test_post_to_buzz"])
    def test_delete_post(driver):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
        
    # Здесь выполняются действия для удаления поста

        assert "post_deleted" in driver.page_source
####

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestFormRegistration:

    def setup(self):
        print("Выполняюсь до теста")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    @pytest.mark.parametrize("username, password", [
        ("admin", "admin123"),
        ("admin123", "admin")
        ]
    )

    def test_login(driver, username, password):
        username_field = driver.find_element("xpath", "//input[@name='username']")
        password_field = driver.find_element("xpath", "//input[@name='password']")
        submit_button = driver.find_element("xpath", "//*[@type='submit']")

        username_field.clear()
        username_field.send_keys(username)

        password_field.clear()
        password_field.send_keys(password)

        submit_button.click()
        
            def teardown(self):
        self.driver.quit()
        print("Выполняюсь после всего теста")

        

