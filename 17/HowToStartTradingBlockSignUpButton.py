"""
-*- coding: utf-8 -*-
@Time    : 2023/05/01 11:30
@Author  : podchasova11
"""

from datetime import datetime
import random

# import pytest
import allure
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from pages.common import Common
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.testing_elements_locators import (TableTradingInstrumentsLocators, FieldDropdownMarketsLocator,
                                                      ItemSortDropdownLocators)
from pages.Elements.AssertClass import AssertClass

COUNT_OF_RUNS = 1


class TableTradingInstrumentsBuyButton(BasePage):

    @allure.step('Start Full test [] button on Table Widget Trading Instruments')
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        item_list = self.arrange_(d, cur_item_link)
        print(f"\n{datetime.now()}   Item_list = {item_list}")

        # Check there are an elements to on Sign up form
        check_signup_form = SignupLogin(d, cur_item_link)
        check_signup_form.should_be_open_signup_form()
        del check_signup_form

        self.element_click(self.driver)
        test_element = AssertClass(self.driver, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)

    @allure.step(f"{datetime.now()}  Start Full test for 'Try free demo' button on 'Block CFD Calculator'")
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
