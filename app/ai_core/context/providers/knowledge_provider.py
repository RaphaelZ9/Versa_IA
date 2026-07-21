"""
===============================================================================
Versa AI

Knowledge Provider

Responsável por fornecer o contexto de conhecimento para o ContextBuilder.

Este provider não consulta repositórios, bancos de dados ou serviços.
Ele recebe um conhecimento já preparado e o disponibiliza como texto de
contexto.

===============================================================================
"""

from __future__ import annotations

from .base_context_provider import BaseContextProvider


class KnowledgeProvider(BaseContextProvider):
    """
    Provider responsável por fornecer o contexto de conhecimento.
    """

    def __init__(
        self,
        knowledge: str | None = None,
    ) -> None:
        self._context = knowledge

    def build(self) -> str:
        """
        Retorna o conhecimento disponível para a requisição atual.
        """

        return self._context or ""