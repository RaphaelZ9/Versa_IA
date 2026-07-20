"""
Versa AI

Arquivo:
intent_type.py

Responsabilidade:
Definir os tipos de intenção reconhecidos pela Versa AI.

Autor: Raphael Wilson
"""

from enum import Enum


class IntentType(str, Enum):
    """
    Tipos de intenção suportados pela Versa AI.
    """

    UNKNOWN = "unknown"

    CHAT = "chat"

    SEARCH = "search"

    QUESTION = "question"

    SUMMARIZE = "summarize"

    EXTRACT = "extract"

    ANALYZE = "analyze"

    CLASSIFY = "classify"

    TRANSLATE = "translate"

    AUTOMATION = "automation"

    EMAIL = "email"

    PDF = "pdf"

    FILE = "file"

    TOOL = "tool"

    WORKFLOW = "workflow"

    MEMORY = "memory"

    KNOWLEDGE = "knowledge"

    REPORT = "report"

    SQL = "sql"

    CODE = "code"

    HELP = "help"