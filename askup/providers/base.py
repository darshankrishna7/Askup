from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Sequence


@dataclass(slots=True)
class Source:
    url: str
    title: str | None = None


@dataclass(slots=True)
class Answer:
    content: str
    sources: Sequence[Source] | None = None


class Provider(ABC):
    """Abstract provider interface so we can plug more back‑ends later."""

    @abstractmethod
    async def ask(self, question: str) -> Answer:  # pragma: no cover
        raise NotImplementedError