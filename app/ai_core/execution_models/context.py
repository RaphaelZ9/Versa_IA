from dataclasses import dataclass, field
from typing import Any

from app.domain.entities.conversation.conversation import Conversation
from app.domain.entities.search_result import SearchResult


@dataclass
class Context:

    conversation: Conversation = field(default_factory=Conversation)

    search_result: SearchResult | None = None

    user: Any = None

    documents: list[Any] = field(default_factory=list)

    tools: list[Any] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def has_search(self) -> bool:

        return self.search_result is not None

    @property
    def has_documents(self) -> bool:

        return len(self.documents) > 0

    @property
    def has_tools(self) -> bool:

        return len(self.tools) > 0

    @property
    def has_metadata(self) -> bool:

        return len(self.metadata) > 0

    def add_document(self, document: Any):

        self.documents.append(document)

    def add_tool(self, tool: Any):

        self.tools.append(tool)

    def add_metadata(self, key: str, value: Any):

        self.metadata[key] = value