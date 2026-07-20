import re

from app.knowledge.knowledge_source import KnowledgeSource


class QueryOptimizer:

    STOPWORDS = {
        "o", "a", "os", "as",
        "de", "da", "do", "das", "dos",
        "um", "uma",
        "por", "para",
        "que", "qual", "quais",
        "como", "quando", "onde",
        "me", "mostrar",
        "mostrarme",
        "quero",
        "gostaria",
        "é",
        "foi",
        "será"
    }

    def optimize(
        self,
        question: str,
        source: KnowledgeSource
    ) -> str:

        text = question.lower().strip()

        text = re.sub(
            r"[?!.:,;]",
            "",
            text
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        if source == KnowledgeSource.ENERGY:

            return self._energy_query(text)

        if source == KnowledgeSource.EQUIPMENT:

            return self._equipment_query(text)

        if source == KnowledgeSource.SUPABASE:

            return self._supabase_query(text)

        return self._internet_query(text)

    def _internet_query(self, text):

        if "presidente" in text and "brasil" in text:

            return "presidente atual brasil site:gov.br"

        return self._keywords(text)

    def _energy_query(self, text):

        keywords = self._keywords(text)

        return (
            f"{keywords} "
            "site:aneel.gov.br "
            "OR site:gov.br "
            "OR site:ons.org.br"
        )

    def _equipment_query(self, text):

        keywords = self._keywords(text)

        return f"{keywords} datasheet PDF"

    def _supabase_query(self, text):

        # Futuramente não pesquisará na internet.
        # O SearchManager chamará o SupabaseProvider.

        return self._keywords(text)

    def _keywords(self, text):

        words = []

        for word in text.split():

            if word in self.STOPWORDS:
                continue

            if len(word) <= 2:
                continue

            words.append(word)

        return " ".join(words)