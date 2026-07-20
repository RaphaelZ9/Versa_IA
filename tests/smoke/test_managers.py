"""
Smoke Test

Módulo:
Managers

Responsabilidade:
Validar a arquitetura básica dos Managers da Versa AI.

Autor: Raphael Wilson
"""

import unittest

from app.managers.base_manager import BaseManager
from app.tools.tool_manager import ToolManager
from app.knowledge.knowledge_manager import KnowledgeManager


class TestManagers(unittest.TestCase):

    def test_tool_manager(self):

        manager = ToolManager()

        self.assertIsInstance(manager, BaseManager)

        self.assertEqual(manager.count(), 0)

    def test_knowledge_manager(self):

        manager = KnowledgeManager()

        self.assertIsInstance(manager, BaseManager)

        self.assertEqual(manager.count(), 5)

    def test_register_unregister(self):

        manager = ToolManager()

        class Dummy:
            pass

        component = Dummy()

        manager.register(component)

        self.assertEqual(manager.count(), 1)

        manager.unregister(component)

        self.assertEqual(manager.count(), 0)

    def test_clear(self):

        manager = ToolManager()

        class Dummy:
            pass

        manager.register(Dummy())
        manager.register(Dummy())

        self.assertEqual(manager.count(), 2)

        manager.clear()

        self.assertEqual(manager.count(), 0)

    def test_shutdown(self):

        manager = ToolManager()

        class Dummy:

            def __init__(self):

                self.closed = False

            def shutdown(self):

                self.closed = True

        component = Dummy()

        manager.register(component)

        manager.shutdown()

        self.assertTrue(component.closed)


if __name__ == "__main__":

    unittest.main()