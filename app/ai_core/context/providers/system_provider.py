"""
===============================================================================
Versa AI

System Provider

Responsável por fornecer o System Prompt para o ContextBuilder.

===============================================================================
"""

from __future__ import annotations

from app.ai_core.prompt.system_prompt import SystemPrompt

from .base_context_provider import BaseContextProvider


class SystemProvider(BaseContextProvider):
    """
    Provider responsável pelo System Prompt.
    """

    def __init__(self) -> None:
        self._system_prompt = SystemPrompt()

    def build(self) -> str:
        return self._system_prompt.build()