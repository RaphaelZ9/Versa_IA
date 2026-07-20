"""
===============================================================================
Versa IA
Context Package

Objeto responsável por transportar todos os contextos utilizados
durante a construção do prompt.

Este componente NÃO possui regras de negócio.

Sua única responsabilidade é armazenar os diferentes contextos
coletados pelo ContextBuilder.

Autor:
Raphael Wilson

Projeto:
Versa IA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class ContextPackage:
    """
    Representa todos os contextos disponíveis para uma requisição.

    Cada atributo representa uma camada independente da arquitetura.

    Novos contextos poderão ser adicionados futuramente sem alterar
    a interface pública do PromptBuilder.
    """

    system_prompt: Optional[str] = None

    company_context: Optional[str] = None

    memory: Optional[str] = None

    knowledge: Optional[str] = None

    conversation: Optional[str] = None

    ###########################################################################
    # Helpers
    ###########################################################################

    def sections(self) -> list[str]:
        """
        Retorna todas as seções válidas do contexto,
        preservando a ordem de construção do prompt.
        """

        sections: list[str] = []

        for value in (
            self.system_prompt,
            self.company_context,
            self.memory,
            self.knowledge,
            self.conversation,
        ):
            if value:
                sections.append(value)

        return sections

    def is_empty(self) -> bool:
        """
        Indica se o pacote não possui nenhum contexto.
        """

        return len(self.sections()) == 0

    def has_memory(self) -> bool:

        return bool(self.memory)

    def has_knowledge(self) -> bool:

        return bool(self.knowledge)

    def has_conversation(self) -> bool:

        return bool(self.conversation)

    def has_company_context(self) -> bool:

        return bool(self.company_context)

    def has_system_prompt(self) -> bool:

        return bool(self.system_prompt)