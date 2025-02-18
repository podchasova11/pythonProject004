
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

