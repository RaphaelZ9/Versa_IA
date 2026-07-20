from app.domain.entities.search_result import SearchResult


class DocumentFilter:

    TRUSTED_DOMAINS = {
        "versaenergia": 100,
        "gov.br": 95,
        "aneel.gov.br": 95,
        "ons.org.br": 95,
        "ibge.gov.br": 90,
        "bcb.gov.br": 90,
        "wikipedia": 70,
        "fifa": 70
    }

    MAX_DOCUMENTS = 5

    def filter(
        self,
        query: str,
        result: SearchResult
    ) -> SearchResult:

        if result is None:
            return result

        if not result.has_documents:
            return result

        for document in result.documents:

            score = 0

            score += self._trust_score(document.url)

            score += self._title_score(
                query,
                document.title
            )

            score += self._content_score(
                query,
                document.content
            )

            score += self._quality_score(
                document.content
            )

            document.score = score

        result.documents.sort(
            key=lambda d: d.score,
            reverse=True
        )

        result.documents = result.documents[:self.MAX_DOCUMENTS]

        return result

    def _trust_score(self, url: str) -> int:

        if not url:
            return 0

        url = url.lower()

        for domain, score in self.TRUSTED_DOMAINS.items():

            if domain in url:
                return score

        return 10

    def _title_score(
        self,
        query: str,
        title: str
    ) -> int:

        if not title:
            return 0

        score = 0

        title = title.lower()

        for word in query.lower().split():

            if word in title:
                score += 8

        return score

    def _content_score(
        self,
        query: str,
        content: str
    ) -> int:

        if not content:
            return 0

        score = 0

        content = content.lower()

        for word in query.lower().split():

            if word in content:
                score += 4

        return score

    def _quality_score(
        self,
        content: str
    ) -> int:

        if not content:
            return 0

        size = len(content)

        if size > 1000:
            return 20

        if size > 500:
            return 15

        if size > 250:
            return 10

        if size > 100:
            return 5

        return 0