"""
Smoke Test

Módulo:
Conversation Manager

Responsabilidade:
Validar o ConversationManager.

Autor: Raphael Wilson
"""

import unittest

from app.conversation.conversation_manager import ConversationManager
from app.domain.entities.conversation.conversation import Conversation
from app.domain.entities.conversation.message import Message


class TestConversationManager(unittest.TestCase):
    """
    Testes do ConversationManager.
    """

    def setUp(self):
        """
        Inicializa o ambiente.
        """

        self.manager = ConversationManager()

    def test_remember(self):
        """
        Valida armazenamento.
        """

        conversation = Conversation()

        self.manager.remember(conversation)

        self.assertEqual(
            self.manager.count(),
            1,
        )

    def test_recall(self):
        """
        Valida recuperação.
        """

        conversation = Conversation()

        self.manager.remember(conversation)

        loaded = self.manager.recall(
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

        self.manager.remember(conversation)

        result = self.manager.append_message(
            conversation.id,
            Message(
                role="user",
                content="Olá Versa AI"
            ),
        )

        self.assertTrue(result)

        self.assertEqual(
            self.manager.message_count(
                conversation.id
            ),
            1,
        )

    def test_last_message(self):
        """
        Valida recuperação da última mensagem.
        """

        conversation = Conversation()

        self.manager.remember(conversation)

        self.manager.append_message(
            conversation.id,
            Message(
                role="assistant",
                content="Bom dia!"
            ),
        )

        last = self.manager.last_message(
            conversation.id
        )

        self.assertIsNotNone(last)

        self.assertEqual(
            last.content,
            "Bom dia!",
        )

    def test_clear_messages(self):
        """
        Valida limpeza das mensagens.
        """

        conversation = Conversation()

        self.manager.remember(conversation)

        self.manager.append_message(
            conversation.id,
            Message()
        )

        self.assertTrue(
            self.manager.clear_messages(
                conversation.id
            )
        )

        self.assertEqual(
            self.manager.message_count(
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

        self.manager.remember(conversation)

        result = self.manager.find_by_title(
            "finance"
        )

        self.assertEqual(
            len(result),
            1,
        )

    def test_find_with_messages(self):
        """
        Valida pesquisa de conversas com mensagens.
        """

        conversation = Conversation()

        conversation.add_message(
            Message(
                content="Olá"
            )
        )

        self.manager.remember(conversation)

        result = self.manager.find_with_messages()

        self.assertEqual(
            len(result),
            1,
        )

    def test_forget(self):
        """
        Valida remoção.
        """

        conversation = Conversation()

        self.manager.remember(conversation)

        self.assertTrue(
            self.manager.forget(
                conversation.id
            )
        )

        self.assertEqual(
            self.manager.count(),
            0,
        )


if __name__ == "__main__":
    unittest.main()