from __future__ import annotations
import asyncio
from typing import List
from openai import AsyncOpenAI, BadRequestError
from web_ai_cli.config import get_settings
from web_ai_cli.providers.base import Provider, Answer, Source


class OpenAISearchProvider(Provider):
    """Wrapper around GPT‑4o search‑preview (or any search‑enabled model)."""

    def __init__(self):
        cfg = get_settings()
        if not cfg.is_valid:
            raise ValueError("OPENAI_API_KEY not set. Check your .env or env vars.")
        self._client = AsyncOpenAI(api_key=cfg.api_key)
        self._model = cfg.model
        self._context_size = cfg.context_size

    async def ask(self, question: str) -> Answer:
        try:
            resp = await self._client.chat.completions.create(
                model=self._model,
                messages=[{"role": "user", "content": question}],
                web_search_options={"search_context_size": self._context_size},
                stream=False,
            )
        except BadRequestError as e:
            raise RuntimeError(f"OpenAI request failed: {e}") from e

        msg = resp.choices[0].message
        # Source extraction: assumes OpenAI returns "citations" metadata soon; placeholder for now
        sources: List[Source] = []
        if msg.tool_calls:  # speculative future field
            for call in msg.tool_calls:
                if call.type == "WEB_CITATION":
                    sources.append(Source(url=call.url, title=call.title))

        return Answer(content=msg.content.strip(), sources=sources or None)