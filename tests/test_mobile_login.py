import pytest

from infra.pages.live_stream_screen import LiveStreamScreen
from infra.pages.login_screen import LoginScreen
from infra.pages.welcome_screen import WelcomeScreen


class TestMobileLogin:

    @pytest.mark.mobile
    @pytest.mark.parametrize("mobile_session", ["ios", "android"], indirect=True)
    def test_user_can_login_and_see_live_stream(self, mobile_session, credentials):
        welcome_screen = WelcomeScreen(mobile_session)
        login_screen = LoginScreen(mobile_session)
        live_stream_screen = LiveStreamScreen(mobile_session)

        welcome_screen.tap_login_button()
        login_screen.login_the_app(credentials["email"], credentials["password"])
        mobile_session.navigate_to_live_stream()

        assert live_stream_screen.validate_stream_status_label() == "streaming"
        assert live_stream_screen.is_stream_visible() is True
