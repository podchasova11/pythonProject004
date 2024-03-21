"""
-*- coding: utf-8 -*-
@Time    : 2023/03/06 11:30
@Author  : podchasova11
"""

import random
from datetime import datetime

import pytest
import allure

from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonSellOnTableTradingInstrumentsLocators, \
    ItemSortDropdownLocators, TableTradingInstrumentsLocators, FieldDropdownMarketsLocator
from pages.Elements.AssertClass import AssertClass

COUNT_OF_RUNS = 2


class TableTradingInstrumentsSellButton(BasePage):

    def __init__(self, browser, link, bid):
        self.item_sort = None
        self.sort_locator = None
        self.current_sort = None

        self.sell_locator = None
        self.sell_list = None

        self.item = None
        self.trade_instrument = None

        super().__init__(browser, link, bid)

    @allure.step(f'{datetime.now()}   Start Full test [Sell] button on Table Widget Trading Instruments')
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link, cur_sort):
        item_list = self.arrange_(d, cur_item_link, cur_sort)
        print(f"\n{datetime.now()}   item_list = {item_list}")

        check_popup = SignupLogin(d, cur_item_link, cur_sort)
        check_popup.check_popup_signup_form()
        del check_popup

        for i, value in enumerate(item_list):
            self.element_click(self.driver, value, cur_sort)
            test_element = AssertClass(self.driver, cur_item_link, self.bid)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(
                        self.driver, cur_item_link, False, True, self.trade_instrument)
            self.driver.get(cur_item_link)

    def arrange_(self, d, cur_item_link, cur_sort):
        global COUNT_OF_RUNS
        print(f"\n{datetime.now()}   1. Arrange for TABLE_TRADING_INSTRUMENTS and '{cur_sort}' cur_sort")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   TABLE_TRADING_INSTRUMENTS present on this page? =>")
        table_list = self.driver.find_elements(*TableTradingInstrumentsLocators.TABLE_TRADING_INSTRUMENTS)
        if len(table_list) == 0:
            print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is NOT present on this page\n")
            pytest.fail(f" Bug ? Checking element is not on this page")

        print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is present on the page!")

        print(f"{datetime.now()}   IS FIELD_DROPDOWN_SORT present in the Live prices table? =>")
        field_dropdown_list = self.driver.find_elements(*FieldDropdownMarketsLocator.FIELD_DROPDOWN_MARKETS)
        if len(field_dropdown_list) == 0:
            pytest.fail("Bug # ? FIELD_DROPDOWN_SORT is not present in Live table!")

        print(f"{datetime.now()}   =>  FIELD_DROPDOWN_SORT is present in the Live prices table!")

        print(f"{datetime.now()}   Start scroll and click FIELD_DROPDOWN_SORT =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            field_dropdown_list[0]
        )
        field_dropdown_list[0].click()

        match cur_sort:
            case 'Most traded':
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_MOST_TRADED
                self.sort_locator = FieldDropdownMarketsLocator.FIELD_DROPDOWN_MOST_TRADED

            case 'Top risers':
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_TOP_RISERS
                self.sort_locator = FieldDropdownMarketsLocator.FIELD_DROPDOWN_TOP_RISERS

            case 'Top fallers':
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_TOP_FALLERS
                self.sort_locator = FieldDropdownMarketsLocator.FIELD_DROPDOWN_TOP_FALLERS

            case 'Most volatile':
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_MOST_VOLATILE
                self.sort_locator = FieldDropdownMarketsLocator.FIELD_DROPDOWN_MOST_VOLATILE

        self.sell_locator = TableTradingInstrumentsLocators.BUTTON_SELL_TRADING_INSTRUMENT
        self.item = TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT

        print(f"{datetime.now()}   Is item_sort_list visible on the FIELD_DROPDOWN_SORT ? =>")

        item_sort_list = self.element_is_visible(ItemSortDropdownLocators.ALL_ITEM_DROPDOWN_SORT)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            item_sort_list
        )

        if not item_sort_list:
            pytest.fail("Bug ? item_sort_list is not visible")
        print(f"{datetime.now()}   => item_sort_list is visible on the FIELD_DROPDOWN_SORT!")

        print(f"{datetime.now()}   Is cur_sort \"{cur_sort}\" present in item_sort_list? =>")
        if not self.driver.find_element(*self.item_sort):
            print(f"{datetime.now()}   => cur_sort \"{cur_sort}\" is not present in item_sort_list!")
            pytest.fail(f"Bug ? cur_sort \"{cur_sort}\" is not present in item_sort_list!")
        print(f"{datetime.now()}   => cur_sort \"{cur_sort}\" is present in item_sort_list!")
        print(f"{datetime.now()}   Start click cur_sort \"{cur_sort}\" =>")

        self.current_sort = self.driver.find_element(*self.item_sort)
        self.current_sort.click()

        print(f"{datetime.now()}   => End Click cur_sort \"{cur_sort}\"\n")

        print(f"{datetime.now()}   Buttons [Sell] is visible and sum buttons no zero? =>")
        if self.driver.find_elements(*self.sell_locator) != 0:
            print(f"{datetime.now()}   => Buttons [Sell] is visible and sum buttons no zero!\n")
            print(f"{datetime.now()}   Start find two random buttons [Sell] on cur_sort \"{cur_sort}\"=>")
            self.sell_list = self.driver.find_elements(*self.sell_locator)
            qty_buttons = len(self.sell_list)
            count_of_runs = COUNT_OF_RUNS if qty_buttons >= COUNT_OF_RUNS else qty_buttons
            item_list = random.sample(range(qty_buttons), count_of_runs)
            print(f"{datetime.now()}   => End find two random buttons [Sell] on the cur_sort "
                  f"\"{cur_sort}\"\n")

            return item_list
        else:
            print(f"{datetime.now()}   => Buttons [Sell] is NOT visible or sum buttons zero!\n")
            pytest.fail("Bug ? element is not on this page")

    @allure.step("Click Sell button on Table Widget Trading Instruments")
    def element_click(self, wd, value, cur_sort):
        print(f"{datetime.now()}   2. Act for trading instrument and \"{cur_sort}\" cur_sort")

        print(f"{datetime.now()}   Start click button [Sell] =>")
        self.sell_list = self.driver.find_elements(*self.sell_locator)
        button = self.sell_list[value]
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )

        # Вытаскиваем линк из кнопки
        button_link = button.get_attribute('data-href')
        # Берём ID item, на который кликаем для сравнения с открытым ID на платформе
        self.trade_instrument = button_link[button_link.find("spotlight") + 10:button_link.find("?")]

        button.click()
        print(f"{datetime.now()}   =>   BUTTON_SELL with item {self.trade_instrument} clicked!\n")

    # def __init__(self, browser, link, bid):
    #     self.item_sorting = None
    #     self.sorting_locator = None
    #     self.current_sorting = None
    #
    #     self.instruments_name_list = None
    #     self.instruments_list = None
    #     self.cur_instrument = None
    #
    #     self.trade_instrument = None
    #
    #     super().__init__(browser, link, bid)

    # @allure.step(f'{datetime.now()}   Start Full test [Sell] button on Table Widget Trading Instruments')
    # def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link, cur_sort):
    #     num_item_list = self.arrange_(d, cur_item_link, cur_sort)
    #     print(f"\n{datetime.now()}   num_item_list = {num_item_list}")
    #
    #     check_popup = SignupLogin(d, cur_item_link, cur_sort)
    #     check_popup.check_popup_signup_form()
    #     del check_popup
    #
    #     for i, volume in enumerate(num_item_list):
    #         self.element_click(d, volume, cur_sort)
    #
    #         check_element = AssertClass(self.driver, cur_item_link, self.bid)
    #         match cur_role:
    #             case "NoReg":
    #                 check_element.assert_signup(d, cur_language, cur_item_link)
    #             case "NoAuth":
    #                 check_element.assert_login(d, cur_language, cur_item_link)
    #             case "Auth":
    #                 check_element.assert_trading_platform_v4(d, cur_item_link, False, True, self.trade_instrument)
    #         self.driver.get(cur_item_link)

    # def arrange_(self, d, cur_item_link, cur_sort):
    #     print(f"\n{datetime.now()}   1. Arrange for TABLE_TRADING_INSTRUMENTS and '{cur_sort}' cur_sort")
    #
    #     if not self.current_page_is(cur_item_link):
    #         self.link = cur_item_link
    #         self.open_page()
    #
    #     print(f"{datetime.now()}   TABLE_TRADING_INSTRUMENTS and cur_sort present on this page? =>")
    #     dropdown_list = self.driver.find_elements(*ItemSortDropdownLocators.ALL_ITEM_DROPDOWN_SORT)
    #     if len(dropdown_list) == 0:
    #         print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS and cur_sort is NOT present on this page\n")
    #         pytest.fail(f" Bug ? Checking cur_sort element is not on this page")
    #     print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS and cur_sort present on the page!\n")
    #
    #     print(f"{datetime.now()}   Start scroll and click FIELD_DROPDOWN_SORT =>")
    #     self.driver.execute_script(
    #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
    #         dropdown_list[0]
    #     )
    #     dropdown_list[0].click()
    #
    #     match cur_sort:
    #         case 'Most traded':
    #             self.sorting_locator = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_MOST_TRADED
    #         case 'Top risers':
    #             self.sorting_locator = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_TOP_RISERS
    #         case 'Top fallers':
    #             self.sorting_locator = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_TOP_FALLERS
    #         case 'Most volatile':
    #             self.sorting_locator = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_MOST_VOLATILE
    #
    #     self.instruments_list = self.driver.find_elements(
    #         *ButtonSellOnTableTradingInstrumentsLocators.TABLE_TRADING_INSTRUMENTS_LIST)
    #     self.instruments_name_list = self.driver.find_elements(
    #         *ButtonSellOnTableTradingInstrumentsLocators.TABLE_TRADING_INSTRUMENTS_NAME_LIST)
    #
    #     print(f"{datetime.now()}   => Found {cur_sort} elements in TABLE_TRADING_INSTRUMENTS")
    #     if not self.driver.find_element(*self.sorting_locator):
    #         print(f"{datetime.now()}   => cur_sort \"{cur_sort}\" is not present in dropdown_list!")
    #         pytest.fail(f"Bug ? cur_sort \"{cur_sort}\" is not present in dropdown_list!")
    #     print(f"{datetime.now()}   => cur_sort \"{cur_sort}\" is present in dropdown_list!")
    #     print(f"{datetime.now()}   Start click cur_sort \"{cur_sort}\" =>")
    #
    #     self.current_sorting = self.driver.find_element(*self.sorting_locator)
    #     self.current_sorting.click()
    #
    #     print(f"{datetime.now()}   => End Click cur_sort \"{cur_sort}\"\n")
    #
    #     print(f"{datetime.now()}   Buttons [Sell] is visible? =>")
    #
    #     if self.driver.find_elements(*self.instruments_list) != 0:
    #         print(f"{datetime.now()}   => Buttons [Sell] is visible!\n")
    #         print(f"{datetime.now()}   Start find two random buttons [Sell] on cur_sort \"{cur_sort}\"=>")
    #         self.instruments_name_list = self.driver.find_elements(*self.instruments_list)
    #         qty_rnd = len(self.instruments_name_list)
    #         count = COUNT if qty_rnd >= COUNT else qty_rnd
    #         item_list = random.sample(range(qty_rnd), count)
    #         print(f"{datetime.now()}   => End find two random buttons [Sell] on the cur_sort "
    #               f"\"{cur_sort}\"\n")
    #
    #         return item_list
    #     else:
    #         print(f"{datetime.now()}   => Buttons [Sell] is NOT visible!\n")
    #         pytest.fail("Bug ? element is not on this page")

    # @allure.step('Click Sell button on Table Widget Trading Instruments')
    # def element_click(self, wd, index, cur_sort):
    #     print(f"\n{datetime.now()}   2. Act for trading instrument and \"{cur_sort}\" cur_sort")
    #
    #     print(f"{datetime.now()}   Start click button [Sell] =>")
    #     self.instruments_name_list = wd.find_elements(*self.instruments_list)
    #     button = self.instruments_name_list[index]
    #     wd.execute_script(
    #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
    #         button
    #     )
    #
    #     button_link = button.get_attribute('data-href')
    #     self.trade_instrument = button_link[button_link.find("spotlight") + 10:button_link.find("?")]
    #
    #     button.click()
    #     print(f"{datetime.now()}   =>   BUTTON_SELL with item {self.trade_instrument} clicked!\n")
