"""
Versa AI

Arquivo:
api_provider.py

Responsabilidade:
Implementar o Provider responsável por realizar consultas
em APIs externas.

Este Provider atua como um adaptador entre o
KnowledgeManager e serviços REST, SOAP ou qualquer outra
API suportada pela Versa AI.

Sua responsabilidade é apenas consultar APIs e retornar
os resultados encontrados.

Não realiza ranking, filtragem ou processamento dos
resultados retornados.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.search_result import SearchResult
from app.knowledge.providers.base_provider import BaseProvider


class APIProvider(BaseProvider):
    """
    Provider responsável por consultas em APIs externas.
    """

    def __init__(self) -> None:
        """
        Inicializa o Provider.
        """

        super().__init__(
            provider_id="api",
            name="API Provider",
            description="Provider responsável por consultas em APIs externas.",
            provider_type="api",
            priority=80,
        )

    def search(self, query: str) -> SearchResult:
        """
        Realiza uma consulta em uma API externa.

        Args:
            query:
                Consulta a ser executada.

        Returns:
            SearchResult contendo os resultados encontrados.
        """

        self._logger.info(f"Consultando API: {query}")

        #
        # A integração com APIs REST/SOAP será implementada
        # em uma etapa futura.
        #

        return SearchResult(
            success=True,
            source=self.provider_type,
            execution_time=0.0,
        )