"""
Versa AI

Arquivo:
memory.py

Responsabilidade:
Representar uma memória da Versa AI.

A memória é a unidade básica de conhecimento utilizada pela IA,
podendo armazenar informações temporárias, permanentes,
preferências, conhecimento corporativo ou contexto de conversação.

Autor: Raphael Wilson
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from app.core.time_utils import utc_now
from typing import Any
from uuid import uuid4

from app.domain.entities.memory.memory_priority import MemoryPriority
from app.domain.entities.memory.memory_scope import MemoryScope
from app.domain.entities.memory.memory_type import MemoryType


@dataclass(slots=True)
class Memory:
    """
    Representa uma memória da Versa AI.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    title: str = ""

    content: str = ""

    memory_type: MemoryType = MemoryType.WORKING

    scope: MemoryScope = MemoryScope.SESSION

    priority: MemoryPriority = MemoryPriority.NORMAL

    metadata: dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(default_factory=utc_now)

    updated_at: datetime = field(default_factory=utc_now)

    expires_at: datetime | None = None

    created_by: str = "system"

    source: str = ""

    tags: list[str] = field(default_factory=list)

    @property
    def is_expired(self) -> bool:
        """
        Verifica se a memória expirou.
        """

        if self.expires_at is None:
            return False

        return utc_now() >= self.expires_at

    @property
    def is_permanent(self) -> bool:
        """
        Indica se a memória é permanente.
        """

        return self.priority == MemoryPriority.PERMANENT

    @property
    def has_tags(self) -> bool:
        """
        Indica se existem tags associadas.
        """

        return len(self.tags) > 0

    def add_tag(self, tag: str) -> None:
        """
        Adiciona uma tag.
        """

        if tag not in self.tags:

            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        """
        Remove uma tag.
        """

        if tag in self.tags:

            self.tags.remove(tag)

    def update_content(self, content: str) -> None:
        """
        Atualiza o conteúdo da memória.
        """

        self.content = content

        self.updated_at = utc_now()

    def touch(self) -> None:
        """
        Atualiza apenas a data da última modificação.
        """

        self.updated_at = utc_now()