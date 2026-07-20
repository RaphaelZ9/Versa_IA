"""
Smoke Test

Módulo:
Intent Service

Responsabilidade:
Validar o IntentService.

Autor: Raphael Wilson
"""

import unittest

from app.domain.entities.intent.intent import Intent
from app.domain.entities.intent.intent_type import IntentType
from app.intent.repositories.in_memory_repository import (
    InMemoryIntentRepository,
)
from app.intent.services.intent_service import (
    IntentService,
)


class TestIntentService(unittest.TestCase):
    """
    Testes do IntentService.
    """

    def setUp(self):
        """
        Inicializa o ambiente de testes.
        """

        self.repository = InMemoryIntentRepository()
        self.service = IntentService(self.repository)

    def test_remember(self):
        """
        Valida armazenamento.
        """

        intent = Intent(
            type=IntentType.SEARCH,
            text="Pesquisar fatura",
        )

        self.service.remember(intent)

        self.assertEqual(
            self.service.count(),
            1,
        )

    def test_recall(self):
        """
        Valida recuperação.
        """

        intent = Intent(
            type=IntentType.CHAT,
            text="Olá",
        )

        self.service.remember(intent)

        loaded = self.service.recall(intent.id)

        self.assertIsNotNone(loaded)

        self.assertEqual(
            loaded.id,
            intent.id,
        )

    def test_update(self):
        """
        Valida atualização.
        """

        intent = Intent(
            text="Pesquisar"
        )

        self.service.remember(intent)

        intent.text = "Pesquisar PDF"

        self.service.update(intent)

        loaded = self.service.recall(intent.id)

        self.assertEqual(
            loaded.text,
            "Pesquisar PDF",
        )

    def test_forget(self):
        """
        Valida remoção.
        """

        intent = Intent()

        self.service.remember(intent)

        self.assertTrue(
            self.service.forget(intent.id)
        )

        self.assertEqual(
            self.service.count(),
            0,
        )

    def test_exists(self):
        """
        Valida existência.
        """

        intent = Intent()

        self.service.remember(intent)

        self.assertTrue(
            self.service.exists(intent.id)
        )

    def test_find_by_type(self):
        """
        Valida pesquisa por tipo.
        """

        self.service.remember(
            Intent(type=IntentType.SEARCH)
        )

        self.service.remember(
            Intent(type=IntentType.CHAT)
        )

        result = self.service.find_by_type(
            IntentType.SEARCH
        )

        self.assertEqual(
            len(result),
            1,
        )

    def test_find_by_confidence(self):
        """
        Valida pesquisa por confiança.
        """

        self.service.remember(
            Intent(confidence=0.95)
        )

        self.service.remember(
            Intent(confidence=0.30)
        )

        result = self.service.find_by_confidence(
            0.90
        )

        self.assertEqual(
            len(result),
            1,
        )

    def test_find_by_text(self):
        """
        Valida pesquisa textual.
        """

        self.service.remember(
            Intent(text="Pesquisar nota fiscal")
        )

        self.service.remember(
            Intent(text="Enviar email")
        )

        result = self.service.find_by_text(
            "nota"
        )

        self.assertEqual(
            len(result),
            1,
        )

        self.assertIn(
            "nota",
            result[0].text.lower(),
        )

    def test_clear(self):
        """
        Valida limpeza.
        """

        self.service.remember(Intent())
        self.service.remember(Intent())

        self.service.clear()

        self.assertEqual(
            self.service.count(),
            0,
        )


if __name__ == "__main__":
    unittest.main()