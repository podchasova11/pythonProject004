    @allure.step(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")

        # Check presenting 'analysis' in url on the opened page
        print(f"{datetime.now()}   IS 'analysis' in url on the opened page?")
        if 'analysis' not in self.driver.current_url:
            msg = f"Opened page have message '404 not found', url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        else:
            msg = f"Need to check content of opened page, url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common.save_current_screenshot(d, f"Need to check content of page, url is: {self.driver.current_url}")
        return True
