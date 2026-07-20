"""
Smoke Test

Módulo:
Providers

Responsabilidade:
Validar a arquitetura básica dos Providers da Versa AI.

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


class TestProviders(unittest.TestCase):

    def _validate_provider(self, provider: BaseProvider):

        self.assertIsInstance(provider, BaseProvider)

        provider.initialize()

        self.assertTrue(provider.is_available())

        result = provider.search("teste")

        self.assertIsInstance(result, SearchResult)

        provider.shutdown()

        self.assertFalse(provider.is_available())

    def test_internet_provider(self):

        self._validate_provider(InternetProvider())

    def test_pdf_provider(self):

        self._validate_provider(PDFProvider())

    def test_api_provider(self):

        self._validate_provider(APIProvider())

    def test_supabase_provider(self):

        self._validate_provider(SupabaseProvider())

    def test_email_provider(self):

        self._validate_provider(EmailProvider())


if __name__ == "__main__":

    unittest.main()