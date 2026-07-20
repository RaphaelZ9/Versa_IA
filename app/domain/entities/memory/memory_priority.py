"""
Versa AI

Arquivo:
memory_priority.py

Responsabilidade:
Definir os níveis de prioridade das memórias da Versa AI.

A prioridade determina a importância da memória e auxilia
na retenção, descarte e recuperação das informações.

Autor: Raphael Wilson
"""

from __future__ import annotations

from enum import Enum


class MemoryPriority(str, Enum):
    """
    Prioridades de memória suportadas pela Versa AI.
    """

    LOW = "low"
    """
    Memória de baixa importância.
    Pode ser descartada rapidamente.
    """

    NORMAL = "normal"
    """
    Prioridade padrão.
    """

    HIGH = "high"
    """
    Memória importante.
    Deve ser preservada sempre que possível.
    """

    CRITICAL = "critical"
    """
    Memória extremamente importante.
    Deve possuir prioridade máxima durante consultas.
    """

    PERMANENT = "permanent"
    """
    Memória permanente.

    Nunca deve ser removida automaticamente.
    """