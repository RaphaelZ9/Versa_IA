"""
===============================================================================
Versa AI

Base Context Provider

Define o contrato de todos os providers responsáveis por fornecer partes do
contexto utilizado pelo ContextBuilder.

Exemplos:

- SystemProvider
- CompanyProvider
- MemoryProvider
- KnowledgeProvider
- ConversationProvider

Cada provider possui uma única responsabilidade:
construir e retornar seu contexto.

===============================================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseContextProvider(ABC):
    """
    Classe base para todos os Context Providers.
    """

    @abstractmethod
    def build(self) -> str:
        """
        Constrói e retorna o contexto deste provider.

        Returns
        -------
        str
            Texto que será incorporado ao ContextPackage.
        """
        raise NotImplementedError