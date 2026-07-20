"""
Versa AI

Arquivo:
base_memory_repository.py

Responsabilidade:
Definir o contrato base para todos os repositórios de memória
da Versa AI.

Especializa o BaseRepository para trabalhar com a entidade
Memory.

Esta classe não implementa regras de negócio.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.domain.entities.memory.memory import Memory
from app.repository.base_repository import BaseRepository


class BaseMemoryRepository(BaseRepository[Memory]):
    """
    Contrato base para todos os repositórios de memória.

    Herdando de BaseRepository, todos os métodos comuns
    (save, update, delete, get_by_id, get_all, exists,
    count e clear) já fazem parte do contrato.

    Caso surjam operações específicas de memória no futuro,
    elas deverão ser adicionadas nesta classe.
    """

    pass