"""
Integration Test

Módulo:
Providers

Responsabilidade:
Validar a integração entre todos os Providers da Versa AI
através da interface definida pela BaseProvider.

Autor: Raphael Wilson
"""

import unittest

from app.domain.entities.search_result import SearchResult
from app.knowledge.providers.base_provider import BaseProvider

from app.knowledge.providers.internet.internet_provider import InternetProvider
from app.knowledge.providers.pdf.pdf_provider import PDFProvider
from app.knowledge.providers.api.api_provider import APIProvider
from app.knowledge.providers.supabase.supabase_provider import SupabaseProvider
from app.knowledge.providers.email.email_provider import EmailProvider


class TestProvidersIntegration(unittest.TestCase):

    def setUp(self) -> None:

        self.providers: list[BaseProvider] = [
            InternetProvider(),
            PDFProvider(),
            APIProvider(),
            SupabaseProvider(),
            EmailProvider(),
        ]

    def test_all_providers_follow_same_contract(self):

        for provider in self.providers:

            provider.initialize()

            self.assertTrue(provider.is_available())

            result = provider.search("Versa Energia")

            self.assertIsInstance(result, SearchResult)

            self.assertTrue(result.success)

            self.assertEqual(result.source, provider.provider_type)

            provider.shutdown()

            self.assertFalse(provider.is_available())


if __name__ == "__main__":

    unittest.main()