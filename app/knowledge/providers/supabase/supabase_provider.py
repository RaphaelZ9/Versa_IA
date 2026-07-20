"""
Versa AI

Arquivo:
supabase_provider.py

Responsabilidade:
Implementar o Provider responsável por realizar consultas
ao banco de dados Supabase.

Este Provider atua como um adaptador entre o
KnowledgeManager e o Supabase, permitindo consultar
informações corporativas armazenadas no banco de dados.

Sua responsabilidade é apenas consultar dados e retornar
os resultados encontrados.

Não realiza ranking, filtragem ou processamento dos
resultados retornados.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.search_result import SearchResult
from app.knowledge.providers.base_provider import BaseProvider


class SupabaseProvider(BaseProvider):
    """
    Provider responsável por consultas ao Supabase.
    """

    def __init__(self) -> None:
        """
        Inicializa o Provider.
        """

        super().__init__(
            provider_id="supabase",
            name="Supabase Provider",
            description="Provider responsável por consultas ao banco de dados Supabase.",
            provider_type="supabase",
            priority=95,
        )

    def search(self, query: str) -> SearchResult:
        """
        Realiza uma consulta ao Supabase.

        Args:
            query:
                Consulta a ser executada.

        Returns:
            SearchResult contendo os resultados encontrados.
        """

        self._logger.info(f"Consultando Supabase: {query}")

        #
        # A integração com o banco Supabase será
        # implementada em uma etapa futura.
        #

        return SearchResult(
            success=True,
            source=self.provider_type,
            execution_time=0.0,
        )