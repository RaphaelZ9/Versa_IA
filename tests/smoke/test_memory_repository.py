"""
Smoke Test

Módulo:
Memory Repository

Responsabilidade:
Validar a implementação do InMemoryRepository.

Autor: Raphael Wilson
"""

import unittest

from app.domain.entities.memory.memory import Memory
from app.memory.repositories.in_memory_repository import InMemoryRepository


class TestMemoryRepository(unittest.TestCase):

    def setUp(self):

        self.repository = InMemoryRepository()

    def test_save(self):

        memory = Memory(title="Teste")

        self.repository.save(memory)

        self.assertEqual(self.repository.count(), 1)

    def test_get_by_id(self):

        memory = Memory(title="Oracle")

        self.repository.save(memory)

        loaded = self.repository.get_by_id(memory.id)

        self.assertIsNotNone(loaded)

        self.assertEqual(loaded.id, memory.id)

    def test_get_all(self):

        self.repository.save(Memory())

        self.repository.save(Memory())

        self.assertEqual(
            len(self.repository.get_all()),
            2,
        )

    def test_exists(self):

        memory = Memory()

        self.repository.save(memory)

        self.assertTrue(
            self.repository.exists(memory.id)
        )

    def test_update(self):

        memory = Memory(
            title="Versa"
        )

        self.repository.save(memory)

        memory.title = "Versa Energia"

        self.repository.update(memory)

        loaded = self.repository.get_by_id(memory.id)

        self.assertEqual(
            loaded.title,
            "Versa Energia"
        )

    def test_delete(self):

        memory = Memory()

        self.repository.save(memory)

        self.assertTrue(
            self.repository.delete(memory.id)
        )

        self.assertEqual(
            self.repository.count(),
            0,
        )

    def test_clear(self):

        self.repository.save(Memory())

        self.repository.save(Memory())

        self.repository.clear()

        self.assertEqual(
            self.repository.count(),
            0,
        )


if __name__ == "__main__":

    unittest.main()