"""
-*- coding: utf-8 -*-
@Time    : 2024/02/27 23:00
@Author  : podchasova11
"""
from datetime import datetime
import pytest
import allure
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import TradeIndicesBlockLocators
from selenium.common.exceptions import ElementClickInterceptedException
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import TradeIndicesBlockLocators
from selenium.common.exceptions import ElementClickInterceptedException


class TradeIndicesBlockStartTradingNow(BasePage):

    @allure.step(f'{datetime.now()}   Start Full test for Start trading now button of Block Trade Indices')
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):

        self.arrange_(d, cur_item_link, True)
        self.element_click()

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)


    def arrange_(self, d, cur_item_link, always=False):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.driver.find_elements(*TradeIndicesBlockLocators.BUTTON_START_TRADING_NOW)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_START_TRADING_NOW is not present on the page!")
            del button_list
            msg = "Testing element 'BUTTON_START_TRADING_NOW on the main banner' is not on this page"
            if always:
                pytest.fail(f"Bug № ??? {msg}")
            else:
                pytest.skip(msg)

        print(f"{datetime.now()}   BUTTON_START_TRADING_NOW scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_START_TRADING_NOW is visible? =>")
        if self.element_is_visible(TradeIndicesBlockLocators.BUTTON_START_TRADING_NOW):
            print(f"{datetime.now()}   => BUTTON_START_TRADING is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_START_TRADING is not visible on the page!")
            pytest.fail("Bug! Testing element 'BUTTON_START_TRADING on Block Trade Indices' is present on this page, "
                        "but not visible")

    @allure.step("Click button [Start Trading Now] on Block Trade Indices")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click button [Start Trading Now] =>")

        button_list = self.driver.find_elements(*TradeIndicesBlockLocators.BUTTON_START_TRADING_NOW)
        print(f"{datetime.now()}   BUTTON_START_TRADING_NOW is clickable? =>")
        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()}   => BUTTON_START_TRADING_NOW is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_START_TRADING_NOW is not clickable after {time_out} sec.")

        print(f"{datetime.now()}   BUTTON_START_TRADING_NOW click =>")
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_START_TRADING_NOW clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_START_TRADING_NOW not clicked")
            print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            elif page_.close_login_form():
                pass
            elif page_.close_signup_page():
                pass
            else:
                page_.close_login_page()

            del page_
            button_list[0].click()

        del button_list
        return True
