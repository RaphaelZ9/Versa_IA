from app.domain.entities.search_result import SearchResult


class SearchResolver:

    MIN_DOCUMENTS = 2

    MIN_CONTENT_SIZE = 80

    def has_enough_context(self, result: SearchResult) -> bool:

        if result is None:
            return False

        if not result.success:
            return False

        if not result.has_documents:
            return False

        valid_documents = 0

        for document in result.documents:

            if not document.content:
                continue

            if len(document.content.strip()) < self.MIN_CONTENT_SIZE:
                continue

            valid_documents += 1

        return valid_documents >= self.MIN_DOCUMENTS