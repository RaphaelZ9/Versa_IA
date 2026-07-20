"""
Versa AI

Arquivo:
email_provider.py

Responsabilidade:
Implementar o Provider responsável por realizar consultas
a caixas de e-mail corporativas.

Este Provider atua como um adaptador entre o
KnowledgeManager e provedores de e-mail, permitindo
consultar mensagens, anexos e informações relacionadas.

Sua responsabilidade é apenas consultar mensagens e
retornar os resultados encontrados.

Não realiza download de anexos, processamento de PDFs
ou execução de automações. Essas responsabilidades
pertencem às respectivas Tools.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.search_result import SearchResult
from app.knowledge.providers.base_provider import BaseProvider


class EmailProvider(BaseProvider):
    """
    Provider responsável por consultas em caixas de e-mail.
    """

    def __init__(self) -> None:
        """
        Inicializa o Provider.
        """

        super().__init__(
            provider_id="email",
            name="Email Provider",
            description="Provider responsável por consultas em caixas de e-mail.",
            provider_type="email",
            priority=85,
        )

    def search(self, query: str) -> SearchResult:
        """
        Realiza uma consulta em mensagens de e-mail.

        Args:
            query:
                Consulta a ser executada.

        Returns:
            SearchResult contendo os resultados encontrados.
        """

        self._logger.info(f"Consultando e-mails: {query}")

        #
        # A integração com Outlook / Microsoft Graph
        # será implementada futuramente.
        #

        return SearchResult(
            success=True,
            source=self.provider_type,
            execution_time=0.0,
        )