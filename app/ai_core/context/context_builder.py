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
from app.ai_core.context.providers import (
    CompanyProvider,
    MemoryProvider,
    SystemProvider,
)


class ContextBuilder:
    """
    Responsável por construir um ContextPackage.
    """

    def __init__(self) -> None:

        self.providers = {
            "system": SystemProvider(),
            "company": CompanyProvider(),
        }

    def build(
        self,
        *,
        memory: str | None = None,
        knowledge: str | None = None,
        conversation: str | None = None,
    ) -> ContextPackage:

        memory_provider = MemoryProvider(memory)

        return ContextPackage(

            system_prompt=self.providers["system"].build(),

            company_context=self.providers["company"].build(),

            memory=memory_provider.build(),

            knowledge=knowledge,

            conversation=conversation,
        )