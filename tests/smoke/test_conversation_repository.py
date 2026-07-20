"""
Smoke Test

Módulo:
Conversation Repository

Responsabilidade:
Validar a implementação do MemoryConversationRepository.

Autor: Raphael Wilson
"""

import unittest

from app.conversation.repositories.memory_repository import (
    MemoryConversationRepository,
)
from app.domain.entities.conversation.conversation import Conversation
from app.domain.entities.conversation.message import Message


class TestConversationRepository(unittest.TestCase):
    """
    Testes do repositório de Conversation.
    """

    def setUp(self):
        """
        Inicializa o ambiente de testes.
        """

        self.repository = MemoryConversationRepository()

    def test_save(self):
        """
        Valida armazenamento.
        """

        conversation = Conversation(title="Teste")

        self.repository.save(conversation)

        self.assertEqual(
            self.repository.count(),
            1,
        )

    def test_get_by_id(self):
        """
        Valida recuperação por ID.
        """

        conversation = Conversation(title="Teste")

        self.repository.save(conversation)

        loaded = self.repository.get_by_id(conversation.id)

        self.assertIsNotNone(loaded)

        self.assertEqual(
            loaded.id,
            conversation.id,
        )

    def test_get_all(self):
        """
        Valida listagem.
        """

        self.repository.save(Conversation())
        self.repository.save(Conversation())

        self.assertEqual(
            len(self.repository.get_all()),
            2,
        )

    def test_update(self):
        """
        Valida atualização.
        """

        conversation = Conversation(title="Primeiro")

        self.repository.save(conversation)

        conversation.title = "Segundo"

        self.repository.update(conversation)

        loaded = self.repository.get_by_id(conversation.id)

        self.assertEqual(
            loaded.title,
            "Segundo",
        )

    def test_delete(self):
        """
        Valida remoção.
        """

        conversation = Conversation()

        self.repository.save(conversation)

        self.assertTrue(
            self.repository.delete(conversation.id)
        )

        self.assertEqual(
            self.repository.count(),
            0,
        )

    def test_exists(self):
        """
        Valida existência.
        """

        conversation = Conversation()

        self.repository.save(conversation)

        self.assertTrue(
            self.repository.exists(conversation.id)
        )

    def test_clear(self):
        """
        Valida limpeza.
        """

        self.repository.save(Conversation())
        self.repository.save(Conversation())

        self.repository.clear()

        self.assertEqual(
            self.repository.count(),
            0,
        )

    def test_find_by_title(self):
        """
        Valida pesquisa por título.
        """

        self.repository.save(
            Conversation(title="Financeiro")
        )

        self.repository.save(
            Conversation(title="Compras")
        )

        result = self.repository.find_by_title(
            "finance"
        )

        self.assertEqual(
            len(result),
            1,
        )

        self.assertEqual(
            result[0].title,
            "Financeiro",
        )

    def test_find_by_metadata(self):
        """
        Valida pesquisa por metadado.
        """

        conversation = Conversation()

        conversation.add_metadata(
            "cliente",
            "Versa"
        )

        self.repository.save(conversation)

        result = self.repository.find_by_metadata(
            "cliente",
            "Versa",
        )

        self.assertEqual(
            len(result),
            1,
        )

    def test_find_with_messages(self):
        """
        Valida pesquisa por conversas que possuem mensagens.
        """

        conversation = Conversation()

        conversation.add_message(
            Message(
                role="user",
                content="Olá"
            )
        )

        self.repository.save(conversation)

        self.repository.save(
            Conversation()
        )

        result = self.repository.find_with_messages()

        self.assertEqual(
            len(result),
            1,
        )

        self.assertEqual(
            result[0].message_count,
            1,
        )


if __name__ == "__main__":

    unittest.main()