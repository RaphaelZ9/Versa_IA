from app.domain.entities.search_result import SearchResult


class ContextExtractor:

    def extract(self, result: SearchResult) -> str:

        if result is None:
            return ""

        if not result.has_documents:
            return ""

        contexto = []

        for documento in result.documents:

            trecho = documento.content.strip()

            if not trecho:
                continue

            contexto.append(
                f"""
Fonte: {documento.title}

{trecho}

URL:
{documento.url}
"""
            )

        return "\n\n".join(contexto)