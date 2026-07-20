"""
Versa AI

Arquivo:
intent.py

Responsabilidade:
Representar uma intenção identificada pela Versa AI.

Autor: Raphael Wilson
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from app.core.time_utils import utc_now
from app.domain.entities.intent.intent_type import IntentType


@dataclass
class Intent:
    """
    Representa uma intenção detectada durante uma interação.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    type: IntentType = IntentType.UNKNOWN

    text: str = ""

    confidence: float = 0.0

    entities: dict[str, str] = field(default_factory=dict)

    suggested_tools: list[str] = field(default_factory=list)

    metadata: dict[str, str] = field(default_factory=dict)

    created_at: datetime = field(default_factory=utc_now)

    def is_unknown(self) -> bool:
        """
        Verifica se a intenção ainda não foi identificada.
        """

        return self.type == IntentType.UNKNOWN

    def add_entity(self, key: str, value: str) -> None:
        """
        Adiciona uma entidade identificada.
        """

        self.entities[key] = value

    def add_tool(self, tool_name: str) -> None:
        """
        Adiciona uma ferramenta sugerida.
        """

        if tool_name not in self.suggested_tools:
            self.suggested_tools.append(tool_name)

    def add_metadata(self, key: str, value: str) -> None:
        """
        Adiciona uma informação complementar.
        """

        self.metadata[key] = value

    def clear_entities(self) -> None:
        """
        Remove todas as entidades.
        """

        self.entities.clear()

    def clear_tools(self) -> None:
        """
        Remove todas as ferramentas sugeridas.
        """

        self.suggested_tools.clear()

    def clear_metadata(self) -> None:
        """
        Remove todos os metadados.
        """

        self.metadata.clear()

    @property
    def has_entities(self) -> bool:
        """
        Verifica se existem entidades identificadas.
        """

        return len(self.entities) > 0

    @property
    def has_tools(self) -> bool:
        """
        Verifica se existem ferramentas sugeridas.
        """

        return len(self.suggested_tools) > 0

    def to_dict(self) -> dict:
        """
        Converte a intenção para dicionário.
        """

        return {
            "id": self.id,
            "type": self.type.value,
            "text": self.text,
            "confidence": self.confidence,
            "entities": self.entities,
            "suggested_tools": self.suggested_tools,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }