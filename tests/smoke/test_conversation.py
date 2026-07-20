"""
Smoke Test

Módulo:
Conversation Entity

Responsabilidade:
Validar a entidade Conversation.

Autor: Raphael Wilson
"""

import unittest

from app.domain.entities.conversation.conversation import Conversation
from app.domain.entities.conversation.message import Message


class TestConversation(unittest.TestCase):
    """
    Testes da entidade Conversation.
    """

    def test_default_values(self):
        """
        Valida os valores padrão.
        """

        conversation = Conversation()

        self.assertTrue(conversation.is_empty)
        self.assertEqual(conversation.message_count, 0)
        self.assertFalse(conversation.has_metadata)

    def test_add_message(self):
        """
        Valida inclusão de mensagem.
        """

        conversation = Conversation()

        message = Message(
            role="user",
            content="Olá Versa AI"
        )

        conversation.add_message(message)

        self.assertEqual(
            conversation.message_count,
            1
        )

        self.assertFalse(
            conversation.is_empty
        )

    def test_last_message(self):
        """
        Valida recuperação da última mensagem.
        """

        conversation = Conversation()

        conversation.add_message(
            Message(
                role="user",
                content="Primeira"
            )
        )

        conversation.add_message(
            Message(
                role="assistant",
                content="Segunda"
            )
        )

        last = conversation.last_message()

        self.assertIsNotNone(last)

        self.assertEqual(
            last.content,
            "Segunda"
        )

    def test_remove_message(self):
        """
        Valida remoção de mensagem.
        """

        conversation = Conversation()

        message = Message(
            content="Teste"
        )

        conversation.add_message(message)

        self.assertTrue(
            conversation.remove_message(message.id)
        )

        self.assertEqual(
            conversation.message_count,
            0
        )

    def test_clear_messages(self):
        """
        Valida limpeza das mensagens.
        """

        conversation = Conversation()

        conversation.add_message(Message())
        conversation.add_message(Message())

        conversation.clear_messages()

        self.assertTrue(
            conversation.is_empty
        )

    def test_metadata(self):
        """
        Valida inclusão de metadados.
        """

        conversation = Conversation()

        conversation.add_metadata(
            "cliente",
            "Versa"
        )

        self.assertTrue(
            conversation.has_metadata
        )

        self.assertEqual(
            conversation.metadata["cliente"],
            "Versa"
        )

    def test_clear_metadata(self):
        """
        Valida limpeza dos metadados.
        """

        conversation = Conversation()

        conversation.add_metadata(
            "cliente",
            "Versa"
        )

        conversation.clear_metadata()

        self.assertFalse(
            conversation.has_metadata
        )

    def test_to_dict(self):
        """
        Valida serialização.
        """

        conversation = Conversation(
            title="Teste"
        )

        conversation.add_message(
            Message(
                role="user",
                content="Olá"
            )
        )

        data = conversation.to_dict()

        self.assertEqual(
            data["title"],
            "Teste"
        )

        self.assertEqual(
            len(data["messages"]),
            1
        )


if __name__ == "__main__":

    unittest.main()