"""
-*- coding: utf-8 -*-
@Time    : 2023/04/18 19:30
@Author  : Mila Podchasova
"""

from datetime import datetime
import pytest
import allure

from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.Markets.markets_locators import HeaderElementLocators
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException


class HeaderCFDCalculatorPageLoginButton(BasePage):

    @allure.step(f"{datetime.now()}  Start Full test for 'Log In' button of Header")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(d)

        test_element = AssertClass(d, cur_item_link, self.bid)

        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.driver.find_elements(*HeaderElementLocators.BUTTON_LOGIN)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_LOGIN is not present on this page")
            del button_list
            pytest.fail("Testing element BUTTON_LOGIN on the 'Header' is not present on this page")
        else:
            print(f"{datetime.now()}   => BUTTON_LOGIN is present on this page")

        print(f"{datetime.now()}   BUTTON_LOGIN scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_LOGIN is visible? =>")
        if self.element_is_visible(HeaderElementLocators.BUTTON_LOGIN):
            print(f"{datetime.now()}   => BUTTON_LOGIN is visible on this page")
        else:
            print(f"{datetime.now()}   => BUTTON_LOGIN is not visible on this page")
            pytest.fail("Bug! Testing element 'BUTTON_LOGIN on the 'Header' is present on this page, "
                        "but not visible")

    @allure.step("Click button [Log In] on 'Header'")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")

        button_list = self.driver.find_elements(*HeaderElementLocators.BUTTON_LOGIN)
        print(f"{datetime.now()}   BUTTON_LOGIN is clickable? =>")
        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()}   => BUTTON_LOGIN is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_LOGIN is not clickable after {time_out} sec.")

        try:
            self.driver.execute_script("arguments[0].click();", button_list[0])
            print(f"{datetime.now()}   => BUTTON_LOGIN clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_LOGIN NOT CLICKED")
            print(f"{datetime.now()}   'Log In' form or page is auto opened")

            page_ = SignupLogin(self.driver)
            if page_.close_login_form():
                pass
            else:
                page_.close_login_page()

            self.driver.execute_script("arguments[0].click();", button_list[0])
            del page_

        del button_list
        return True
