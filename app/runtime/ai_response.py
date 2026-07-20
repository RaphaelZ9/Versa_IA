"""
===============================================================================
Versa AI
Arquivo: ai_response.py

Objeto padrão de resposta da Versa AI.

Toda resposta produzida por qualquer modelo de IA deve ser representada por esta
classe.

Responsabilidades
-----------------
- Armazenar o texto gerado.
- Armazenar metadados.
- Armazenar informações do modelo.
- Armazenar chamadas de ferramentas.
- Armazenar referências (RAG).
- Armazenar métricas de execução.

Este objeto é utilizado por toda a plataforma.
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class AIResponse:
    """
    Representa a resposta produzida pela IA.
    """

    # =========================================================================
    # Conteúdo principal
    # =========================================================================

    content: str = ""

    success: bool = True

    # =========================================================================
    # Informações do modelo
    # =========================================================================

    provider: str = ""

    model: str = ""

    finish_reason: str = ""

    # =========================================================================
    # Métricas
    # =========================================================================

    tokens: int = 0

    execution_time: float = 0.0

    # =========================================================================
    # Conversa
    # =========================================================================

    conversation_id: str = ""

    # =========================================================================
    # Ferramentas
    # =========================================================================

    tool_calls: list[dict[str, Any]] = field(default_factory=list)

    # =========================================================================
    # Conhecimento / RAG
    # =========================================================================

    citations: list[Any] = field(default_factory=list)

    # =========================================================================
    # Metadados
    # =========================================================================

    metadata: dict[str, Any] = field(default_factory=dict)

    # =========================================================================
    # Erros
    # =========================================================================

    error_message: str = ""

    # =========================================================================
    # Data/Hora
    # =========================================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    # =========================================================================
    # Properties
    # =========================================================================

    @property
    def has_metadata(self) -> bool:
        """
        Indica se existem metadados.
        """
        return bool(self.metadata)

    @property
    def has_tool_calls(self) -> bool:
        """
        Indica se houve chamadas de ferramentas.
        """
        return bool(self.tool_calls)

    @property
    def has_citations(self) -> bool:
        """
        Indica se existem referências de conhecimento.
        """
        return bool(self.citations)

    @property
    def is_success(self) -> bool:
        """
        Indica se a operação foi concluída com sucesso.
        """
        return self.success

    # =========================================================================
    # Metadata
    # =========================================================================

    def add_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Adiciona um metadado.
        """
        self.metadata[key] = value

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Recupera um metadado.
        """
        return self.metadata.get(key, default)

    # =========================================================================
    # Tool Calls
    # =========================================================================

    def add_tool_call(
        self,
        tool_name: str,
        arguments: dict[str, Any],
        result: Any = None,
    ) -> None:
        """
        Registra uma execução de ferramenta.
        """
        self.tool_calls.append(
            {
                "tool": tool_name,
                "arguments": arguments,
                "result": result,
            }
        )

    # =========================================================================
    # Citations
    # =========================================================================

    def add_citation(
        self,
        citation: Any,
    ) -> None:
        """
        Adiciona uma referência utilizada na resposta.
        """
        self.citations.append(citation)

    # =========================================================================
    # Error
    # =========================================================================

    def set_error(
        self,
        message: str,
    ) -> None:
        """
        Marca a resposta como erro.
        """
        self.success = False
        self.error_message = message

    # =========================================================================
    # Serialização
    # =========================================================================

    def to_dict(self) -> dict[str, Any]:
        """
        Converte o objeto para dicionário.
        """
        return {
            "content": self.content,
            "success": self.success,
            "provider": self.provider,
            "model": self.model,
            "finish_reason": self.finish_reason,
            "tokens": self.tokens,
            "execution_time": self.execution_time,
            "conversation_id": self.conversation_id,
            "tool_calls": self.tool_calls,
            "citations": self.citations,
            "metadata": self.metadata,
            "error_message": self.error_message,
            "created_at": self.created_at.isoformat(),
        }

    # =========================================================================
    # String
    # =========================================================================

    def __str__(self) -> str:
        return self.content