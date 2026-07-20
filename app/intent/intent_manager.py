"""
Versa AI

Arquivo:
intent_manager.py

Responsabilidade:
Orquestrar todas as operações relacionadas às intenções
identificadas pela Versa AI.

O IntentManager coordena o IntentService, oferecendo uma
interface única para o restante da aplicação.

Não implementa regras de negócio.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.intent.intent import Intent
from app.domain.entities.intent.intent_type import IntentType

from app.intent.repositories.base_intent_repository import (
    BaseIntentRepository,
)
from app.intent.repositories.in_memory_repository import (
    InMemoryIntentRepository,
)
from app.intent.services.intent_service import (
    IntentService,
)


class IntentManager:
    """
    Gerenciador responsável pelas operações de intenção.
    """

    def __init__(
        self,
        repository: BaseIntentRepository | None = None,
    ) -> None:
        """
        Inicializa o IntentManager.

        Args:
            repository:
                Repositório utilizado para persistência.
                Caso não informado, utiliza InMemoryIntentRepository.
        """

        self._repository = (
            repository
            if repository is not None
            else InMemoryIntentRepository()
        )

        self._service = IntentService(self._repository)

    @property
    def repository(self) -> BaseIntentRepository:
        """
        Retorna o repositório utilizado.
        """

        return self._repository

    @property
    def service(self) -> IntentService:
        """
        Retorna o serviço de intenções.
        """

        return self._service

    def remember(self, intent: Intent) -> None:
        """
        Armazena uma intenção.
        """

        self._service.remember(intent)

    def recall(self, intent_id: str) -> Intent | None:
        """
        Recupera uma intenção.
        """

        return self._service.recall(intent_id)

    def update(self, intent: Intent) -> None:
        """
        Atualiza uma intenção.
        """

        self._service.update(intent)

    def forget(self, intent_id: str) -> bool:
        """
        Remove uma intenção.
        """

        return self._service.forget(intent_id)

    def get_all(self) -> list[Intent]:
        """
        Retorna todas as intenções.
        """

        return self._service.get_all()

    def exists(self, intent_id: str) -> bool:
        """
        Verifica se uma intenção existe.
        """

        return self._service.exists(intent_id)

    def count(self) -> int:
        """
        Retorna a quantidade de intenções.
        """

        return self._service.count()

    def clear(self) -> None:
        """
        Remove todas as intenções.
        """

        self._service.clear()

    def find_by_type(
        self,
        intent_type: IntentType,
    ) -> list[Intent]:
        """
        Retorna intenções de um determinado tipo.
        """

        return self._service.find_by_type(intent_type)

    def find_by_confidence(
        self,
        minimum: float,
    ) -> list[Intent]:
        """
        Retorna intenções com confiança mínima.
        """

        return self._service.find_by_confidence(minimum)

    def find_by_text(
        self,
        text: str,
    ) -> list[Intent]:
        """
        Pesquisa intenções pelo texto informado.
        """

        return self._service.find_by_text(text)