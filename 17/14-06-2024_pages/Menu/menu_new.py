# pages/Menu/menu_new.py
    
    @allure.step('Select Way_to_trade menu, Professional submenu, check that footer is displaed')
    def check_that_footer_displayed_on_professional_page(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Way_to_trade" menu, "Professional" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_WAYS_TO_TRADE)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_WAYS_TO_TRADE_PROFESSIONAL)
        self.check_that_footer_is_opened(d, cur_language, self.FOOTER_RISK_WARNING_BLOCK)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
#######################
    @allure.step(f"{datetime.now()}.   Click 'Markets' menu section.")
    def main_menu_move_focus(self, d, test_language, main_menu_locator):

        menu = d.find_elements(*main_menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => Main Menu not present")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
            pytest.skip(f"Main menu not present for '{test_language}' language")
        print(f"{datetime.now()}   => Main menu is present")

        if not self.element_is_visible(main_menu_locator, 5):
            print(f"{datetime.now()}   => Main menu not visible")
            pytest.fail("Main menu not visible")
        print(f"{datetime.now()}   => Main menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*main_menu_locator)  # not Glossary
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        del menu
        print(f"{datetime.now()}   => Markets menu focus moved")
################
    @allure.step(f"{datetime.now()}.   Focus move to 'Markets [Forex]' menu item and click (US_11.01.02).")
    def sub_menu_move_focus_click(self, d, test_language, sub_menu_locator):

        sub_menu = d.find_elements(*sub_menu_locator)
        if len(sub_menu) == 0:
            pytest.skip(f"Sub menu not present for '{test_language}' language")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url
    ##############################    

    @allure.step(f"{datetime.now()}.   Check that Footer is opened on page [Professional]")
    def check_that_footer_is_opened(self, d, test_language, footer_locator):
        """
        Check that Footer is opened on the page [Professional]
        """

        footer = d.find_elements(*footer_locator)
        if len(footer) == 0:
            pytest.fail("Bug #034! The footer is missing on click menu item [Professional] "
                        "of the menu section [Ways to trade]")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            footer[0]
        )

        print(f"{datetime.now()}   FOOTER_RISK_WARNING_BLOCK is visible? =>")
        if self.element_is_visible(MainMenu.FOOTER_RISK_WARNING_BLOCK):
            print(f"{datetime.now()}   => FOOTER_RISK_WARNING_BLOCK is visible on the page!")
        else:
            print(f"{datetime.now()}   => FOOTER_RISK_WARNING_BLOCK is not visible on the page!")
            pytest.fail("Bug #034! The footer is missing on click menu item [Professional] "
                        "of the menu section [Ways to trade]")
