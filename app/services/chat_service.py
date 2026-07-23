from __future__ import annotations

import time
from threading import Lock

from app.versa_ai import VersaAI


class ChatService:
    """
    Serviço responsável por manter uma única instância
    da VersaAI durante toda a execução da aplicação.
    """

    def __init__(self) -> None:

        self._lock = Lock()

        self._initialized = False

        self._ia = VersaAI()

    def initialize(self) -> None:

        with self._lock:

            if self._initialized:
                return

            self._ia.initialize()

            self._initialized = True

    def shutdown(self) -> None:

        with self._lock:

            if not self._initialized:
                return

            self._ia.shutdown()

            self._initialized = False

    def chat(self, message: str) -> dict:

        start = time.perf_counter()

        resposta = self._ia.chat(message)

        elapsed = int((time.perf_counter() - start) * 1000)

        # Extrai o texto independentemente do tipo retornado
        if hasattr(resposta, "content"):
            texto = resposta.content

        elif isinstance(resposta, dict):
            texto = resposta.get("content") or resposta.get("response") or str(resposta)

        else:
            texto = str(resposta)

        return {

            "success": True,

            "response": texto,

            "elapsed_ms": elapsed

        }


chat_service = ChatService()