from infra.pages.base_screen import BaseScreen


class LoginScreen(BaseScreen):
    EMAIL_INPUT = {
        "ios": "email_input_ios",
        "android": "email_input_android",
    }
    PASSWORD_INPUT = {
        "ios": "password_input_ios",
        "android": "password_input_android",
    }
    TERMS_CHECKBOX = {
        "ios": "terms_and_conditions_check_box_ios",
        "android": "terms_and_conditions_check_box_android",
    }
    LOGIN_BUTTON = {
        "ios": "login_button_ios",
        "android": "login_button_android",
    }

    def login_the_app(self, email: str, password: str):
        self.session.enter_text(self.get_locator(self.EMAIL_INPUT), email)
        self.session.enter_text(self.get_locator(self.PASSWORD_INPUT), password)
        self.session.tap(self.get_locator(self.TERMS_CHECKBOX))
        self.session.tap(self.get_locator(self.LOGIN_BUTTON))
        self.session.login()
