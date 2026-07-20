"""
===============================================================================
Versa AI

Memory Provider

Responsável por fornecer o contexto de memória para o ContextBuilder.

Este provider não consulta repositórios, bancos de dados ou serviços.
Ele recebe uma memória já preparada e a disponibiliza como texto de contexto.

===============================================================================
"""

from __future__ import annotations

from .base_context_provider import BaseContextProvider


class MemoryProvider(BaseContextProvider):
    """
    Provider responsável por fornecer o contexto de memória.
    """

    def __init__(
        self,
        memory: str | None = None,
    ) -> None:
        self._memory = memory

    def build(self) -> str:
        """
        Retorna a memória disponível para a requisição atual.
        """

        if self._memory is None:
            return ""

        return self._memory