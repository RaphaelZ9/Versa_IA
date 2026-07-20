from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:

    title: str

    content: str

    source: str

    url: str = ""

    score: float = 0.0

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def has_url(self) -> bool:

        return bool(self.url)

    @property
    def has_metadata(self) -> bool:

        return bool(self.metadata)

    def add_metadata(self, key: str, value: Any):

        self.metadata[key] = value

    def get_metadata(self, key: str, default=None):

        return self.metadata.get(key, default)

    def __str__(self):

        return self.content