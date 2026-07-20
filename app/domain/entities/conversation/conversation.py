"""
Versa AI

Arquivo:
conversation.py

Responsabilidade:
Representar uma conversa composta por diversas mensagens.

Autor: Raphael Wilson
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from app.core.time_utils import utc_now
from app.domain.entities.conversation.message import Message


@dataclass
class Conversation:
    """
    Representa uma conversa da Versa AI.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    title: str = ""

    messages: list[Message] = field(default_factory=list)

    metadata: dict[str, str] = field(default_factory=dict)

    created_at: datetime = field(default_factory=utc_now)

    updated_at: datetime = field(default_factory=utc_now)

    def add_message(
        self,
        message: Message,
    ) -> None:
        """
        Adiciona uma mensagem à conversa.
        """

        self.messages.append(message)
        self.updated_at = utc_now()

    def remove_message(
        self,
        message_id: str,
    ) -> bool:
        """
        Remove uma mensagem pelo identificador.

        Returns:
            True caso encontrada.
        """

        for message in self.messages:
            if message.id == message_id:
                self.messages.remove(message)
                self.updated_at = utc_now()
                return True

        return False

    def clear_messages(self) -> None:
        """
        Remove todas as mensagens.
        """

        self.messages.clear()
        self.updated_at = utc_now()

    @property
    def message_count(self) -> int:
        """
        Retorna a quantidade de mensagens.
        """

        return len(self.messages)

    @property
    def is_empty(self) -> bool:
        """
        Indica se a conversa está vazia.
        """

        return len(self.messages) == 0

    def add_metadata(
        self,
        key: str,
        value: str,
    ) -> None:
        """
        Adiciona um metadado.
        """

        self.metadata[key] = value
        self.updated_at = utc_now()

    def clear_metadata(self) -> None:
        """
        Remove todos os metadados.
        """

        self.metadata.clear()
        self.updated_at = utc_now()

    @property
    def has_metadata(self) -> bool:
        """
        Indica se existem metadados.
        """

        return len(self.metadata) > 0

    def last_message(self) -> Message | None:
        """
        Retorna a última mensagem da conversa.
        """

        if self.is_empty:
            return None

        return self.messages[-1]

    def to_dict(self) -> dict:
        """
        Converte a conversa para um dicionário.
        """

        return {
            "id": self.id,
            "title": self.title,
            "messages": [
                message.to_dict()
                for message in self.messages
            ],
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }