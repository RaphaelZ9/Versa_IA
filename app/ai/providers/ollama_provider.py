"""
===============================================================================
Versa AI
Arquivo: ollama_provider.py

Implementação do Provider para o Ollama.

Responsabilidades
-----------------
- Comunicar com o servidor Ollama.
- Enviar prompts.
- Receber respostas.
- Realizar Health Check.
- Listar modelos disponíveis.
- Gerenciar o modelo ativo.

Este Provider NÃO conhece:

- Conversation
- Memory
- Intent
- Knowledge
- PromptBuilder
- Agentes

Toda preparação do prompt pertence ao AI Core.
===============================================================================
"""

from typing import Any, Dict, Generator, List, Optional

from ollama import Client

from app.ai.providers.base_provider import BaseProvider
from app.core.config import Config
from app.core.logging.log_manager import LogManager
from time import perf_counter


class OllamaProvider(BaseProvider):

    def __init__(self) -> None:

        self.logger = LogManager.get_logger("OllamaProvider")

        self.client: Optional[Client] = None

        self.host = Config.OLLAMA_HOST

        self.model = Config.OLLAMA_MODEL

    # ---------------------------------------------------------------------

    def initialize(self) -> None:

        self.logger.info("Inicializando Ollama Provider...")

        self.client = Client(host=self.host)

        self.logger.info(
            "Ollama Provider inicializado (%s)",
            self.host
        )

    # ---------------------------------------------------------------------

    def chat(
        self,
        messages: List[Dict[str, str]],
        **kwargs
    ) -> str:

        if self.client is None:
            raise RuntimeError(
                "Ollama Provider não foi inicializado."
            )

        self.logger.info(
            "Enviando %s mensagem(ns) ao Ollama...",
            len(messages)
        )

        inicio = perf_counter()

        response = self.client.chat(
            model=self.model,
            messages=messages,
            **kwargs
        )

        tempo = perf_counter() - inicio

        prompt_tokens = response.get("prompt_eval_count", 0)
        response_tokens = response.get("eval_count", 0)

        prompt_duration = response.get("prompt_eval_duration", 0)
        eval_duration = response.get("eval_duration", 0)

        self.logger.info(
            "Resposta recebida em %.2f segundos.",
            tempo
        )

        self.logger.info(
            "Prompt Tokens   : %s",
            prompt_tokens
        )

        self.logger.info(
            "Response Tokens : %s",
            response_tokens
        )

        if eval_duration:

            tokens_por_segundo = (
                response_tokens /
                (eval_duration / 1_000_000_000)
            )

            self.logger.info(
                "Velocidade      : %.2f tokens/s",
                tokens_por_segundo
            )

        return response["message"]["content"]

    # ---------------------------------------------------------------------

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> str:

        messages = []

        if system_prompt:

            messages.append(
                {
                    "role": "system",
                    "content": system_prompt
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        return self.chat(
            messages=messages,
            **kwargs
        )

    # ---------------------------------------------------------------------

    def embeddings(
        self,
        text: str
    ) -> List[float]:

        raise NotImplementedError(
            "Embeddings ainda não implementados."
        )

    # ---------------------------------------------------------------------

    def stream(
        self,
        messages: List[Dict[str, str]],
        **kwargs
    ) -> Generator[str, None, None]:

        if self.client is None:
            raise RuntimeError(
                "Ollama Provider não foi inicializado."
            )

        stream = self.client.chat(
            model=self.model,
            messages=messages,
            stream=True,
            **kwargs
        )

        for chunk in stream:

            content = chunk["message"]["content"]

            if content:

                yield content

    # ---------------------------------------------------------------------

    def list_models(self) -> List[str]:

        if self.client is None:
            raise RuntimeError(
                "Ollama Provider não foi inicializado."
            )

        response = self.client.list()

        models = []

        for model in response.get("models", []):

            models.append(model["name"])

        return models

    # ---------------------------------------------------------------------

    def get_current_model(self) -> str:

        return self.model

    # ---------------------------------------------------------------------

    def set_model(
        self,
        model: str
    ) -> None:

        self.model = model

    # ---------------------------------------------------------------------

    def health_check(self) -> bool:

        try:

            self.list_models()

            return True

        except Exception as exc:

            self.logger.exception(exc)

            return False

    # ---------------------------------------------------------------------

    def get_provider_name(self) -> str:

        return "ollama"

    # ---------------------------------------------------------------------

    def shutdown(self) -> None:

        self.logger.info(
            "Finalizando Ollama Provider..."
        )

        self.client = None

        self.logger.info(
            "Ollama Provider finalizado."
        )