"""
Versa AI

Arquivo:
internet_provider.py

Responsabilidade:
Implementar o Provider responsável por realizar pesquisas
na Internet.

Este Provider atua como um adaptador entre o
KnowledgeManager e os mecanismos de pesquisa disponíveis.

Sua responsabilidade é apenas pesquisar e retornar
informações obtidas na Internet.

Não realiza ranking, filtragem ou processamento dos
resultados retornados.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.search_result import SearchResult
from app.knowledge.providers.base_provider import BaseProvider


class InternetProvider(BaseProvider):
    """
    Provider responsável por pesquisas na Internet.
    """

    def __init__(self) -> None:
        """
        Inicializa o Provider.
        """

        super().__init__(
            provider_id="internet",
            name="Internet Provider",
            description="Provider responsável por pesquisas na Internet.",
            provider_type="internet",
            priority=100,
        )

    def search(self, query: str) -> SearchResult:
        """
        Realiza uma pesquisa na Internet.

        Args:
            query:
                Consulta a ser pesquisada.

        Returns:
            SearchResult contendo os resultados encontrados.
        """

        self._logger.info(f"Pesquisando na Internet: {query}")

        #
        # A integração com mecanismos de pesquisa
        # será implementada futuramente.
        #

        return SearchResult(
            success=True,
            source=self.provider_type,
            execution_time=0.0,
        )