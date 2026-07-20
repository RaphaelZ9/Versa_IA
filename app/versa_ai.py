"""
===============================================================================
Versa AI
Arquivo: versa_ai.py

Interface pública da plataforma Versa AI.

Responsabilidades:
- Inicializar a plataforma.
- Encerrar a plataforma.
- Receber mensagens do usuário.
- Delegar toda a execução ao Kernel.

Este arquivo NÃO deve conter regras de negócio.
Toda a inteligência da aplicação pertence ao VersaKernel.
===============================================================================
"""

from app.core.kernel import VersaKernel
from app.runtime.ai_response import AIResponse


class VersaAI:
    """
    Interface principal da plataforma Versa AI.

    Esta classe representa o ponto de entrada da aplicação e deve ser utilizada
    por aplicações externas (CLI, API, Desktop, Web, etc.).

    Toda a lógica da plataforma é delegada ao VersaKernel.
    """

    def __init__(self) -> None:
        """
        Cria uma nova instância da plataforma.
        """
        self._kernel = VersaKernel()

    def initialize(self) -> None:
        """
        Inicializa todos os componentes internos da plataforma.
        """
        self._kernel.initialize()

    def chat(self, message: str) -> AIResponse:
        """
        Processa uma mensagem enviada pelo usuário.

        Parameters
        ----------
        message : str
            Mensagem enviada pelo usuário.

        Returns
        -------
        AIResponse
            Resposta produzida pela IA.
        """
        return self._kernel.chat(message)

    def shutdown(self) -> None:
        """
        Finaliza a plataforma liberando recursos.
        """
        self._kernel.shutdown()

    @property
    def kernel(self) -> VersaKernel:
        """
        Retorna a instância do Kernel.

        Disponível apenas para casos específicos de integração e testes.
        """
        return self._kernel