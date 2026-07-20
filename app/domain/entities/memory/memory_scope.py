"""
Versa AI

Arquivo:
memory_scope.py

Responsabilidade:
Definir o escopo das memórias utilizadas pela Versa AI.

O escopo determina a quem ou a que contexto uma memória
pertence e quem poderá utilizá-la.

Autor: Raphael Wilson
"""

from __future__ import annotations

from enum import Enum


class MemoryScope(str, Enum):
    """
    Escopos de memória suportados pela Versa AI.
    """

    GLOBAL = "global"
    """
    Memória compartilhada por toda a aplicação.
    """

    SYSTEM = "system"
    """
    Memória utilizada exclusivamente pelo sistema.
    """

    USER = "user"
    """
    Memória pertencente a um usuário específico.
    """

    SESSION = "session"
    """
    Memória válida apenas durante uma sessão.
    """

    PROJECT = "project"
    """
    Memória relacionada a um projeto específico.
    """

    WORKFLOW = "workflow"
    """
    Memória utilizada durante a execução de um workflow.
    """