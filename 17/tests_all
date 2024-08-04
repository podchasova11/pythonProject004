"""
-*- coding: utf-8 -*-
@Time    : 2024/06/06 15:29
@Author  : podchasova11
"""

import pytest
import allure
from datetime import datetime

from pages.BugsManual.bug_043 import ProfessionalMenuCheckFooter
from pages.BugsManual.bug_038 import WebTradingPlatformPage
from pages.BugsManual.bug_090 import CreateARiskFreeDemoAccountButton
from pages.BugsManual.bug_285 import ButtonMyAccount
from pages.Elements.AssertClass import AssertClass
from pages.Elements.PlatformOverviewButton import PlatformOverviewButton
from pages.Menu.menu import MenuSection
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55

from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.conditions_new import NewConditions


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("Start retest manual TC_55!00_038 The Trading platform overview page not open when"
                 " button [Platform overview] click on the 'Investmate app' page")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_038
    def test_038(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The Trading platform overview page does not open when
         the button [Platform overview] is pressed on the "Investmate app" page

         Author: podchasova11
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "038", "The Trading platform overview page not open when"
                   " button [Platform overview] click on the 'Investmate app' page"
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PlatformOverviewButton(d, link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, link)

        print(f'\n{datetime.now()}   3. Assert')

        page = WebTradingPlatformPage(d, link, bid)
        if not page.should_be_web_trading_platform_page(d, link):
            Common().pytest_fail(f"Bug#038. "
                                 "Expected result:The Desktop Trading page is opened "
                                 "\n"
                                 "Actual result: The Home page is opened ")
        Common().save_current_screenshot(d, "AT_55!038 Pass")

    @allure.step("Start retest manual TC_55!00_043 "
                 "The footer is missing on click menu item [Professional] of the menu section [Ways to trade]")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_043
    def test_043(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        The footer is missing on click menu item [Professional] of the menu section [Ways to trade]
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional]menu item
        Author: podchasova11
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "043",
            "The footer is missing on click menu item [Professional] of the menu section [Ways to trade]"
        )
        # pytest.skip("Autotest under construction")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        link = menu.open_ways_to_trade_professional_menu(d, cur_language, cur_country, link)

        menu = ProfessionalMenuCheckFooter(d, link, bid)
        menu.check_that_footer_displayed_on_professional_page(d, cur_language, cur_country, link)

    @allure.step("Start retest manual TC_55!00_090 "
                 "The trading platform page is not opened "
                 "in [demo mode] after clicking on the [Create a risk-free demo account] button "
                 "on the 'Demo account' page")
    @pytest.mark.parametrize('cur_country', ['de', 'ua']) # на лицензии 'au' другой локатор кнопки => тест выдает ошибку
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_090
    def test_090(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        The trading platform page is not opened in "Demo account" page
        after clicking on the [Create a risk-free demo account] button
        Language: All.
        License: All, except FCA, SCA.
        Country: All, except GB, AE.
        Author: podchasova11
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "090",
            "The trading platform page is not opened "
            "in [demo mode] after clicking on the [Create a risk-free demo account] button"
            "on the 'Demo account' page"
        )

        # pytest.skip("Autotest under construction")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        # Arrange
        menu = MenuSection(d, link)
        link = menu.sub_menu_demo_account_move_focus_click(d, cur_language, cur_country, link)
        # Act, Assert
        test_element = CreateARiskFreeDemoAccountButton(d, link, bid)
        test_element.full_test(d, cur_role, link)

    @allure.step("Start retest manual TC_55!00_285en Opened the Trading platform page "
                 "instead [My Account] menu after clicking the [My account] button")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_285en
    def test_285en(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Opened the Trading platform page
        instead [My Account] menu after clicking the [My account] button
        Language: EN
        License: SCA.
        Country: AE.
        Author: podchasova11
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "285en",
            "Opened the Trading platform page "
            "instead [My Account] menu after clicking the [My account] button"
        )

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_EN_AE, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # Arrange
        button = ButtonMyAccount(d, link, bid)
        button.arrange_(link)

        # Act
        button.element_click()

        # Assert
        match cur_role:
            case "Auth":
                button.assert_my_account_menu_opened_en(d)

    @allure.step("Start retest manual TC_55!00_285ar Opened the Trading platform page "
                 "instead [My Account] menu after clicking the [My account] button")
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_285ar
    def test_285ar(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Opened the Trading platform page
        instead [My Account] menu after clicking the [My account] button
        Language: AR
        License: SCA.
        Country: AE.
        Author: podchasova11
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "285ar",
            "Opened the Trading platform page "
            "instead [My Account] menu after clicking the [My account] button"
        )

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_AR_AE, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # Arrange
        button = ButtonMyAccount(d, link, bid)
        button.arrange_(link)

        # Act
        button.element_click()

        # Assert
        match cur_role:
            case "Auth":
                button.assert_my_account_menu_opened_ar(d)
