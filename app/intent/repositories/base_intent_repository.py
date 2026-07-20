"""
Versa AI

Arquivo:
base_intent_repository.py

Responsabilidade:
Definir o contrato para todos os repositórios de Intent.

Especializa o BaseRepository para trabalhar com a entidade
Intent.

Autor: Raphael Wilson
"""

from __future__ import annotations

from abc import abstractmethod

from app.domain.entities.intent.intent import Intent
from app.domain.entities.intent.intent_type import IntentType
from app.repository.base_repository import BaseRepository


class BaseIntentRepository(BaseRepository[Intent]):
    """
    Contrato base para os repositórios de Intent.
    """

    @abstractmethod
    def find_by_type(
        self,
        intent_type: IntentType,
    ) -> list[Intent]:
        """
        Retorna todas as intenções de um determinado tipo.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_confidence(
        self,
        minimum: float,
    ) -> list[Intent]:
        """
        Retorna intenções com confiança mínima.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_text(
        self,
        text: str,
    ) -> list[Intent]:
        """
        Pesquisa intenções pelo texto.
        """
        raise NotImplementedError