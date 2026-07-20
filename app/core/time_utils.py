"""
===============================================================================
Versa AI

time_utils.py

Funções utilitárias para manipulação de datas.

===============================================================================
"""

from __future__ import annotations

from datetime import datetime, timezone


def utc_now() -> datetime:
    """
    Retorna a data/hora atual em UTC.
    """

    return datetime.now(timezone.utc)


def local_now() -> datetime:
    """
    Retorna a data/hora local.
    """

    return datetime.now()


def iso_now() -> str:
    """
    Retorna a data atual em formato ISO-8601 UTC.
    """

    return utc_now().isoformat()


def to_iso(dt: datetime) -> str:
    """
    Converte datetime para ISO.
    """

    return dt.isoformat()


def from_iso(value: str) -> datetime:
    """
    Converte ISO para datetime.
    """

    return datetime.fromisoformat(value)