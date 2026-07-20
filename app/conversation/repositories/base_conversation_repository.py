"""
Versa AI

Arquivo:
base_conversation_repository.py

Responsabilidade:
Definir o contrato para todos os repositórios de Conversation.

Autor: Raphael Wilson
"""

from __future__ import annotations

from abc import abstractmethod

from app.repository.base_repository import BaseRepository
from app.domain.entities.conversation.conversation import Conversation


class BaseConversationRepository(BaseRepository[Conversation]):
    """
    Contrato base para os repositórios de Conversation.
    """

    @abstractmethod
    def find_by_title(
        self,
        title: str,
    ) -> list[Conversation]:
        """
        Pesquisa conversas pelo título.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_metadata(
        self,
        key: str,
        value: str,
    ) -> list[Conversation]:
        """
        Pesquisa conversas por metadado.
        """
        raise NotImplementedError

    @abstractmethod
    def find_with_messages(self) -> list[Conversation]:
        """
        Retorna apenas conversas que possuem mensagens.
        """
        raise NotImplementedError