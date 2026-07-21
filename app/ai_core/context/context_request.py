"""
===============================================================================
Versa AI

Context Request

Representa todos os dados necessários para construir um ContextPackage.

Este objeto é utilizado como entrada do ContextBuilder.

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ContextRequest:
    """
    Dados necessários para construção do ContextPackage.
    """

    memory: str | None = None
    knowledge: str | None = None
    conversation: str | None = None