"""
Versa AI

Arquivo:
intent_service.py

Responsabilidade:
Implementar as regras de negócio relacionadas às intenções
identificadas pela Versa AI.

O IntentService é responsável pelo gerenciamento das
intenções utilizando um repositório para persistência.

Esta classe não conhece detalhes de infraestrutura.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.intent.intent import Intent
from app.domain.entities.intent.intent_type import IntentType
from app.intent.repositories.base_intent_repository import (
    BaseIntentRepository,
)


class IntentService:
    """
    Serviço responsável pelas regras de negócio das intenções.
    """

    def __init__(
        self,
        repository: BaseIntentRepository,
    ) -> None:
        """
        Inicializa o serviço.

        Args:
            repository:
                Repositório utilizado para persistência.
        """

        self._repository = repository

    def remember(self, intent: Intent) -> None:
        """
        Armazena uma intenção.
        """

        self._repository.save(intent)

    def recall(self, intent_id: str) -> Intent | None:
        """
        Recupera uma intenção pelo identificador.
        """

        return self._repository.get_by_id(intent_id)

    def update(self, intent: Intent) -> None:
        """
        Atualiza uma intenção.
        """

        self._repository.update(intent)

    def forget(self, intent_id: str) -> bool:
        """
        Remove uma intenção.

        Returns:
            True caso removida.
        """

        return self._repository.delete(intent_id)

    def get_all(self) -> list[Intent]:
        """
        Retorna todas as intenções.
        """

        return self._repository.get_all()

    def exists(self, intent_id: str) -> bool:
        """
        Verifica se uma intenção existe.
        """

        return self._repository.exists(intent_id)

    def count(self) -> int:
        """
        Retorna a quantidade de intenções.
        """

        return self._repository.count()

    def clear(self) -> None:
        """
        Remove todas as intenções.
        """

        self._repository.clear()

    def find_by_type(
        self,
        intent_type: IntentType,
    ) -> list[Intent]:
        """
        Retorna intenções de um determinado tipo.
        """

        return self._repository.find_by_type(intent_type)

    def find_by_confidence(
        self,
        minimum: float,
    ) -> list[Intent]:
        """
        Retorna intenções com confiança mínima.
        """

        return self._repository.find_by_confidence(minimum)

    def find_by_text(
        self,
        text: str,
    ) -> list[Intent]:
        """
        Pesquisa intenções pelo texto informado.
        """

        return self._repository.find_by_text(text)