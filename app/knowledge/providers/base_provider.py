"""
Versa AI

Arquivo:
base_provider.py

Responsabilidade:
Definir a interface base para todos os provedores de conhecimento
utilizados pela Versa AI.

Todos os providers devem herdar desta classe, garantindo uma API
consistente para inicialização, pesquisa e encerramento.

Autor: Raphael Wilson
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from app.core.logger import get_logger


class BaseProvider(ABC):
    """
    Classe base para todos os Providers da Versa AI.
    """

    def __init__(
        self,
        provider_id: str,
        name: str,
        description: str,
        provider_type: str,
        priority: int = 100,
    ) -> None:

        self.id = provider_id
        self.name = name
        self.description = description
        self.provider_type = provider_type
        self.priority = priority

        self.enabled: bool = True
        self.initialized: bool = False

        self._logger = get_logger(self.__class__.__name__)

    def initialize(self) -> None:
        """
        Inicializa o provider.
        """

        self.initialized = True

        self._logger.info(f"{self.name} inicializado.")

    def is_available(self) -> bool:
        """
        Verifica se o provider está disponível.
        """

        return self.initialized

    @abstractmethod
    def search(self, query: str) -> list[Any]:
        """
        Executa uma pesquisa.

        Deve ser implementado por cada Provider.
        """

        raise NotImplementedError

    def shutdown(self) -> None:
        """
        Finaliza o provider.
        """

        self.initialized = False

        self._logger.info(f"{self.name} finalizado.")