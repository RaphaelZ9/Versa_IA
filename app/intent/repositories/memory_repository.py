"""
Versa AI

Arquivo:
in_memory_repository.py

Responsabilidade:
Implementar um repositório de intenções em memória (RAM).

Esta implementação é utilizada durante o desenvolvimento,
testes e execução local da Versa AI.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.intent.intent import Intent
from app.domain.entities.intent.intent_type import IntentType
from app.intent.repositories.base_intent_repository import (
    BaseIntentRepository,
)


class InMemoryIntentRepository(BaseIntentRepository):
    """
    Implementação de repositório utilizando memória RAM.
    """

    def __init__(self) -> None:
        """
        Inicializa o repositório.
        """

        self._intents: dict[str, Intent] = {}

    def save(self, intent: Intent) -> None:
        """
        Persiste uma intenção.
        """

        self._intents[intent.id] = intent

    def update(self, intent: Intent) -> None:
        """
        Atualiza uma intenção.
        """

        self._intents[intent.id] = intent

    def delete(self, intent_id: str) -> bool:
        """
        Remove uma intenção.

        Returns:
            True caso removida.
        """

        if intent_id in self._intents:
            del self._intents[intent_id]
            return True

        return False

    def get_by_id(self, intent_id: str) -> Intent | None:
        """
        Recupera uma intenção pelo identificador.
        """

        return self._intents.get(intent_id)

    def get_all(self) -> list[Intent]:
        """
        Retorna todas as intenções.
        """

        return list(self._intents.values())

    def exists(self, intent_id: str) -> bool:
        """
        Verifica se uma intenção existe.
        """

        return intent_id in self._intents

    def count(self) -> int:
        """
        Retorna a quantidade de intenções.
        """

        return len(self._intents)

    def clear(self) -> None:
        """
        Remove todas as intenções.
        """

        self._intents.clear()

    def find_by_type(
        self,
        intent_type: IntentType,
    ) -> list[Intent]:
        """
        Retorna todas as intenções de um determinado tipo.
        """

        return [
            intent
            for intent in self._intents.values()
            if intent.type == intent_type
        ]

    def find_by_confidence(
        self,
        minimum: float,
    ) -> list[Intent]:
        """
        Retorna intenções cuja confiança é maior ou igual
        ao valor informado.
        """

        return [
            intent
            for intent in self._intents.values()
            if intent.confidence >= minimum
        ]

    def find_by_text(
        self,
        text: str,
    ) -> list[Intent]:
        """
        Pesquisa intenções cujo texto contenha o valor informado.
        A comparação é case-insensitive.
        """

        text = text.lower()

        return [
            intent
            for intent in self._intents.values()
            if text in intent.text.lower()
        ]