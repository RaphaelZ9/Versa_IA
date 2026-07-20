"""
Versa AI

Arquivo:
base_tool.py

Responsabilidade:
Definir a interface base para todas as ferramentas da Versa AI.

Todas as ferramentas devem herdar desta classe, garantindo uma API
consistente para inicialização, execução e encerramento.

Autor: Raphael Wilson
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):


    def __init__(
        self,
        tool_id: str,
        name: str,
        description: str,
        category: str,
        priority: int = 100,
    ) -> None:

        self.id = tool_id
        self.name = name
        self.description = description
        self.category = category
        self.priority = priority

        self.enabled: bool = True

        self.initialized: bool = False

    @abstractmethod
    def initialize(self) -> None:

        pass

    @abstractmethod
    def can_execute(self, context: Any) -> bool:

        pass

    @abstractmethod
    def execute(self, **kwargs: Any) -> Any:

        pass

    @abstractmethod
    def shutdown(self) -> None:

        pass