from abc import ABC, abstractmethod


class OSUtils(ABC):

    @abstractmethod
    def create_new_document(self) -> None:
        ...

    @abstractmethod
    def save_document(self, document_name: str) -> None:
        ...
