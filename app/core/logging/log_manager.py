"""
===============================================================================
Versa AI
Arquivo: log_manager.py

Gerenciador central de loggers da aplicação.

Responsabilidades
-----------------
- Fornecer uma única instância de logger para cada módulo.
- Evitar criação duplicada de loggers.
- Centralizar o acesso ao sistema de logging.
===============================================================================
"""

from __future__ import annotations

from typing import Dict
import logging

from app.core.logging.logger import get_logger


class LogManager:
    """
    Cache central de loggers.

    Exemplo
    --------

    logger = LogManager.get_logger("KnowledgeManager")
    logger.info("Inicializado")
    """

    _cache: Dict[str, logging.Logger] = {}

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """
        Retorna um logger para o módulo informado.

        Caso ainda não exista, ele será criado automaticamente.

        Parameters
        ----------
        name : str
            Nome do módulo.

        Returns
        -------
        logging.Logger
        """

        if name not in cls._cache:
            cls._cache[name] = get_logger(name)

        return cls._cache[name]

    # =====================================================================
    # Atalhos mais utilizados
    # =====================================================================

    @classmethod
    def app(cls) -> logging.Logger:
        return cls.get_logger("VersaAI")

    @classmethod
    def kernel(cls) -> logging.Logger:
        return cls.get_logger("VersaKernel")

    @classmethod
    def ai(cls) -> logging.Logger:
        return cls.get_logger("AI")

    @classmethod
    def prompt(cls) -> logging.Logger:
        return cls.get_logger("Prompt")

    @classmethod
    def search(cls) -> logging.Logger:
        return cls.get_logger("Search")

    @classmethod
    def memory(cls) -> logging.Logger:
        return cls.get_logger("Memory")

    @classmethod
    def tools(cls) -> logging.Logger:
        return cls.get_logger("Tools")

    @classmethod
    def knowledge(cls) -> logging.Logger:
        return cls.get_logger("Knowledge")

    @classmethod
    def automation(cls) -> logging.Logger:
        return cls.get_logger("Automation")

    @classmethod
    def runtime(cls) -> logging.Logger:
        return cls.get_logger("Runtime")

    @classmethod
    def api(cls) -> logging.Logger:
        return cls.get_logger("API")

    @classmethod
    def error(cls) -> logging.Logger:
        return cls.get_logger("Error")

    # =====================================================================
    # Utilidades
    # =====================================================================

    @classmethod
    def clear_cache(cls) -> None:
        """
        Limpa o cache de loggers.

        Útil em testes automatizados.
        """
        cls._cache.clear()

    @classmethod
    def registered_loggers(cls) -> list[str]:
        """
        Retorna os loggers já criados.
        """
        return sorted(cls._cache.keys())