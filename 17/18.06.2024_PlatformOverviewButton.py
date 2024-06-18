"""
-*- coding: utf-8 -*-
@Time    : 2024/06/14 10:20
@Author  : podchasova11
"""

from datetime import datetime

import allure
import pytest

from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import MyAccountButtonLocators
from pages.Menu.menu import MenuSection
from pages.base_page import BasePage
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PlatformOverviewButton(BasePage):
    user_story_menu_link = None

    @allure.step(f"{datetime.now()}   Start full test of [Platform overview] button")
    def full_test(self, d, cur_language, cur_country, cur_role, link):
        self.get_us_link()
        self.arrange_(d)
        self.element_click()

        test_element = AssertClass(d, self.bid)
        match cur_role:
            case "NoReg" | "NoAuth" | "Auth":
                test_element.assert_that_trading_page_is_opened(d)

    def get_us_link(self, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        if cur_language not in ["en"]:
            pytest.skip(f"This test is not for {cur_language} language")

            page_conditions = Conditions(d, "")
            main_link = page_conditions.preconditions(
                d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
            if not self.user_story_menu_link:
                page_menu = MenuSection(d, main_link)
                page_menu.menu_education_move_focus(d, cur_language, cur_country)
                us_link = page_menu.sub_menu_investmate_app_move_focus_click(d, cur_language)
                self.user_story_menu_link = us_link
            return self.user_story_menu_link


           #####################################

    def arrange_(self, link):
        print(f"\n{datetime.now()}   1. Arrange for [Platform overview] button")

        if not self.current_page_is(link):
            self.link = CapitalComPageSrc.URL
            self.open_page()

    print(f"{datetime.now()}   Is BUTTON_MY_ACCOUNT present on the page? =>")
    button = self.driver.find_elements(*MyAccountButtonLocators.BUTTON_MY_ACCOUNT)
    if len(button) == 0:
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not present on the page")
        Common().pytest_fail("BUTTON_MY_ACCOUNT is not present on the page")
    print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is present on the page")
    self.driver.execute_script(
        'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        button[0]
    )

    print(f"{datetime.now()}   Is BUTTON_MY_ACCOUNT clickable?  =>")
    time_out = 3
    if not self.element_is_clickable(button[0], time_out):
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not clickable after {time_out} sec")
        Common.pytest_fail("Bug ? BUTTON_MY_ACCOUNT is not clickable")
    print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is clickable")

    @allure.step("Click My account button in the page header")
    def element_click(self):
        print(f"{datetime.now()}   2. Act for My account button")
        print(f"{datetime.now()}   Start to click BUTTON_MY_ACCOUNT =>")

        button = self.driver.find_elements(*MyAccountButtonLocators.BUTTON_MY_ACCOUNT)
        button[0].click()

        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url)
        )

        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is clicked")
