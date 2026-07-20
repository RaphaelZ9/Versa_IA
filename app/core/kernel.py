"""
===============================================================================
Versa AI
Arquivo: kernel.py

Kernel principal da plataforma Versa AI.

Responsabilidades
-----------------
- Inicializar os módulos centrais da plataforma.
- Gerenciar o ciclo de vida da aplicação.
- Coordenar o Conversation Manager.
- Delegar o contexto pronto ao AI Core.

===============================================================================
"""

from __future__ import annotations

from typing import Optional

from app.ai_core.ai_core import AICore
from app.conversation.conversation_manager import ConversationManager
from app.core.logging.log_manager import LogManager
from app.runtime.ai_response import AIResponse


class VersaKernel:
    """
    Núcleo principal da plataforma Versa AI.
    """

    def __init__(self) -> None:
        self.logger = LogManager.kernel()

        self._initialized = False

        self.ai_core: Optional[AICore] = None

        self.conversation_manager: Optional[
            ConversationManager
        ] = None

    # =========================================================================
    # Inicialização
    # =========================================================================

    def initialize(self) -> None:
        if self._initialized:
            return

        self.logger.info(
            "Inicializando Versa Kernel..."
        )

        self.ai_core = AICore()

        self.ai_core.initialize()

        self.logger.info(
            "AI Core iniciado."
        )

        self.conversation_manager = ConversationManager()

        self.logger.info(
            "Conversation Manager iniciado."
        )

        self._initialized = True

        self.logger.info(
            "Versa Kernel inicializado."
        )

    # =========================================================================
    # Chat
    # =========================================================================

    def chat(
        self,
        message: str,
        system_prompt: str | None = None,
    ) -> AIResponse:
        """
        Processa uma mensagem do usuário.
        """

        if not self._initialized:
            self.initialize()

        assert self.ai_core is not None
        assert self.conversation_manager is not None

        context = self.conversation_manager.build_context(
            system_prompt=system_prompt,
        )

        return self.ai_core.chat(
            message=message,
            context=context,
        )

    # =========================================================================
    # Getters
    # =========================================================================

    def get_ai_core(self) -> AICore:
        if self.ai_core is None:
            raise RuntimeError(
                "AI Core não inicializado."
            )

        return self.ai_core

    def get_conversation_manager(self) -> ConversationManager:
        if self.conversation_manager is None:
            raise RuntimeError(
                "ConversationManager não inicializado."
            )

        return self.conversation_manager

    # =========================================================================
    # Status
    # =========================================================================

    @property
    def initialized(self) -> bool:
        return self._initialized

    # =========================================================================
    # Shutdown
    # =========================================================================

    def shutdown(self) -> None:
        if not self._initialized:
            return

        self.logger.info(
            "Finalizando Versa Kernel..."
        )

        if self.ai_core is not None:
            self.ai_core.shutdown()

        self._initialized = False

        self.logger.info(
            "Versa Kernel finalizado."
        )