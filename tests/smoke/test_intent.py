"""
Smoke Test

Módulo:
Intent Entity

Responsabilidade:
Validar a entidade Intent.

Autor: Raphael Wilson
"""

import unittest

from app.domain.entities.intent.intent import Intent
from app.domain.entities.intent.intent_type import IntentType


class TestIntent(unittest.TestCase):
    """
    Testes da entidade Intent.
    """

    def test_default_values(self):
        """
        Valida valores padrão.
        """

        intent = Intent()

        self.assertEqual(
            intent.type,
            IntentType.UNKNOWN,
        )

        self.assertEqual(
            intent.confidence,
            0.0,
        )

        self.assertFalse(
            intent.has_entities,
        )

        self.assertFalse(
            intent.has_tools,
        )

    def test_add_entity(self):
        """
        Valida inclusão de entidade.
        """

        intent = Intent()

        intent.add_entity(
            "empresa",
            "Versa Energia",
        )

        self.assertTrue(
            intent.has_entities,
        )

        self.assertEqual(
            intent.entities["empresa"],
            "Versa Energia",
        )

    def test_add_tool(self):
        """
        Valida inclusão de ferramenta.
        """

        intent = Intent()

        intent.add_tool(
            "EmailTool",
        )

        self.assertTrue(
            intent.has_tools,
        )

        self.assertEqual(
            len(intent.suggested_tools),
            1,
        )

    def test_duplicate_tool(self):
        """
        Não deve permitir ferramentas duplicadas.
        """

        intent = Intent()

        intent.add_tool("EmailTool")
        intent.add_tool("EmailTool")

        self.assertEqual(
            len(intent.suggested_tools),
            1,
        )

    def test_clear_entities(self):
        """
        Valida limpeza das entidades.
        """

        intent = Intent()

        intent.add_entity(
            "empresa",
            "Versa",
        )

        intent.clear_entities()

        self.assertFalse(
            intent.has_entities,
        )

    def test_clear_tools(self):
        """
        Valida limpeza das ferramentas.
        """

        intent = Intent()

        intent.add_tool(
            "PDFTool",
        )

        intent.clear_tools()

        self.assertFalse(
            intent.has_tools,
        )

    def test_metadata(self):
        """
        Valida inclusão de metadados.
        """

        intent = Intent()

        intent.add_metadata(
            "modelo",
            "llama3",
        )

        self.assertEqual(
            intent.metadata["modelo"],
            "llama3",
        )

    def test_to_dict(self):
        """
        Valida serialização.
        """

        intent = Intent(
            type=IntentType.SEARCH,
            text="Pesquisar fatura",
            confidence=0.98,
        )

        data = intent.to_dict()

        self.assertEqual(
            data["type"],
            "search",
        )

        self.assertEqual(
            data["text"],
            "Pesquisar fatura",
        )

        self.assertEqual(
            data["confidence"],
            0.98,
        )


if __name__ == "__main__":

    unittest.main()