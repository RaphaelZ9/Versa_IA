from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseProvider(ABC):
    """
    Interface base para qualquer provedor de LLM.

    Todos os providers (Ollama, OpenAI, Gemini, Anthropic, etc.)
    devem implementar esta interface.
    """

    @abstractmethod
    def initialize(self) -> None:
        """Inicializa o provider."""
        pass

    @abstractmethod
    def chat(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Envia uma conversa ao modelo.
        """
        pass

    @abstractmethod
    def generate(
        self,
        prompt: str,
        **kwargs
    ) -> str:
        """
        Geração simples de texto.
        """
        pass

    @abstractmethod
    def embeddings(
        self,
        text: str
    ) -> List[float]:
        """
        Gera embeddings.
        """
        pass

    @abstractmethod
    def stream(
        self,
        prompt: str,
        **kwargs
    ):
        """
        Geração em streaming.
        """
        pass

    @abstractmethod
    def list_models(self) -> List[str]:
        """Lista os modelos disponíveis."""
        pass

    @abstractmethod
    def get_current_model(self) -> str:
        """Retorna o modelo atualmente utilizado."""
        pass

    @abstractmethod
    def health_check(self) -> bool:
        """Verifica se o provider está operacional."""
        pass

    @abstractmethod
    def get_provider_name(self) -> str:
        """Retorna o nome do provider."""
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Finaliza o provider."""
        pass