    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        print(f"\n{datetime.now()}   2. Start Act. Click on the link ('Offices in four continents')")
        self.driver.find_element(*LINK_OFFICES_IN_FOUR_COUNTRY_LOCATOR).click()
        print(f"\n{datetime.now()}   Link ('Offices in four continents') is clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Check message 'Access denied Error 16' on the opened page")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check message 'Access denied Error 16' on the opened page")

        # Check presenting 'ar-ae/about-us/our-offices' in url on the opened page
        print(f"{datetime.now()}   IS 'ar-ae/about-us/our-offices' in url on the opened page?")

        if 'ar-ae/about-us/our-offices' not in self.driver.current_url:
            msg = f"Opened page have message 'Access denied Error 16', url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        else:
            msg = f"Need to check content of opened page, url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        return True
    
