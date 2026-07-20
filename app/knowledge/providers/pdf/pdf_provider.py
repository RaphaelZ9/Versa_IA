"""
Versa AI

Arquivo:
pdf_provider.py

Responsabilidade:
Implementar o Provider responsável por realizar pesquisas
em documentos PDF.

Este Provider atua como um adaptador entre o
KnowledgeManager e os mecanismos de leitura de arquivos PDF.

Sua responsabilidade é apenas pesquisar e retornar
informações encontradas em documentos PDF.

Não realiza ranking, filtragem ou processamento dos
resultados retornados.

Autor: Raphael Wilson
"""

from __future__ import annotations

from app.core.logger import get_logger
from app.domain.entities.search_result import SearchResult
from app.knowledge.providers.base_provider import BaseProvider


class PDFProvider(BaseProvider):

    def __init__(self) -> None:

        super().__init__(
            provider_id="pdf",
            name="PDF Provider",
            description="Provider responsável por pesquisas em documentos PDF.",
            provider_type="pdf",
            priority=90,
        )

        self._logger = get_logger("PDFProvider")

    def initialize(self) -> None:

        self.initialized = True

        self._logger.info("PDFProvider inicializado.")

    def is_available(self) -> bool:

        return self.initialized

    def search(self, query: str) -> SearchResult:

        self._logger.info(f"Pesquisando em PDFs: {query}")

        return SearchResult(
            success=True,
            source=self.provider_type,
            execution_time=0.0,
        )

    def shutdown(self) -> None:

        self.initialized = False

        self._logger.info("PDFProvider finalizado.")