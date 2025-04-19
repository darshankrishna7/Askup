from __future__ import annotations
import asyncio
import typer
from typing import Annotated, List, Optional
from rich.console import Console
from web_ai_cli.providers.openai_search import OpenAISearchProvider
from web_ai_cli.utils.display import print_answer

app = typer.Typer(add_completion=False)
_console = Console()
_provider = OpenAISearchProvider()


@app.callback()
def main(
    question: Optional[str] = typer.Option(
        None,
        "-q",
        "--question",
        help="Ask a web-searchable question",
    ),
    context: Optional[str] = typer.Option(
        None,
        "--context-size",
        "-c",
        help="Search context size: small | medium | large (defaults to env config)",
    ),
):
    """webai: ask the web from your terminal 🧠"""
    if not question:
        _console.print("[bold red]No question given. Use -q or --question.[/]")
        raise typer.Exit(1)

    if context:
        _provider._context_size = context  # type: ignore

    answer = asyncio.run(_provider.ask(question))
    print_answer(question, answer)


if __name__ == "__main__":  # pragma: no cover
    app()
