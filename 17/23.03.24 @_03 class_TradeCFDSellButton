from datetime import datetime
import pytest
import allure

from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import TradeCFDLocators
from selenium.common.exceptions import ElementClickInterceptedException


class TradeCFDSellButton(BasePage):

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)

        page_signup_login = SignupLogin(d, cur_item_link)
        page_signup_login.check_popup_signup_form()

        trade_instrument = self.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, False, True, trade_instrument)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_SELL is located on the page? =>")
        button_list = self.elements_are_located(TradeCFDLocators.SELL_BUTTON)

        if not button_list:
            print(f"{datetime.now()}   => BUTTON_SELL is not located on the page!")
            pytest.skip("Checking element (BUTTON_SELL) is not on this page")

        print(f"{datetime.now()}   => BUTTON_SELL is located on the page!")

    @allure.step("Click button [Sell]")
    def element_click(self, cur_role):
        print(f"\n{datetime.now()}   2. Act_v0")
        button_list = self.driver.find_elements(*TradeCFDLocators.SELL_BUTTON)

        print(f"{datetime.now()}   BUTTON_SELL is present? =>")
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_SELL is not present on the page")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_SELL is present on the page")

        print(f"{datetime.now()}   BUTTON_SELL scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        print(f"{datetime.now()}   => BUTTON_SELL scrolled")

        button_link = button_list[0].get_attribute('href')
        trade_instrument = button_link[button_link.find("spotlight") + 10:button_link.find("?")]

        print(f"{datetime.now()}   BUTTON_SELL is clickable? =>")
        if not self.element_is_clickable(button_list[0], 5):
            print(f"{datetime.now()}   => BUTTON_SELL is not clickable more then 5 sec.")
            pytest.fail("BUTTON_SELL is not clickable more then 5 sec.")
        try:
            print(f"{datetime.now()}   BUTTON_SELL CLICK =>")
            button_list[0].click()

            print(f"{datetime.now()}   => BUTTON_SELL clicked!")

        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_SELL NOT CLICKED")

            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            self.driver.execute_script("arguments[0].click();", button_list[0])
            del page_

        del button_list
        return trade_instrument
