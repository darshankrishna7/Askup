from __future__ import annotations
from rich.console import Console
from rich.table import Table
from typing import Sequence, Optional
from ..providers.base import Answer, Source


_console = Console()


def print_answer(question: str, answer: Answer) -> None:
    _console.rule(f":mag:  {question}")
    _console.print(answer.content)

    if answer.sources:
        tbl = Table(show_header=True, header_style="bold cyan")
        tbl.add_column("#")
        tbl.add_column("Source")
        for i, src in enumerate(answer.sources, 1):
            label = src.title or src.url
            tbl.add_row(str(i), f"[link={src.url}]{label}[/]")
        _console.print(tbl)