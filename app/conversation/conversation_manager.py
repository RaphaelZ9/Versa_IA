"""
Versa AI

Arquivo:
conversation_manager.py

Responsabilidade:
Orquestrar as operações relacionadas às conversas e construir
o contexto da requisição.

O ConversationManager representa a interface pública do
módulo Conversation.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.ai_core.context.context_builder import ContextBuilder
from app.ai_core.context.context_package import ContextPackage
from app.ai_core.context.context_request import ContextRequest
from app.conversation.repositories.base_conversation_repository import (
    BaseConversationRepository,
)
from app.conversation.repositories.memory_repository import (
    MemoryConversationRepository,
)
from app.conversation.services.conversation_service import (
    ConversationService,
)
from app.domain.entities.conversation.conversation import Conversation
from app.domain.entities.conversation.message import Message


class ConversationManager:
    """
    Gerenciador responsável pelas operações de Conversation.
    """

    def __init__(
        self,
        repository: BaseConversationRepository | None = None,
    ) -> None:
        """
        Inicializa o ConversationManager.

        Args:
            repository:
                Repositório utilizado para persistência.
                Caso não informado, utiliza MemoryConversationRepository.
        """

        self._repository = (
            repository
            if repository is not None
            else MemoryConversationRepository()
        )

        self._service = ConversationService(
            self._repository
        )

        self._context_builder = ContextBuilder()

    @property
    def repository(self) -> BaseConversationRepository:
        """
        Retorna o repositório utilizado.
        """

        return self._repository

    @property
    def service(self) -> ConversationService:
        """
        Retorna o serviço utilizado.
        """

        return self._service

    # ==========================================================
    # Context
    # ==========================================================

    def build_context(
        self,
        *,
        system_prompt: str | None = None,
    ) -> ContextPackage:
        """
        Constrói o contexto utilizado na requisição atual.

        O parâmetro system_prompt é mantido como sobrescrita opcional
        por compatibilidade com a API pública do Kernel.
        """

        request = ContextRequest()

        context = self._context_builder.build(request)

        if system_prompt is not None:
            context.system_prompt = system_prompt

        return context

    # ==========================================================
    # CRUD
    # ==========================================================

    def remember(
        self,
        conversation: Conversation,
    ) -> None:
        """
        Armazena uma conversa.
        """

        self._service.remember(conversation)

    def recall(
        self,
        conversation_id: str,
    ) -> Conversation | None:
        """
        Recupera uma conversa.
        """

        return self._service.recall(conversation_id)

    def update(
        self,
        conversation: Conversation,
    ) -> None:
        """
        Atualiza uma conversa.
        """

        self._service.update(conversation)

    def forget(
        self,
        conversation_id: str,
    ) -> bool:
        """
        Remove uma conversa.
        """

        return self._service.forget(conversation_id)

    def get_all(self) -> list[Conversation]:
        """
        Retorna todas as conversas.
        """

        return self._service.get_all()

    def exists(
        self,
        conversation_id: str,
    ) -> bool:
        """
        Verifica se uma conversa existe.
        """

        return self._service.exists(conversation_id)

    def count(self) -> int:
        """
        Retorna a quantidade de conversas.
        """

        return self._service.count()

    def clear(self) -> None:
        """
        Remove todas as conversas.
        """

        self._service.clear()

    # ==========================================================
    # Consultas
    # ==========================================================

    def find_by_title(
        self,
        title: str,
    ) -> list[Conversation]:
        """
        Pesquisa conversas pelo título.
        """

        return self._service.find_by_title(title)

    def find_by_metadata(
        self,
        key: str,
        value: str,
    ) -> list[Conversation]:
        """
        Pesquisa conversas por metadado.
        """

        return self._service.find_by_metadata(
            key,
            value,
        )

    def find_with_messages(self) -> list[Conversation]:
        """
        Retorna apenas conversas que possuem mensagens.
        """

        return self._service.find_with_messages()

    # ==========================================================
    # Operações do domínio
    # ==========================================================

    def append_message(
        self,
        conversation_id: str,
        message: Message,
    ) -> bool:
        """
        Adiciona uma mensagem à conversa.
        """

        return self._service.append_message(
            conversation_id,
            message,
        )

    def last_message(
        self,
        conversation_id: str,
    ) -> Message | None:
        """
        Retorna a última mensagem da conversa.
        """

        return self._service.last_message(
            conversation_id,
        )

    def message_count(
        self,
        conversation_id: str,
    ) -> int:
        """
        Retorna a quantidade de mensagens.
        """

        return self._service.message_count(
            conversation_id,
        )

    def clear_messages(
        self,
        conversation_id: str,
    ) -> bool:
        """
        Remove todas as mensagens da conversa.
        """

        return self._service.clear_messages(
            conversation_id,
        )