"""
Versa AI

Arquivo:
knowledge_manager.py

Responsabilidade:
Gerenciar todos os Providers responsáveis pelo acesso ao
conhecimento da Versa AI.

O KnowledgeManager atua como um orquestrador dos Providers,
registrando automaticamente as fontes de conhecimento
disponíveis e coordenando as pesquisas realizadas.

Sua responsabilidade é consolidar os resultados obtidos
pelos Providers em um único SearchResult.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.search_result import SearchResult

from app.managers.base_manager import BaseManager

from app.knowledge.providers.base_provider import BaseProvider

from app.knowledge.providers.internet.internet_provider import InternetProvider
from app.knowledge.providers.pdf.pdf_provider import PDFProvider
from app.knowledge.providers.api.api_provider import APIProvider
from app.knowledge.providers.supabase.supabase_provider import SupabaseProvider
from app.knowledge.providers.email.email_provider import EmailProvider


class KnowledgeManager(BaseManager):
    """
    Gerenciador responsável pelos Providers da Versa AI.
    """

    def __init__(self) -> None:

        super().__init__()

        self._load_default_providers()

    def _load_default_providers(self) -> None:
        """
        Carrega automaticamente os Providers padrão.
        """

        self.register_provider(InternetProvider())
        self.register_provider(PDFProvider())
        self.register_provider(APIProvider())
        self.register_provider(SupabaseProvider())
        self.register_provider(EmailProvider())

    def register_provider(self, provider: BaseProvider) -> None:
        """
        Registra um novo Provider.
        """

        provider.initialize()

        self.register(provider)

    def unregister_provider(self, provider: BaseProvider) -> None:
        """
        Remove um Provider.
        """

        provider.shutdown()

        self.unregister(provider)

    def get_provider(self, provider_id: str) -> BaseProvider | None:
        """
        Localiza um Provider pelo seu identificador.
        """

        provider = self.get(
            lambda component: getattr(component, "id", None) == provider_id
        )

        return provider

    def get_providers(self) -> list[BaseProvider]:
        """
        Retorna todos os Providers registrados.
        """

        return self.get_all()

    def search(self, query: str) -> SearchResult:
        """
        Executa uma pesquisa utilizando todos os Providers
        disponíveis.
        """

        self._logger.info(f"Pesquisando: {query}")

        result = SearchResult(
            success=True,
            source="knowledge_manager",
        )

        for provider in self.get_all():

            if not provider.is_available():
                continue

            provider_result = provider.search(query)

            result.documents.extend(provider_result.documents)

        return result

    def shutdown(self) -> None:
        """
        Finaliza todos os Providers registrados.
        """

        super().shutdown()