"""
-*- coding: utf-8 -*-                   C:\Users\Mila\PycharmProjects\TestCapitalComPySe\pages\Elements\ButtonCreateAccountMainBanner.py
@Time    : 202/02/09 20:39
@Author  : Mila Podchasova
"""

from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import MainBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException


class MainBannerCreateAccount(BasePage):

    @allure.step(f'{datetime.now()}   Start Full test for Create Account button of Main banner')
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):

        self.arrange_(d, cur_item_link)
        self.element_click()

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    def full_test(self, d, cur_language, cur_country, cur_role, page_url):

        self.arrange_(d, page_url)

        self.element_click()

        test_element = AssertClass(d, page_url)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(
                    d, cur_language, page_url
                )
            case "NoAuth":
                test_element.assert_login(
                    d, cur_language, page_url
                )
            case "Auth":
                test_element.assert_trading_platform_v4(
                    d, page_url
                )

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.driver.find_elements(*MainBannerLocators.BUTTON_CREATE_ACCOUNT)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT is not present on the page!")
            del button_list
            pytest.skip("Checking element 'BUTTON_CREATE_ACCOUNT on the main banner' is not on this page")

        print(f"{datetime.now()}   BUTTON_CREATE_ACCOUNT scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_CREATE_ACCOUNT is visible? =>")
        if self.element_is_visible(MainBannerLocators.BUTTON_CREATE_ACCOUNT):
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT is not visible on the page!")
            pytest.fail("Bug! Checking element 'BUTTON_CREATE_ACCOUNT on main banner' is present on this page, "
                        "but not visible")

    @allure.step("Click button [Create Account] on Main banner")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click button [Create Account] =>")
        button_list = self.driver.find_elements(*MainBannerLocators.BUTTON_CREATE_ACCOUNT)

        print(f"{datetime.now()}   BUTTON_CREATE_ACCOUNT is clickable? =>")
        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_CREATE_ACCOUNT is not clickable after {time_out} sec.")

        print(f"{datetime.now()}   BUTTON_CREATE_ACCOUNT click =>")
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_CREATE_ACCOUNT not clicked")
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
####################################################################################################################################


"""
-*- coding: utf-8 -*-
@Time    : 202/02/09 20:39
@Author  : Mila Podchasova
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import MainBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException


class MainBannerOpenAnAccount(BasePage):

    @allure.step(f"{datetime.now()}   Start Full test for Open an account button of Main banner")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):

        self.arrange_(d, cur_item_link)
        self.element_click(cur_language, cur_country)

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    # def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
    #
    #     self.arrange_(d, cur_item_link)
    #     self.element_click()
    #
    #     test_element = AssertClass(d, cur_item_link, self.bid)
    #     match cur_role:
    #         case "NoReg" | "NoAuth":
    #             test_element.assert_signup(d, cur_language, cur_item_link)
    #         case "Auth":
    #             test_element.assert_trading_platform_v4(d, cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.driver.find_elements(*MainBannerLocators.BUTTON_OPEN_AN_ACCOUNT)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_OPEN_AN_ACCOUNT is not present on the page!")
            del button_list
            pytest.skip("Checking element 'BUTTON_OPEN_AN_ACCOUNT on Main banner' is not on this page")

        print(f"{datetime.now()}   BUTTON_OPEN_AN_ACCOUNT scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_OPEN_AN_ACCOUNT is visible? =>")
        if self.element_is_visible(MainBannerLocators.BUTTON_OPEN_AN_ACCOUNT):
            print(f"{datetime.now()}   => BUTTON_OPEN_AN_ACCOUNT is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_OPEN_AN_ACCOUNT is not visible on the page!")
            pytest.fail("Bug! Checking element 'BUTTON_OPEN_AN_ACCOUNT on Main banner' is present on this page, "
                        "but not visible")

    @allure.step("Click button [Open an account] on Main banner")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click button [Open an account] =>")
        button_list = self.driver.find_elements(*MainBannerLocators.BUTTON_OPEN_AN_ACCOUNT)

        print(f"{datetime.now()}   BUTTON_OPEN_AN_ACCOUNT is clickable? =>")
        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()}   => BUTTON_OPEN_AN_ACCOUNT is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_OPEN_AN_ACCOUNT is not clickable after {time_out} sec.")

        print(f"{datetime.now()}   BUTTON_OPEN_AN_ACCOUNT click =>")
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_OPEN_AN_ACCOUNT clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_OPEN_AN_ACCOUNT not clicked")
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
