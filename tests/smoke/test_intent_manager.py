"""
Smoke Test

Módulo:
Intent Manager

Responsabilidade:
Validar o IntentManager.

Autor: Raphael Wilson
"""

import unittest

from app.domain.entities.intent.intent import Intent
from app.domain.entities.intent.intent_type import IntentType
from app.intent.intent_manager import IntentManager


class TestIntentManager(unittest.TestCase):
    """
    Testes do IntentManager.
    """

    def setUp(self):
        """
        Inicializa o ambiente de testes.
        """

        self.manager = IntentManager()

    def test_remember(self):
        """
        Valida armazenamento.
        """

        intent = Intent(
            type=IntentType.SEARCH,
            text="Pesquisar contrato",
        )

        self.manager.remember(intent)

        self.assertEqual(
            self.manager.count(),
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

        self.manager.remember(intent)

        loaded = self.manager.recall(intent.id)

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

        self.manager.remember(intent)

        intent.text = "Pesquisar PDF"

        self.manager.update(intent)

        loaded = self.manager.recall(intent.id)

        self.assertEqual(
            loaded.text,
            "Pesquisar PDF",
        )

    def test_forget(self):
        """
        Valida remoção.
        """

        intent = Intent()

        self.manager.remember(intent)

        self.assertTrue(
            self.manager.forget(intent.id)
        )

        self.assertEqual(
            self.manager.count(),
            0,
        )

    def test_exists(self):
        """
        Valida existência.
        """

        intent = Intent()

        self.manager.remember(intent)

        self.assertTrue(
            self.manager.exists(intent.id)
        )

    def test_find_by_type(self):
        """
        Valida pesquisa por tipo.
        """

        self.manager.remember(
            Intent(type=IntentType.SEARCH)
        )

        self.manager.remember(
            Intent(type=IntentType.CHAT)
        )

        result = self.manager.find_by_type(
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

        self.manager.remember(
            Intent(confidence=0.95)
        )

        self.manager.remember(
            Intent(confidence=0.40)
        )

        result = self.manager.find_by_confidence(
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

        self.manager.remember(
            Intent(text="Pesquisar nota fiscal")
        )

        self.manager.remember(
            Intent(text="Enviar email")
        )

        result = self.manager.find_by_text(
            "nota"
        )

        self.assertEqual(
            len(result),
            1,
        )

    def test_clear(self):
        """
        Valida limpeza.
        """

        self.manager.remember(Intent())
        self.manager.remember(Intent())

        self.manager.clear()

        self.assertEqual(
            self.manager.count(),
            0,
        )


if __name__ == "__main__":
    unittest.main()