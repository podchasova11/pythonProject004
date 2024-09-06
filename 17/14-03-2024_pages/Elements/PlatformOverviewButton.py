
import pytest
from pages.base_page import BasePage

class USLink:
    user_story_menu_link = None

    def get_us_link(self, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        if cur_language in ["de", "es", "fr", "it", "pl", "cn", "nl"]:
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


class PlatformOverviewButton(BasePage):
    pytest.skip("Class for bug#_029 under construction")
    page_conditions = None
    us_link = USLink()
    
    @allure.step(f"{datetime.now()}   Start full test of [Platform overview] button")
    def full_test(self, d, cur_language, cur_country, cur_role, link):
        self.arrange_(d)
        self.element_click()
    
        test_element = AssertClass(d, self.bid)
        match cur_role:
            case "NoReg" | "NoAuth" | "Auth":
                test_element.assert_desktop_trading_page(d)
    
    def arrange_(self, link):
        print(f"\n{datetime.now()}   1. Arrange for [Platform overview] button")
    
        if not self.current_page_is(link):
            self.link = CapitalComPageSrc.URL
            self.open_page()
    
        print(f"{datetime.now()}   Is BUTTON_PLATFORM_OVERVIEW present on the page? =>")
        button = self.driver.find_elements(*ButtonLocators.BUTTON_PLATFORM_OVERVIEW)
        if len(button) == 0:
            print(f"{datetime.now()}   => BUTTON_PLATFORM_OVERVIEW is not present on the page")
            Common().pytest_fail("BUTTON_PLATFORM_OVERVIEW is not present on the page")
        print(f"{datetime.now()}   => BUTTON_PLATFORM_OVERVIEW is present on the page")
    
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button[0]
        )
    
        print(f"{datetime.now()}   Is BUTTON_PLATFORM_OVERVIEW clickable?  =>")
        time_out = 3
        if not self.element_is_clickable(button[0], time_out):
            print(f"{datetime.now()}   => BUTTON_PLATFORM_OVERVIEW is not clickable after {time_out} sec")
            Common.pytest_fail("Bug ? BUTTON_PLATFORM_OVERVIEW is not clickable")
        print(f"{datetime.now()}   => BUTTON_PLATFORM_OVERVIEW is clickable")
    
    @allure.step("Click [Platform overview] button in the page")
    def element_click(self):
        print(f"{datetime.now()}   2. Act for [Platform overview] button")
        print(f"{datetime.now()}   Start to click BUTTON_PLATFORM_OVERVIEW =>")
    
        button = self.driver.find_elements(*ButtonLocators.BUTTON_PLATFORM_OVERVIEW)
        button[0].click()
    
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url)
        )
    
        print(f"{datetime.now()}   => BUTTON_PLATFORM_OVERVIEW is clicked")
