"""Centralised config loading (env, dotenv, defaults)."""

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(".env"), override=False)


@dataclass(slots=True)
class Settings:
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    model: str = os.getenv("WEB_AI_MODEL", "gpt-4o-search-preview")
    context_size: str = os.getenv("WEB_AI_SEARCH_CONTEXT_SIZE", "medium")

    @property
    def is_valid(self) -> bool:  # quick sanity check
        return bool(self.api_key)


def get_settings() -> Settings:  # convenience accessor
    return Settings()