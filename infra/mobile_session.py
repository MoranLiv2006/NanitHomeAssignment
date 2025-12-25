class MobileSession:
    def __init__(self, platform: str):
        if platform not in ("ios", "android"):
            raise ValueError("Platform must be 'ios' or 'android'")

        self.platform = platform
        self.screen_state = None
        self.app_launched = False
        self.logged_in = False
        self.stream_visible = False

    def launch_app(self):
        self.app_launched = True
        self.screen_state = "welcome"

    def find_element(self, element_id: str) -> bool:
        return True

    def tap(self, element_id: str):
        pass

    def enter_text(self, element_id: str, text: str):
        pass

    def login(self):
        self.logged_in = True
        self.screen_state = "live_stream"

    def navigate_to_live_stream(self):
        self.stream_visible = True
        self.screen_state = "live_stream"
