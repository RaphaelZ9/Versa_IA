"""
===============================================================================
Versa AI

BaseRepository

Classe base para todos os repositórios da plataforma.

Responsabilidades:

- CRUD básico
- Interface comum
- Logging
- Inicialização

Esta classe NÃO conhece:

- Supabase
- Oracle
- SQL Server
- PostgreSQL
- MongoDB

Cada implementação concreta será responsável pela persistência.

===============================================================================
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar

from app.core.logging.log_manager import LogManager

T = TypeVar("T")

class BaseRepository(Generic[T], ABC):
    """
    Classe base para todos os repositórios.
    """

    def __init__(self) -> None:

        self.logger = LogManager.get_logger(
            self.__class__.__name__
        )

    ###########################################################################
    # CRUD
    ###########################################################################

    def save(self, entity: T) -> T:
        """
        Salva uma entidade.

        Deve ser sobrescrito pelas implementações concretas.
        """
        raise NotImplementedError()

    def update(self, entity: T) -> T:
        """
        Atualiza uma entidade.
        """
        raise NotImplementedError()

    def delete(self, entity_id: Any) -> None:
        """
        Remove uma entidade.
        """
        raise NotImplementedError()

    def find_by_id(self, entity_id: Any) -> T | None:
        """
        Localiza uma entidade pelo ID.
        """
        raise NotImplementedError()

    def find_all(self) -> list[T]:
        """
        Retorna todas as entidades.
        """
        raise NotImplementedError()

    ###########################################################################
    # UTIL
    ###########################################################################

    def initialize(self) -> None:
        """
        Inicialização do repositório.
        """

        self.logger.info(
            "%s inicializado.",
            self.__class__.__name__
        )

    def shutdown(self) -> None:
        """
        Finalização do repositório.
        """

        self.logger.info(
            "%s finalizado.",
            self.__class__.__name__
        )

    ###########################################################################
    # REPRESENTAÇÃO
    ###########################################################################

    def __repr__(self) -> str:

        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:

        return self.__class__.__name__