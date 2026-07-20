"""
Smoke Test

Módulo:
Memory Service

Responsabilidade:
Validar a implementação do MemoryService.

Autor: Raphael Wilson
"""

from datetime import timedelta
import unittest

from app.core.time_utils import utc_now
from app.domain.entities.memory.memory import Memory
from app.memory.repositories.memory_repository import InMemoryRepository
from app.memory.services.memory_service import MemoryService


class TestMemoryService(unittest.TestCase):
    """
    Testes básicos do MemoryService.
    """

    def setUp(self):
        """
        Inicializa o ambiente de testes.
        """

        self.repository = InMemoryRepository()

        self.service = MemoryService(
            repository=self.repository
        )

    def test_remember(self):
        """
        Valida o armazenamento de uma memória.
        """

        memory = Memory(title="Oracle")

        self.service.remember(memory)

        self.assertEqual(
            self.service.count(),
            1,
        )

    def test_recall(self):
        """
        Valida recuperação de memória.
        """

        memory = Memory(title="APEX")

        self.service.remember(memory)

        loaded = self.service.recall(memory.id)

        self.assertIsNotNone(loaded)

        self.assertEqual(
            loaded.title,
            "APEX",
        )

    def test_update(self):
        """
        Valida atualização de memória.
        """

        memory = Memory(title="Versa")

        self.service.remember(memory)

        memory.title = "Versa Energia"

        self.service.update(memory)

        loaded = self.service.recall(memory.id)

        self.assertEqual(
            loaded.title,
            "Versa Energia",
        )

    def test_exists(self):
        """
        Valida existência da memória.
        """

        memory = Memory()

        self.service.remember(memory)

        self.assertTrue(
            self.service.exists(memory.id)
        )

    def test_get_all(self):
        """
        Valida listagem das memórias.
        """

        self.service.remember(Memory())

        self.service.remember(Memory())

        self.assertEqual(
            len(self.service.get_all()),
            2,
        )

    def test_forget(self):
        """
        Valida remoção da memória.
        """

        memory = Memory()

        self.service.remember(memory)

        self.assertTrue(
            self.service.forget(memory.id)
        )

        self.assertEqual(
            self.service.count(),
            0,
        )

    def test_clear(self):
        """
        Valida limpeza do repositório.
        """

        self.service.remember(Memory())

        self.service.remember(Memory())

        self.service.clear()

        self.assertEqual(
            self.service.count(),
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

        self.service.remember(expired)

        self.service.remember(valid)

        removed = self.service.cleanup_expired()

        self.assertEqual(
            removed,
            1,
        )

        self.assertEqual(
            self.service.count(),
            1,
        )


if __name__ == "__main__":

    unittest.main()