"""
===============================================================================
Versa AI

Conversation Provider

Responsável por fornecer o contexto da conversa para o ContextBuilder.

Este provider não consulta repositórios, bancos de dados ou serviços.
Ele recebe uma conversa já preparada e a disponibiliza como texto de contexto.

===============================================================================
"""

from __future__ import annotations

from .base_context_provider import BaseContextProvider


class ConversationProvider(BaseContextProvider):
    """
    Provider responsável por fornecer o contexto da conversa.
    """

    def __init__(
        self,
        conversation: str | None = None,
    ) -> None:
        self._context = conversation

    def build(self) -> str:
        """
        Retorna a conversa disponível para a requisição atual.
        """

        return self._context or ""