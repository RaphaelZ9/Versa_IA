"""
===============================================================================
Versa AI

Company Provider

Responsável por fornecer o contexto institucional da empresa para o
ContextBuilder.

===============================================================================
"""

from __future__ import annotations

from app.ai_core.context.company_context import CompanyContext

from .base_context_provider import BaseContextProvider


class CompanyProvider(BaseContextProvider):
    """
    Provider responsável pelo contexto institucional da empresa.
    """

    def __init__(self) -> None:
        self._company_context = CompanyContext()

    def build(self) -> str:
        """
        Retorna o contexto institucional.

        Returns
        -------
        str
            Texto contendo o contexto institucional da empresa.
        """
        return self._company_context.build()