from source.bot_utils.os_utils import OSUtils


class WindowsOsUtils(OSUtils):
    def __init__(self):
        raise NotImplementedError("Error: Windows utils are not implemented yet")

    def create_new_document(self) -> None:
        raise NotImplementedError("Error: Windows utils are not implemented yet")

    def save_document(self, document_name: str) -> None:
        raise NotImplementedError("Error: Windows utils are not implemented yet")
