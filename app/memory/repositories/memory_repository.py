"""
Versa AI

Arquivo:
in_memory_repository.py

Responsabilidade:
Implementar um repositório de memória em memória (RAM).

Esta implementação é utilizada durante o desenvolvimento,
testes e execução local da Versa AI, não realizando qualquer
persistência em banco de dados.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.memory.memory import Memory
from app.memory.repositories.base_memory_repository import (
    BaseMemoryRepository,
)


class InMemoryRepository(BaseMemoryRepository):
    """
    Implementação de repositório utilizando memória RAM.
    """

    def __init__(self) -> None:
        """
        Inicializa o repositório.
        """

        self._memories: dict[str, Memory] = {}

    def save(self, memory: Memory) -> None:
        """
        Persiste uma memória.
        """

        self._memories[memory.id] = memory

    def update(self, memory: Memory) -> None:
        """
        Atualiza uma memória existente.
        """

        self._memories[memory.id] = memory

    def delete(self, memory_id: str) -> bool:
        """
        Remove uma memória.

        Returns:
            True caso a memória tenha sido removida.
        """

        if memory_id in self._memories:
            del self._memories[memory_id]
            return True

        return False

    def get_by_id(self, memory_id: str) -> Memory | None:
        """
        Retorna uma memória pelo identificador.
        """

        return self._memories.get(memory_id)

    def get_all(self) -> list[Memory]:
        """
        Retorna todas as memórias armazenadas.
        """

        return list(self._memories.values())

    def exists(self, memory_id: str) -> bool:
        """
        Verifica se uma memória existe.
        """

        return memory_id in self._memories

    def count(self) -> int:
        """
        Retorna a quantidade de memórias armazenadas.
        """

        return len(self._memories)

    def clear(self) -> None:
        """
        Remove todas as memórias.
        """

        self._memories.clear()