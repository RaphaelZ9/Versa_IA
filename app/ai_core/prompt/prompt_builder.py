"""
===============================================================================
Versa AI

Prompt Builder

Responsável exclusivamente por transformar um ContextPackage pronto
em mensagens compatíveis com o provider de LLM.

Este módulo NÃO constrói contexto, não consulta Providers e não conhece
implementações internas como SystemPrompt ou CompanyContext.

===============================================================================
"""

from __future__ import annotations

from app.ai_core.context.context_package import ContextPackage
from app.core.logging.log_manager import LogManager


class PromptBuilder:
    """
    Responsável por montar as mensagens enviadas ao modelo.

    O contexto deve ser construído previamente pelo ContextBuilder e entregue
    por meio de um ContextPackage.
    """

    def __init__(self) -> None:
        self.logger = LogManager.get_logger(
            "PromptBuilder"
        )

    # =========================================================================
    # Public API
    # =========================================================================

    def build(
        self,
        *,
        user_message: str,
        context: ContextPackage,
    ) -> list[dict[str, str]]:
        """
        Constrói as mensagens enviadas ao modelo.

        Ordem:

            1) Seções disponíveis no ContextPackage
            2) Mensagem do usuário
        """

        self.logger.info(
            "Construindo prompt..."
        )

        messages: list[dict[str, str]] = []

        self._append_context(
            messages,
            context,
        )

        self._append_message(
            messages,
            self._build_user(
                user_message
            ),
        )

        self.logger.info(
            "Prompt construído (%s mensagens).",
            len(messages),
        )

        return messages

    # =========================================================================
    # Context
    # =========================================================================

    def _append_context(
        self,
        messages: list[dict[str, str]],
        context: ContextPackage,
    ) -> None:
        """
        Adiciona ao prompt as seções já preparadas no ContextPackage.
        """

        for section in context.sections():
            self._append_message(
                messages,
                self._message(
                    role="system",
                    content=section,
                ),
            )

    # =========================================================================
    # User
    # =========================================================================

    def _build_user(
        self,
        message: str,
    ) -> dict[str, str]:
        """
        Cria a mensagem enviada pelo usuário.
        """

        return self._message(
            role="user",
            content=message,
        )

    # =========================================================================
    # Message helpers
    # =========================================================================

    def _append_message(
        self,
        messages: list[dict[str, str]],
        message: dict[str, str],
    ) -> None:
        """
        Adiciona uma mensagem válida ao prompt.
        """

        role = self._clean(
            message.get("role")
        )

        content = self._clean(
            message.get("content")
        )

        if not role or not content:
            return

        messages.append(
            self._message(
                role=role,
                content=content,
            )
        )

    def _message(
        self,
        *,
        role: str,
        content: str,
    ) -> dict[str, str]:
        """
        Cria uma mensagem no formato esperado pelos providers.
        """

        return {
            "role": role,
            "content": content,
        }

    def _clean(
        self,
        text: str | None,
    ) -> str:
        """
        Remove espaços extras de um texto.
        """

        if text is None:
            return ""

        return str(text).strip()

    # =========================================================================
    # Preview and exports
    # =========================================================================

    def preview(
        self,
        *,
        user_message: str,
        context: ContextPackage,
    ) -> str:
        """
        Retorna uma visualização legível do prompt.
        """

        messages = self.build(
            user_message=user_message,
            context=context,
        )

        lines: list[str] = [
            "=" * 80,
            "VERSA AI - PROMPT PREVIEW",
            "=" * 80,
        ]

        for index, message in enumerate(
            messages,
            start=1,
        ):
            role = message.get(
                "role",
                "unknown",
            ).upper()

            lines.extend(
                [
                    "",
                    f"[{index}] {role}",
                    "-" * 80,
                    message.get(
                        "content",
                        "",
                    ),
                ]
            )

        lines.extend(
            [
                "",
                "=" * 80,
            ]
        )

        return "\n".join(lines)

    def to_markdown(
        self,
        *,
        user_message: str,
        context: ContextPackage,
    ) -> str:
        """
        Exporta o prompt em Markdown.
        """

        messages = self.build(
            user_message=user_message,
            context=context,
        )

        markdown: list[str] = [
            "# Versa AI Prompt",
            "",
        ]

        for message in messages:
            role = message.get(
                "role",
                "unknown",
            ).upper()

            markdown.extend(
                [
                    f"## {role}",
                    "",
                    message.get(
                        "content",
                        "",
                    ),
                    "",
                ]
            )

        return "\n".join(markdown)

    def to_text(
        self,
        *,
        user_message: str,
        context: ContextPackage,
    ) -> str:
        """
        Exporta todas as mensagens para texto simples.
        """

        messages = self.build(
            user_message=user_message,
            context=context,
        )

        text: list[str] = []

        for message in messages:
            role = message.get(
                "role",
                "",
            ).upper()

            content = message.get(
                "content",
                "",
            )

            text.extend(
                [
                    f"[{role}]",
                    content,
                    "",
                ]
            )

        return "\n".join(text)

    # =========================================================================
    # Statistics
    # =========================================================================

    def token_estimate(
        self,
        *,
        user_message: str,
        context: ContextPackage,
    ) -> int:
        """
        Retorna uma estimativa simples da quantidade de tokens.
        """

        text = self.to_text(
            user_message=user_message,
            context=context,
        )

        return max(
            1,
            len(text) // 4,
        )

    def statistics(
        self,
        *,
        user_message: str,
        context: ContextPackage,
    ) -> dict[str, int | bool]:
        """
        Retorna estatísticas do prompt montado.
        """

        messages = self.build(
            user_message=user_message,
            context=context,
        )

        total_characters = sum(
            len(
                message.get(
                    "content",
                    "",
                )
            )
            for message in messages
        )

        return {
            "messages": len(messages),
            "characters": total_characters,
            "estimated_tokens": max(
                1,
                total_characters // 4,
            ),
            "has_memory": context.has_memory(),
            "has_knowledge": context.has_knowledge(),
            "has_conversation": context.has_conversation(),
            "has_company_context": context.has_company_context(),
            "has_system_prompt": context.has_system_prompt(),
        }

    # =========================================================================
    # Metadata
    # =========================================================================

    @property
    def version(self) -> str:
        """
        Retorna a versão do PromptBuilder.
        """

        return "2.0"

    def reset(self) -> None:
        """
        Mantém compatibilidade com futuras implementações stateful.
        """

        self.logger.debug(
            "PromptBuilder resetado."
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(version='{self.version}')"
        )

    def __str__(self) -> str:
        return (
            f"PromptBuilder "
            f"v{self.version}"
        )