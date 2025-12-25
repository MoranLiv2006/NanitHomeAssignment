from infra.pages.base_screen import BaseScreen


class WelcomeScreen(BaseScreen):
    LOGIN_BUTTON = {
        "ios": "login_button_ios",
        "android": "login_button_android",
    }

    def tap_login_button(self):
        self.session.tap(self.get_locator(self.LOGIN_BUTTON))
