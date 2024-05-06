 @allure.step("Check that 'Sign up form' on 'CFD Calculator' page open")
    def should_be_open_signup_form(self, cur_language):
        """
        Check there are an elements to on Sign up form
        """
        print(f"{datetime.now()}   Start step Check that [Sign up] form on 'CFD Calculator' page opened")
        if self.element_is_visible(HowToStartTradingSignupLocators.SIGNUP_FRAME, 3):
            print(f"{datetime.now()}   'Sign up' form on 'CFD Calculator' page opened")

            print(f"{datetime.now()}   Assert SIGNUP_INPUT_EMAIL =>")
            Common().assert_true_false(
                self.element_is_visible(HowToStartTradingSignupLocators.SIGNUP_INPUT_EMAIL),
                f"{datetime.now()}   SIGNUP_INPUT_EMAIL "
            )

            print(f"{datetime.now()}   Assert SIGNUP_REF_LOGIN =>")
            Common().assert_true_false(
                self.element_is_visible(HowToStartTradingSignupLocators.SIGNUP_REF_LOGIN),
                f"{datetime.now()})   Problem with 'Login' reference")

            print(f"{datetime.now()}   Assert SIGNUP_PRIVACY_POLICY_ALL_2 =>")
            if not self.element_is_visible(HowToStartTradingSignupLocators.SIGNUP_PRIVACY_POLICY_ALL_2):

                print(f"{datetime.now()}   Assert SIGNUP_PRIVACY_POLICY_ALL_1 =>")
                if not self.element_is_visible(HowToStartTradingSignupLocators.SIGNUP_PRIVACY_POLICY_ALL_1):
                    Common().assert_true_false(
                        False,
                        f"{datetime.now()}   Problem with 'Privacy policy' reference on '{cur_language}' language!"
                    )

            print(f"{datetime.now()}   => SIGNUP_PRIVACY_POLICY_ALL")

            print(f"{datetime.now()}   => 'Signup' form is checked")
            return True
        else:
            print(f"{datetime.now()}   'Sign up' form not opened")
            return False
