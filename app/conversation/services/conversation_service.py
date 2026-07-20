"""
Versa AI

Arquivo:
conversation_service.py

Responsabilidade:
Implementar as regras de negócio relacionadas às conversas.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.conversation.repositories.base_conversation_repository import (
    BaseConversationRepository,
)
from app.domain.entities.conversation.conversation import Conversation
from app.domain.entities.conversation.message import Message


class ConversationService:
    """
    Serviço responsável pelas regras de negócio das conversas.
    """

    def __init__(
        self,
        repository: BaseConversationRepository,
    ) -> None:
        """
        Inicializa o serviço.

        Args:
            repository:
                Repositório utilizado para persistência.
        """

        self._repository = repository

    def remember(
        self,
        conversation: Conversation,
    ) -> None:
        """
        Armazena uma conversa.
        """

        self._repository.save(conversation)

    def recall(
        self,
        conversation_id: str,
    ) -> Conversation | None:
        """
        Recupera uma conversa.
        """

        return self._repository.get_by_id(conversation_id)

    def update(
        self,
        conversation: Conversation,
    ) -> None:
        """
        Atualiza uma conversa.
        """

        self._repository.update(conversation)

    def forget(
        self,
        conversation_id: str,
    ) -> bool:
        """
        Remove uma conversa.
        """

        return self._repository.delete(conversation_id)

    def get_all(self) -> list[Conversation]:
        """
        Retorna todas as conversas.
        """

        return self._repository.get_all()

    def exists(
        self,
        conversation_id: str,
    ) -> bool:
        """
        Verifica se a conversa existe.
        """

        return self._repository.exists(conversation_id)

    def count(self) -> int:
        """
        Retorna a quantidade de conversas.
        """

        return self._repository.count()

    def clear(self) -> None:
        """
        Remove todas as conversas.
        """

        self._repository.clear()

    def find_by_title(
        self,
        title: str,
    ) -> list[Conversation]:
        """
        Pesquisa conversas pelo título.
        """

        return self._repository.find_by_title(title)

    def find_by_metadata(
        self,
        key: str,
        value: str,
    ) -> list[Conversation]:
        """
        Pesquisa conversas por metadado.
        """

        return self._repository.find_by_metadata(key, value)

    def find_with_messages(self) -> list[Conversation]:
        """
        Retorna apenas conversas que possuem mensagens.
        """

        return self._repository.find_with_messages()

    # ==========================================================
    # Operações específicas do domínio Conversation
    # ==========================================================

    def append_message(
        self,
        conversation_id: str,
        message: Message,
    ) -> bool:
        """
        Adiciona uma mensagem à conversa.

        Returns:
            True caso a conversa exista.
        """

        conversation = self.recall(conversation_id)

        if conversation is None:
            return False

        conversation.add_message(message)

        self.update(conversation)

        return True

    def last_message(
        self,
        conversation_id: str,
    ) -> Message | None:
        """
        Retorna a última mensagem da conversa.
        """

        conversation = self.recall(conversation_id)

        if conversation is None:
            return None

        return conversation.last_message()

    def message_count(
        self,
        conversation_id: str,
    ) -> int:
        """
        Retorna a quantidade de mensagens.
        """

        conversation = self.recall(conversation_id)

        if conversation is None:
            return 0

        return conversation.message_count

    def clear_messages(
        self,
        conversation_id: str,
    ) -> bool:
        """
        Remove todas as mensagens da conversa.

        Returns:
            True caso a conversa exista.
        """

        conversation = self.recall(conversation_id)

        if conversation is None:
            return False

        conversation.clear_messages()

        self.update(conversation)

        return True