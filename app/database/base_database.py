"""
Versa AI

Arquivo:
base_database.py

Responsabilidade:
Definir a interface base para todos os bancos de dados utilizados
pela Versa AI.

Todos os bancos devem herdar desta classe, garantindo uma API
consistente para conexão, execução de comandos e encerramento.

Autor: Raphael Wilson
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseDatabase(ABC):


    def __init__(
        self,
        database_id: str,
        name: str,
        description: str,
        priority: int = 100,
    ) -> None:

        self.id = database_id
        self.name = name
        self.description = description
        self.priority = priority

        self.enabled: bool = True

        self.connected: bool = False

    @abstractmethod
    def connect(self) -> None:

        pass

    @abstractmethod
    def disconnect(self) -> None:

        pass

    @abstractmethod
    def is_connected(self) -> bool:

        pass

    @abstractmethod
    def execute(
        self,
        query: str,
        parameters: dict[str, Any] | None = None,
    ) -> Any:

        pass

    @abstractmethod
    def shutdown(self) -> None:

        pass