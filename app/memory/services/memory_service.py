"""
Versa AI

Arquivo:
memory_service.py

Responsabilidade:
Implementar as regras de negócio relacionadas às memórias
da Versa AI.

O MemoryService é responsável pela manipulação das memórias,
utilizando um repositório para persistência dos dados.

Esta classe não conhece detalhes de infraestrutura
(Supabase, Redis, PostgreSQL etc.).

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.memory.memory import Memory
from app.memory.repositories.base_memory_repository import (
    BaseMemoryRepository,
)


class MemoryService:
    """
    Serviço responsável pelas regras de negócio da memória.
    """

    def __init__(
        self,
        repository: BaseMemoryRepository,
    ) -> None:
        """
        Inicializa o serviço.

        Args:
            repository:
                Repositório utilizado para persistência.
        """

        self._repository = repository

    def remember(self, memory: Memory) -> None:
        """
        Armazena uma memória.
        """

        self._repository.save(memory)

    def recall(self, memory_id: str) -> Memory | None:
        """
        Recupera uma memória.
        """

        return self._repository.get_by_id(memory_id)

    def update(self, memory: Memory) -> None:
        """
        Atualiza uma memória.
        """

        self._repository.update(memory)

    def forget(self, memory_id: str) -> bool:
        """
        Remove uma memória.

        Returns:
            True caso removida.
        """

        return self._repository.delete(memory_id)

    def get_all(self) -> list[Memory]:
        """
        Retorna todas as memórias.
        """

        return self._repository.get_all()

    def exists(self, memory_id: str) -> bool:
        """
        Verifica se a memória existe.
        """

        return self._repository.exists(memory_id)

    def count(self) -> int:
        """
        Retorna o total de memórias.
        """

        return self._repository.count()

    def clear(self) -> None:
        """
        Remove todas as memórias.
        """

        self._repository.clear()

    def cleanup_expired(self) -> int:
        """
        Remove memórias expiradas.

        Returns:
            Quantidade de memórias removidas.
        """

        removed = 0

        for memory in self.get_all():

            if memory.is_expired:

                self.forget(memory.id)

                removed += 1

        return removed