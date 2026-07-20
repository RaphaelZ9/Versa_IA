"""
===============================================================================
Versa AI
Arquivo: logger.py

Infraestrutura de Logging da Versa AI.

Responsabilidades
-----------------
- Criar loggers padronizados.
- Gravar logs em arquivo.
- Exibir logs no console.
- Evitar handlers duplicados.
- Centralizar a configuração de logging.

Todos os módulos da Versa AI utilizam esta infraestrutura através do
LogManager.
===============================================================================
"""

import logging
import os
from pathlib import Path


# =============================================================================
# CONFIGURAÇÕES
# =============================================================================

LOG_DIRECTORY = Path("logs")

LOG_LEVEL = logging.DEBUG

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)-20s | "
    "%(message)s"
)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


# =============================================================================
# PREPARAÇÃO
# =============================================================================

LOG_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True
)


# =============================================================================
# LOGGER FACTORY
# =============================================================================

def get_logger(name: str) -> logging.Logger:
    """
    Retorna um logger configurado.

    Caso o logger já exista, ele é reutilizado.

    Parameters
    ----------
    name : str
        Nome do logger.

    Returns
    -------
    logging.Logger
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=DATE_FORMAT
    )

    # -------------------------------------------------------------------------
    # Arquivo
    # -------------------------------------------------------------------------

    file_handler = logging.FileHandler(
        LOG_DIRECTORY / f"{name}.log",
        encoding="utf-8"
    )

    file_handler.setLevel(LOG_LEVEL)

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # -------------------------------------------------------------------------
    # Console
    # -------------------------------------------------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    # -------------------------------------------------------------------------

    logger.propagate = False

    return logger


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    logger = get_logger("versa")

    logger.debug("Debug")

    logger.info("Info")

    logger.warning("Warning")

    logger.error("Error")

    logger.critical("Critical")