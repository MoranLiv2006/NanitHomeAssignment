import pytest

from infra.pages.live_stream_screen import LiveStreamScreen
from infra.pages.login_screen import LoginScreen
from infra.pages.welcome_screen import WelcomeScreen


class TestMobileApiIntegration:

    @pytest.mark.integration
    @pytest.mark.parametrize("mobile_session", ["ios", "android"], indirect=True)
    def test_stream_status_is_consistent_in_both_the_api_and_the_mobile_layers(self, mobile_session, streaming_validator, credentials):
        # mobile section
        welcome = WelcomeScreen(mobile_session)
        login = LoginScreen(mobile_session)
        live_stream = LiveStreamScreen(mobile_session)

        welcome.tap_login_button()
        login.login_the_app(credentials["email"], credentials["password"])
        mobile_session.navigate_to_live_stream()

        assert live_stream.is_stream_visible()

        # api section
        streaming_validator.validate_streaming_performance_parameters()

        # mobile-api integration validation
        assert mobile_session.stream_visible is True
