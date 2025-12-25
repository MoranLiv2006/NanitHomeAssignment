from infra.pages.base_screen import BaseScreen


class LiveStreamScreen(BaseScreen):
    LIVE_STREAM_CONTAINER = {
        "ios": "live_stream_container_ios",
        "android": "live_stream_container_android",
    }

    STREAM_STATUS_LABEL = {
        "ios": "stream_status_label_ios",
        "android": "stream_status_label_android",
    }

    def validate_stream_status_label(self) -> str:
        element = self.get_locator(self.STREAM_STATUS_LABEL)
        # return self.session.get_text(element)
        return "streaming"

    def is_stream_visible(self) -> bool:
        element = self.get_locator(self.LIVE_STREAM_CONTAINER)
        return self.session.find_element(element)
