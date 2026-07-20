"""
Smoke Test

Módulo:
Intent Repository

Responsabilidade:
Validar a implementação do InMemoryIntentRepository.

Autor: Raphael Wilson
"""

import unittest

from app.domain.entities.intent.intent import Intent
from app.domain.entities.intent.intent_type import IntentType
from app.intent.repositories.in_memory_repository import (
    InMemoryIntentRepository,
)


class TestIntentRepository(unittest.TestCase):
    """
    Testes do repositório de intenções.
    """

    def setUp(self):
        """
        Inicializa o ambiente de testes.
        """

        self.repository = InMemoryIntentRepository()

    def test_save(self):
        """
        Valida armazenamento.
        """

        intent = Intent(
            type=IntentType.SEARCH,
            text="Pesquisar fatura",
        )

        self.repository.save(intent)

        self.assertEqual(
            self.repository.count(),
            1,
        )

    def test_get_by_id(self):
        """
        Valida recuperação por ID.
        """

        intent = Intent(
            type=IntentType.CHAT,
            text="Olá",
        )

        self.repository.save(intent)

        loaded = self.repository.get_by_id(intent.id)

        self.assertIsNotNone(loaded)

        self.assertEqual(
            loaded.id,
            intent.id,
        )

    def test_get_all(self):
        """
        Valida listagem.
        """

        self.repository.save(Intent())
        self.repository.save(Intent())

        self.assertEqual(
            len(self.repository.get_all()),
            2,
        )

    def test_update(self):
        """
        Valida atualização.
        """

        intent = Intent(
            text="Pesquisar",
        )

        self.repository.save(intent)

        intent.text = "Pesquisar PDF"

        self.repository.update(intent)

        loaded = self.repository.get_by_id(intent.id)

        self.assertEqual(
            loaded.text,
            "Pesquisar PDF",
        )

    def test_delete(self):
        """
        Valida remoção.
        """

        intent = Intent()

        self.repository.save(intent)

        self.assertTrue(
            self.repository.delete(intent.id)
        )

        self.assertEqual(
            self.repository.count(),
            0,
        )

    def test_exists(self):
        """
        Valida existência.
        """

        intent = Intent()

        self.repository.save(intent)

        self.assertTrue(
            self.repository.exists(intent.id)
        )

    def test_clear(self):
        """
        Valida limpeza.
        """

        self.repository.save(Intent())
        self.repository.save(Intent())

        self.repository.clear()

        self.assertEqual(
            self.repository.count(),
            0,
        )

    def test_find_by_type(self):
        """
        Valida pesquisa por tipo.
        """

        self.repository.save(
            Intent(type=IntentType.SEARCH)
        )

        self.repository.save(
            Intent(type=IntentType.CHAT)
        )

        result = self.repository.find_by_type(
            IntentType.SEARCH
        )

        self.assertEqual(
            len(result),
            1,
        )

        self.assertEqual(
            result[0].type,
            IntentType.SEARCH,
        )

    def test_find_by_confidence(self):
        """
        Valida pesquisa por confiança.
        """

        self.repository.save(
            Intent(
                confidence=0.95
            )
        )

        self.repository.save(
            Intent(
                confidence=0.40
            )
        )

        result = self.repository.find_by_confidence(
            0.90
        )

        self.assertEqual(
            len(result),
            1,
        )

        self.assertGreaterEqual(
            result[0].confidence,
            0.90,
        )

    def test_find_by_text(self):
        """
        Valida pesquisa textual.
        """

        self.repository.save(
            Intent(
                text="Pesquisar fatura Eneva"
            )
        )

        self.repository.save(
            Intent(
                text="Enviar email"
            )
        )

        result = self.repository.find_by_text(
            "fatura"
        )

        self.assertEqual(
            len(result),
            1,
        )

        self.assertIn(
            "fatura",
            result[0].text.lower(),
        )


if __name__ == "__main__":

    unittest.main()