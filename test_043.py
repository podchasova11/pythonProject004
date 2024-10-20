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
