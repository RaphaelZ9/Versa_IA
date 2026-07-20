"""
Versa AI

Arquivo:
message.py

Responsabilidade:
Representar uma mensagem pertencente a uma conversa.

Uma mensagem pode ser enviada pelo usuário, pela IA,
pelo sistema ou por uma ferramenta.

Autor: Raphael Wilson
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from app.core.time_utils import utc_now


@dataclass
class Message:
    """
    Representa uma mensagem de uma conversa.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    role: str = "user"

    content: str = ""

    metadata: dict[str, str] = field(default_factory=dict)

    created_at: datetime = field(default_factory=utc_now)

    def add_metadata(
        self,
        key: str,
        value: str,
    ) -> None:
        """
        Adiciona um metadado à mensagem.
        """

        self.metadata[key] = value

    def remove_metadata(
        self,
        key: str,
    ) -> None:
        """
        Remove um metadado da mensagem.
        """

        self.metadata.pop(key, None)

    def clear_metadata(self) -> None:
        """
        Remove todos os metadados.
        """

        self.metadata.clear()

    @property
    def has_metadata(self) -> bool:
        """
        Indica se existem metadados associados.
        """

        return len(self.metadata) > 0

    def to_dict(self) -> dict:
        """
        Converte a mensagem para um dicionário.
        """

        return {
            "id": self.id,
            "role": self.role,
            "content": self.content,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }