    @allure.step(f"{datetime.now()}   3. Start Assert. Check [CFD trading] page is opened in EN "
                 f"language after clicking the link [CFD] ")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check [CFD trading] page is opened in EN"
              f"language after clicking the link [CFD] ")

        # Check presenting 'fr-fr' in url on the opened page
        print(f"{datetime.now()}   IS 'fr-fr' in url on the opened page?")

        if 'fr-fr' not in self.driver.current_url:
            msg = (f"Opened page have URL: {self.driver.current_url},"
                   f" and page opened in EN language")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        else:
            msg = f"Need to check content of opened page, url {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        return True
