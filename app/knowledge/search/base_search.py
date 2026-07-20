from abc import ABC, abstractmethod

from app.domain.entities.search_result import SearchResult


class BaseSearch(ABC):

    @abstractmethod
    def search(self, query: str) -> SearchResult:

        pass