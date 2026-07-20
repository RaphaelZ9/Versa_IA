"""
Versa AI

Arquivo:
base_agent.py

Responsabilidade:
Definir a interface base para todos os agentes da IA.

Todos os agentes do sistema devem herdar desta classe,
garantindo uma API consistente para inicialização,
execução e encerramento.

Autor: Raphael Wilson
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):


    def __init__(
        self,
        agent_id: str,
        name: str,
        description: str,
        specialty: str,
        priority: int = 100,
    ) -> None:

        self.id = agent_id
        self.name = name
        self.description = description
        self.specialty = specialty
        self.priority = priority

        self.capabilities: list[str] = []

        self.enabled: bool = True

        self.initialized: bool = False

    @abstractmethod
    def initialize(self) -> None:
 
        pass

    @abstractmethod
    def can_handle(self, intent: Any) -> bool:

        pass

    @abstractmethod
    def execute(self, context: Any) -> Any:

        pass

    @abstractmethod
    def shutdown(self) -> None:

        pass