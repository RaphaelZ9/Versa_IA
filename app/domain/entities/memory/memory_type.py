"""
Versa AI

Arquivo:
memory_type.py

Responsabilidade:
Definir os tipos de memória utilizados pela Versa AI.

Os tipos de memória representam a finalidade e o ciclo
de vida das informações armazenadas pelo sistema.

Autor: Raphael Wilson
"""

from __future__ import annotations

from enum import Enum


class MemoryType(str, Enum):
    """
    Tipos de memória suportados pela Versa AI.
    """

    WORKING = "working"
    """
    Memória temporária utilizada durante a execução
    de uma tarefa ou workflow.
    """

    CONVERSATION = "conversation"
    """
    Memória relacionada ao histórico da conversa
    atual com o usuário.
    """

    KNOWLEDGE = "knowledge"
    """
    Memória proveniente da base de conhecimento
    corporativa.
    """

    LONG_TERM = "long_term"
    """
    Memória persistente utilizada para armazenar
    informações relevantes por longo período.
    """

    PREFERENCE = "preference"
    """
    Preferências aprendidas pela Versa AI.
    """

    SYSTEM = "system"
    """
    Informações internas utilizadas pela própria
    Versa AI.
    """