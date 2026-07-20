"""
Smoke Test

Módulo:
Memory Manager

Responsabilidade:
Validar a implementação do MemoryManager.

Autor: Raphael Wilson
"""

import unittest
from datetime import timedelta

from app.core.time_utils import utc_now
from app.domain.entities.memory.memory import Memory
from app.memory.memory_manager import MemoryManager


class TestMemoryManager(unittest.TestCase):
    """
    Testes básicos do MemoryManager.
    """

    def setUp(self):
        """
        Inicializa o ambiente de testes.
        """

        self.manager = MemoryManager()

    def test_remember(self):
        """
        Valida o armazenamento de uma memória.
        """

        memory = Memory(title="Oracle")

        self.manager.remember(memory)

        self.assertEqual(
            self.manager.count(),
            1,
        )

    def test_recall(self):
        """
        Valida recuperação de memória.
        """

        memory = Memory(title="APEX")

        self.manager.remember(memory)

        loaded = self.manager.recall(memory.id)

        self.assertIsNotNone(loaded)

        self.assertEqual(
            loaded.title,
            "APEX",
        )

    def test_update(self):
        """
        Valida atualização da memória.
        """

        memory = Memory(title="Versa")

        self.manager.remember(memory)

        memory.title = "Versa Energia"

        self.manager.update(memory)

        loaded = self.manager.recall(memory.id)

        self.assertEqual(
            loaded.title,
            "Versa Energia",
        )

    def test_exists(self):
        """
        Valida existência da memória.
        """

        memory = Memory()

        self.manager.remember(memory)

        self.assertTrue(
            self.manager.exists(memory.id)
        )

    def test_get_all(self):
        """
        Valida listagem das memórias.
        """

        self.manager.remember(Memory())

        self.manager.remember(Memory())

        self.assertEqual(
            len(self.manager.get_all()),
            2,
        )

    def test_forget(self):
        """
        Valida remoção de memória.
        """

        memory = Memory()

        self.manager.remember(memory)

        self.assertTrue(
            self.manager.forget(memory.id)
        )

        self.assertEqual(
            self.manager.count(),
            0,
        )

    def test_clear(self):
        """
        Valida limpeza das memórias.
        """

        self.manager.remember(Memory())

        self.manager.remember(Memory())

        self.manager.clear()

        self.assertEqual(
            self.manager.count(),
            0,
        )

    def test_cleanup_expired(self):
        """
        Valida remoção de memórias expiradas.
        """

        expired = Memory(
            title="Expirada",
            expires_at=utc_now() - timedelta(days=1),
        )

        valid = Memory(
            title="Válida",
            expires_at=utc_now() + timedelta(days=1),
        )

        self.manager.remember(expired)

        self.manager.remember(valid)

        removed = self.manager.cleanup_expired()

        self.assertEqual(
            removed,
            1,
        )

        self.assertEqual(
            self.manager.count(),
            1,
        )


if __name__ == "__main__":

    unittest.main()