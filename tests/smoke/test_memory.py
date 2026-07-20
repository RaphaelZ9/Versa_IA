"""
Smoke Test

Módulo:
Memory

Responsabilidade:
Validar a arquitetura básica do módulo de memória da Versa AI.

Autor: Raphael Wilson
"""

import unittest
from datetime import datetime, timedelta
from app.core.time_utils import utc_now
from app.domain.entities.memory.memory import Memory
from app.domain.entities.memory.memory_priority import MemoryPriority
from app.domain.entities.memory.memory_scope import MemoryScope
from app.domain.entities.memory.memory_type import MemoryType


class TestMemory(unittest.TestCase):
    """
    Testes básicos da arquitetura de memória.
    """

    def test_default_memory(self):
        """
        Valida a criação da memória com valores padrão.
        """

        memory = Memory()

        self.assertIsNotNone(memory.id)

        self.assertEqual(memory.title, "")

        self.assertEqual(memory.content, "")

        self.assertEqual(
            memory.memory_type,
            MemoryType.WORKING,
        )

        self.assertEqual(
            memory.scope,
            MemoryScope.SESSION,
        )

        self.assertEqual(
            memory.priority,
            MemoryPriority.NORMAL,
        )

        self.assertFalse(memory.is_expired)

    def test_add_remove_tags(self):
        """
        Valida inclusão e remoção de tags.
        """

        memory = Memory()

        memory.add_tag("oracle")
        memory.add_tag("apex")

        self.assertEqual(len(memory.tags), 2)

        self.assertTrue(memory.has_tags)

        memory.remove_tag("oracle")

        self.assertEqual(len(memory.tags), 1)

    def test_update_content(self):
        """
        Valida atualização do conteúdo.
        """

        memory = Memory()

        previous = memory.updated_at

        memory.update_content("Versa Energia")

        self.assertEqual(
            memory.content,
            "Versa Energia",
        )

        self.assertGreaterEqual(
            memory.updated_at,
            previous,
        )

    def test_touch(self):
        """
        Valida atualização da data de modificação.
        """

        memory = Memory()

        previous = memory.updated_at

        memory.touch()

        self.assertGreaterEqual(
            memory.updated_at,
            previous,
        )

    def test_permanent_memory(self):
        """
        Valida memórias permanentes.
        """

        memory = Memory(
            priority=MemoryPriority.PERMANENT
        )

        self.assertTrue(memory.is_permanent)

    def test_expired_memory(self):
        """
        Valida expiração de memória.
        """

        memory = Memory(
            expires_at=utc_now() - timedelta(days=1)
        )

        self.assertTrue(memory.is_expired)

    def test_not_expired_memory(self):
        """
        Valida memória ainda válida.
        """

        memory = Memory(
            expires_at=utc_now() + timedelta(days=1)
        )

        self.assertFalse(memory.is_expired)

    def test_metadata(self):
        """
        Valida utilização de metadados.
        """

        memory = Memory()

        memory.metadata["supplier"] = "ENEVA"

        self.assertEqual(
            memory.metadata["supplier"],
            "ENEVA",
        )


if __name__ == "__main__":

    unittest.main()