from source.bot_utils.os_utils import OSUtils


class LinuxOsUtils(OSUtils):
    def __init__(self):
        raise NotImplementedError("Error: Linux utils are not implemented yet")

    def create_new_document(self) -> None:
        raise NotImplementedError("Error: Linux utils are not implemented yet")

    def save_document(self, document_name: str) -> None:
        raise NotImplementedError("Error: Linux utils are not implemented yet")
