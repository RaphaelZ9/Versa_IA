"""
Versa AI

Arquivo:
memory_manager.py

Responsabilidade:
Orquestrar todas as operações relacionadas à memória da
Versa AI.

O MemoryManager coordena o MemoryService, oferecendo uma
interface única para o restante da aplicação.

Não implementa regras de negócio.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.memory.memory import Memory

from app.memory.repositories.base_memory_repository import (
    BaseMemoryRepository,
)
from app.memory.repositories.in_memory_repository import (
    InMemoryRepository,
)
from app.memory.services.memory_service import MemoryService


class MemoryManager:
    """
    Gerenciador responsável pelas operações de memória.
    """

    def __init__(
        self,
        repository: BaseMemoryRepository | None = None,
    ) -> None:
        """
        Inicializa o MemoryManager.

        Args:
            repository:
                Repositório utilizado para persistência.
                Caso não informado, utiliza InMemoryRepository.
        """

        self._repository = (
            repository
            if repository is not None
            else InMemoryRepository()
        )

        self._service = MemoryService(self._repository)

    @property
    def repository(self) -> BaseMemoryRepository:
        """
        Retorna o repositório utilizado.
        """

        return self._repository

    @property
    def service(self) -> MemoryService:
        """
        Retorna o serviço de memória.
        """

        return self._service

    def remember(self, memory: Memory) -> None:
        """
        Armazena uma memória.
        """

        self._service.remember(memory)

    def recall(self, memory_id: str) -> Memory | None:
        """
        Recupera uma memória.
        """

        return self._service.recall(memory_id)

    def update(self, memory: Memory) -> None:
        """
        Atualiza uma memória.
        """

        self._service.update(memory)

    def forget(self, memory_id: str) -> bool:
        """
        Remove uma memória.
        """

        return self._service.forget(memory_id)

    def get_all(self) -> list[Memory]:
        """
        Retorna todas as memórias.
        """

        return self._service.get_all()

    def exists(self, memory_id: str) -> bool:
        """
        Verifica se uma memória existe.
        """

        return self._service.exists(memory_id)

    def count(self) -> int:
        """
        Retorna a quantidade de memórias.
        """

        return self._service.count()

    def clear(self) -> None:
        """
        Remove todas as memórias.
        """

        self._service.clear()

    def cleanup_expired(self) -> int:
        """
        Remove memórias expiradas.

        Returns:
            Quantidade de memórias removidas.
        """

        return self._service.cleanup_expired()