"""
Smoke Test

Módulo:
Conversation Service

Responsabilidade:
Validar o ConversationService.

Autor: Raphael Wilson
"""

import unittest

from app.conversation.repositories.memory_repository import (
    MemoryConversationRepository,
)
from app.conversation.services.conversation_service import (
    ConversationService,
)
from app.domain.entities.conversation.conversation import Conversation
from app.domain.entities.conversation.message import Message


class TestConversationService(unittest.TestCase):
    """
    Testes do ConversationService.
    """

    def setUp(self):
        """
        Inicializa o ambiente.
        """

        self.repository = MemoryConversationRepository()

        self.service = ConversationService(
            self.repository
        )

    def test_remember(self):
        """
        Valida armazenamento.
        """

        conversation = Conversation()

        self.service.remember(conversation)

        self.assertEqual(
            self.service.count(),
            1,
        )

    def test_recall(self):
        """
        Valida recuperação.
        """

        conversation = Conversation()

        self.service.remember(conversation)

        loaded = self.service.recall(
            conversation.id
        )

        self.assertEqual(
            loaded.id,
            conversation.id,
        )

    def test_append_message(self):
        """
        Valida inclusão de mensagem.
        """

        conversation = Conversation()

        self.service.remember(conversation)

        self.assertTrue(
            self.service.append_message(
                conversation.id,
                Message(
                    role="user",
                    content="Olá"
                ),
            )
        )

        self.assertEqual(
            self.service.message_count(
                conversation.id
            ),
            1,
        )

    def test_last_message(self):
        """
        Valida recuperação da última mensagem.
        """

        conversation = Conversation()

        self.service.remember(conversation)

        self.service.append_message(
            conversation.id,
            Message(
                role="assistant",
                content="Resposta"
            ),
        )

        last = self.service.last_message(
            conversation.id
        )

        self.assertIsNotNone(last)

        self.assertEqual(
            last.content,
            "Resposta",
        )

    def test_clear_messages(self):
        """
        Valida limpeza das mensagens.
        """

        conversation = Conversation()

        self.service.remember(conversation)

        self.service.append_message(
            conversation.id,
            Message()
        )

        self.assertTrue(
            self.service.clear_messages(
                conversation.id
            )
        )

        self.assertEqual(
            self.service.message_count(
                conversation.id
            ),
            0,
        )

    def test_find_by_title(self):
        """
        Valida pesquisa por título.
        """

        conversation = Conversation(
            title="Financeiro"
        )

        self.service.remember(conversation)

        result = self.service.find_by_title(
            "finance"
        )

        self.assertEqual(
            len(result),
            1,
        )

    def test_find_with_messages(self):
        """
        Valida pesquisa por conversas com mensagens.
        """

        conversation = Conversation()

        conversation.add_message(
            Message(content="Olá")
        )

        self.service.remember(conversation)

        result = self.service.find_with_messages()

        self.assertEqual(
            len(result),
            1,
        )


if __name__ == "__main__":
    unittest.main()