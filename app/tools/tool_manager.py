"""
Versa AI

Arquivo:
tool_manager.py

Responsabilidade:
Gerenciar todas as ferramentas (Tools) registradas na Versa AI.

O ToolManager atua como um orquestrador das ferramentas,
permitindo registrar, localizar e recuperar Tools de maneira
padronizada.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.managers.base_manager import BaseManager
from app.tools.base_tool import BaseTool


class ToolManager(BaseManager):
    """
    Gerenciador responsável pelas Tools da Versa AI.
    """

    def __init__(self) -> None:
        """
        Inicializa o ToolManager.
        """

        super().__init__()

    def register_tool(self, tool: BaseTool) -> None:
        """
        Registra uma nova Tool.
        """

        self.register(tool)

    def unregister_tool(self, tool: BaseTool) -> None:
        """
        Remove uma Tool.
        """

        self.unregister(tool)

    def get_tool(self, tool_id: str) -> BaseTool | None:
        """
        Retorna uma Tool pelo seu identificador.
        """

        component = self.get(
            lambda tool: getattr(tool, "id", None) == tool_id
        )

        return component

    def get_tools(self) -> list[BaseTool]:
        """
        Retorna todas as Tools registradas.
        """

        return self.get_all()