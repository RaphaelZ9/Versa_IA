"""
===============================================================================
Versa AI

Memory Service

Responsável por preparar o contexto de memória utilizado na geração
das respostas.

Nesta primeira versão, o serviço apenas normaliza a memória recebida.

Toda evolução futura (resumos, limite de tokens, memória de longo prazo,
embeddings etc.) deverá acontecer nesta classe.

===============================================================================
"""

from __future__ import annotations


class MemoryService:
    """
    Serviço responsável por preparar a memória da conversa.
    """

    def build(
        self,
        memory: str | None = None,
    ) -> str:
        """
        Prepara a memória utilizada na requisição atual.

        Parameters
        ----------
        memory:
            Memória previamente preparada.

        Returns
        -------
        str
            Texto da memória que será utilizado pelo MemoryProvider.
        """

        return memory or ""