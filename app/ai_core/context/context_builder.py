"""
===============================================================================
Versa AI

Context Builder

Responsável por montar um ContextPackage a partir dos Context Providers.

O ContextBuilder não conhece as implementações concretas dos contextos.
Ele apenas solicita que cada Provider construa sua parte do contexto.

===============================================================================
"""

from __future__ import annotations

from app.ai_core.context.context_package import ContextPackage
from app.ai_core.context.context_request import ContextRequest
from app.ai_core.context.providers import (
    CompanyProvider,
    ConversationProvider,
    KnowledgeProvider,
    MemoryProvider,
    SystemProvider,
)


class ContextBuilder:
    """
    Responsável por construir um ContextPackage.
    """

    def __init__(self) -> None:
        self._system_provider = SystemProvider()
        self._company_provider = CompanyProvider()

    def build(
        self,
        request: ContextRequest,
    ) -> ContextPackage:
        """
        Constrói um ContextPackage utilizando os Providers disponíveis.
        """

        memory_provider = MemoryProvider(request.memory)
        conversation_provider = ConversationProvider(request.conversation)
        knowledge_provider = KnowledgeProvider(request.knowledge)

        return ContextPackage(
            system_prompt=self._system_provider.build(),
            company_context=self._company_provider.build(),
            memory=memory_provider.build(),
            knowledge=knowledge_provider.build(),
            conversation=conversation_provider.build(),
        )