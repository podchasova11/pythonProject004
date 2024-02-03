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
        



