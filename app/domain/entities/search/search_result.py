"""
Versa AI

Arquivo:
search_result.py

Responsabilidade:
Representar o resultado de uma pesquisa realizada por um
Provider de conhecimento.

Esta entidade encapsula o resultado retornado pelos Providers
da Versa AI (Internet, PDF, API, Supabase, Email, etc.),
armazenando os documentos encontrados, informações da fonte,
tempo de execução e o status da operação.

Autor: Raphael Wilson
"""

from __future__ import annotations

from dataclasses import dataclass, field

from app.domain.entities.document import Document


@dataclass(slots=True)
class SearchResult:

    success: bool

    source: str

    documents: list[Document] = field(default_factory=list)

    error: str = ""

    execution_time: float = 0.0

    @property
    def has_documents(self) -> bool:

        return len(self.documents) > 0

    @property
    def is_empty(self) -> bool:

        return len(self.documents) == 0

    @property
    def is_success(self) -> bool:

        return self.success

    @property
    def count(self) -> int:

        return len(self.documents)

    def add_document(self, document: Document) -> None:

        self.documents.append(document)

    def clear(self) -> None:

        self.documents.clear()

    def first(self) -> Document | None:

        if self.documents:
            return self.documents[0]

        return None

    def __iter__(self):

        return iter(self.documents)

    def __len__(self) -> int:

        return len(self.documents)