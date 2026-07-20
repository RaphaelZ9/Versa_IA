"""
===============================================================================
Versa AI
Arquivo: model_manager.py

Gerenciador central dos modelos de IA.

Responsabilidades
-----------------
- Inicializar o provider ativo.
- Encerrar o provider.
- Encaminhar prompts ao provider.
- Listar modelos disponíveis.
- Alterar o modelo em tempo de execução.
- Verificar a saúde do provider.

O restante da aplicação nunca conversa diretamente com um Provider.
Toda comunicação deve passar pelo ModelManager.
===============================================================================
"""

from __future__ import annotations

from typing import Dict, List, Optional

from app.ai.providers.base_provider import BaseProvider
from app.ai.providers.ollama_provider import OllamaProvider
from app.core.logging.log_manager import LogManager


class ModelManager:
    """
    Gerencia o provider e o modelo de IA utilizados pela plataforma.
    """

    def __init__(
        self,
        provider: Optional[BaseProvider] = None,
    ) -> None:

        self.logger = LogManager.get_logger("ModelManager")

        self.provider: BaseProvider = (
            provider if provider is not None
            else OllamaProvider()
        )

        self._initialized = False

    # ======================================================================
    # Ciclo de vida
    # ======================================================================

    def initialize(self) -> None:

        if self._initialized:
            return

        self.logger.info("Inicializando Model Manager...")

        self.provider.initialize()

        self._initialized = True

        self.logger.info(
            "Provider ativo: %s",
            self.provider.get_provider_name()
        )

        self.logger.info(
            "Modelo ativo: %s",
            self.provider.get_current_model()
        )

    def shutdown(self) -> None:

        if not self._initialized:
            return

        self.logger.info("Finalizando Model Manager...")

        self.provider.shutdown()

        self._initialized = False

        self.logger.info("Model Manager finalizado.")

    # ======================================================================
    # Chat
    # ======================================================================

    def chat(
        self,
        messages: List[Dict[str, str]],
        **kwargs,
    ) -> str:

        if not self._initialized:
            self.initialize()

        return self.provider.chat(
            messages=messages,
            **kwargs,
        )

    # ======================================================================
    # Geração simples
    # ======================================================================

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        **kwargs,
    ) -> str:

        if not self._initialized:
            self.initialize()

        return self.provider.generate(
            prompt=prompt,
            system_prompt=system_prompt,
            **kwargs,
        )

    # ======================================================================
    # Streaming
    # ======================================================================

    def stream(
        self,
        messages: List[Dict[str, str]],
        **kwargs,
    ):

        if not self._initialized:
            self.initialize()

        return self.provider.stream(
            messages=messages,
            **kwargs,
        )

    # ======================================================================
    # Embeddings
    # ======================================================================

    def embeddings(
        self,
        text: str,
    ):

        if not self._initialized:
            self.initialize()

        return self.provider.embeddings(text)

    # ======================================================================
    # Provider
    # ======================================================================

    def get_provider(self) -> BaseProvider:
        """
        Retorna o provider ativo.
        """
        return self.provider

    def set_provider(
        self,
        provider: BaseProvider,
    ) -> None:
        """
        Altera o provider ativo.
        """

        if self._initialized:
            self.provider.shutdown()

        self.provider = provider

        self._initialized = False

        self.initialize()

    # ======================================================================
    # Modelos
    # ======================================================================

    def list_models(self) -> List[str]:

        if not self._initialized:
            self.initialize()

        return self.provider.list_models()

    def get_current_model(self) -> str:

        return self.provider.get_current_model()

    def set_model(
        self,
        model: str,
    ) -> None:

        if hasattr(self.provider, "set_model"):
            self.provider.set_model(model)

            self.logger.info(
                "Modelo alterado para '%s'.",
                model,
            )

    # ======================================================================
    # Health
    # ======================================================================

    def health_check(self) -> bool:

        if not self._initialized:
            self.initialize()

        return self.provider.health_check()