"""
===============================================================================
Versa AI
Arquivo: ai_core.py

Núcleo da Inteligência Artificial da plataforma.

Responsabilidades
-----------------
- Receber solicitações do Kernel.
- Solicitar a construção do contexto.
- Transformar o contexto em mensagens para o modelo.
- Delegar chamadas ao ModelManager.
- Retornar um AIResponse.

===============================================================================
"""

from __future__ import annotations

from typing import Optional

from app.ai.model_manager import ModelManager
from app.ai_core.context.context_builder import ContextBuilder
from app.ai_core.context.context_package import ContextPackage
from app.ai_core.prompt.prompt_builder import PromptBuilder
from app.core.logging.log_manager import LogManager
from app.runtime.ai_response import AIResponse


class AICore:
    """
    Núcleo da Inteligência Artificial da Versa AI.
    """

    def __init__(
        self,
        model_manager: Optional[ModelManager] = None,
    ) -> None:
        self.logger = LogManager.get_logger(
            "AICore"
        )

        self.model_manager = (
            model_manager
            if model_manager is not None
            else ModelManager()
        )

        self.context_builder = ContextBuilder()

        self.prompt_builder = PromptBuilder()

        self._initialized = False

    # =========================================================================
    # Inicialização
    # =========================================================================

    def initialize(self) -> None:
        if self._initialized:
            return

        self.logger.info(
            "Inicializando AI Core..."
        )

        self.model_manager.initialize()

        self._initialized = True

        self.logger.info(
            "AI Core inicializado."
        )

    # =========================================================================
    # Chat
    # =========================================================================

    def chat(
        self,
        message: str,
        system_prompt: Optional[str] = None,
    ) -> AIResponse:
        """
        Processa uma mensagem enviada pelo usuário.
        """

        if not self._initialized:
            self.initialize()

        context = self._build_context(
            system_prompt=system_prompt,
        )

        messages = self.prompt_builder.build(
            user_message=message,
            context=context,
        )

        self.logger.info(
            "Enviando mensagem ao ModelManager..."
        )

        try:
            content = self.model_manager.chat(
                messages
            )

            response = AIResponse(
                success=True,
                content=content,
                provider=(
                    self.model_manager
                    .get_provider()
                    .get_provider_name()
                ),
                model=self.model_manager.get_current_model(),
            )

            self.logger.info(
                "Resposta recebida com sucesso."
            )

            return response

        except Exception as exc:
            self.logger.exception(exc)

            response = AIResponse()

            response.set_error(
                str(exc)
            )

            return response

    # =========================================================================
    # Context
    # =========================================================================

    def _build_context(
        self,
        *,
        system_prompt: Optional[str],
    ) -> ContextPackage:
        """
        Constrói o contexto utilizado para a requisição atual.

        O parâmetro system_prompt é mantido como sobrescrita opcional
        por compatibilidade com a API pública atual.
        """

        context = self.context_builder.build()

        if system_prompt is not None:
            context.system_prompt = system_prompt

        return context

    # =========================================================================
    # Generate
    # =========================================================================

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> AIResponse:
        if not self._initialized:
            self.initialize()

        try:
            content = self.model_manager.generate(
                prompt=prompt,
                system_prompt=system_prompt,
            )

            return AIResponse(
                success=True,
                content=content,
                provider=(
                    self.model_manager
                    .get_provider()
                    .get_provider_name()
                ),
                model=self.model_manager.get_current_model(),
            )

        except Exception as exc:
            self.logger.exception(exc)

            response = AIResponse()

            response.set_error(
                str(exc)
            )

            return response

    # =========================================================================
    # Status
    # =========================================================================

    @property
    def initialized(self) -> bool:
        """
        Indica se o AI Core já foi inicializado.
        """

        return self._initialized

    # =========================================================================
    # Shutdown
    # =========================================================================

    def shutdown(self) -> None:
        if not self._initialized:
            return

        self.logger.info(
            "Finalizando AI Core..."
        )

        self.model_manager.shutdown()

        self._initialized = False

        self.logger.info(
            "AI Core finalizado."
        )