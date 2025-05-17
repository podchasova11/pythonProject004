
    @allure.step('Checking that The Desktop "Trading page: is opened')
    def assert_desktop_trading_page(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        platform_overview_btn_link = d.current_url
        if platform_overview_btn_link == "https://capital.com/":
            assert False, \
                ('Bug#029. '
                 'Expected result: The Desktop Trading page is opened '
                 '\n'
                 'Actual result: The Home page is opened ')
        else:
            print(f"{datetime.now()}   =>There is no bug")
            
            
