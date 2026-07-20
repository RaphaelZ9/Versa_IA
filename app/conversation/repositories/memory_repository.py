"""
Versa AI

Arquivo:
in_memory_repository.py

Responsabilidade:
Implementar um repositório de conversas utilizando memória RAM.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.conversation.repositories.base_conversation_repository import (
    BaseConversationRepository,
)
from app.domain.entities.conversation.conversation import Conversation


class MemoryConversationRepository(BaseConversationRepository):
    """
    Implementação em memória do repositório de conversas.
    """

    def __init__(self) -> None:
        """
        Inicializa o repositório.
        """

        self._conversations: dict[str, Conversation] = {}

    def save(
        self,
        conversation: Conversation,
    ) -> None:
        """
        Armazena uma conversa.
        """

        self._conversations[conversation.id] = conversation

    def update(
        self,
        conversation: Conversation,
    ) -> None:
        """
        Atualiza uma conversa.
        """

        self._conversations[conversation.id] = conversation

    def delete(
        self,
        conversation_id: str,
    ) -> bool:
        """
        Remove uma conversa.

        Returns:
            True caso encontrada.
        """

        if conversation_id in self._conversations:
            del self._conversations[conversation_id]
            return True

        return False

    def get_by_id(
        self,
        conversation_id: str,
    ) -> Conversation | None:
        """
        Recupera uma conversa pelo identificador.
        """

        return self._conversations.get(conversation_id)

    def get_all(self) -> list[Conversation]:
        """
        Retorna todas as conversas.
        """

        return list(self._conversations.values())

    def exists(
        self,
        conversation_id: str,
    ) -> bool:
        """
        Verifica se a conversa existe.
        """

        return conversation_id in self._conversations

    def count(self) -> int:
        """
        Retorna a quantidade de conversas.
        """

        return len(self._conversations)

    def clear(self) -> None:
        """
        Remove todas as conversas.
        """

        self._conversations.clear()

    def find_by_title(
        self,
        title: str,
    ) -> list[Conversation]:
        """
        Pesquisa conversas pelo título.
        """

        title = title.lower()

        return [
            conversation
            for conversation in self._conversations.values()
            if title in conversation.title.lower()
        ]

    def find_by_metadata(
        self,
        key: str,
        value: str,
    ) -> list[Conversation]:
        """
        Pesquisa conversas por metadado.
        """

        return [
            conversation
            for conversation in self._conversations.values()
            if conversation.metadata.get(key) == value
        ]

    def find_with_messages(self) -> list[Conversation]:
        """
        Retorna conversas que possuem mensagens.
        """

        return [
            conversation
            for conversation in self._conversations.values()
            if conversation.message_count > 0
        ]