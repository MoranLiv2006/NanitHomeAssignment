class BaseScreen:
    def __init__(self, session):
        self.session = session
        self.platform = session.platform

    def get_locator(self, locator_dict: dict) -> str:
        try:
            return locator_dict[self.platform]
        except KeyError:
            raise ValueError(
                f"Locator not defined for platform: {self.platform}"
            )
