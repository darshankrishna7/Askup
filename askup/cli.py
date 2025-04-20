from __future__ import annotations
import asyncio
from typing import Optional
import typer
from rich.console import Console
from askup.providers.openai_search import OpenAISearchProvider
from askup.utils.display import print_answer
from . import __version__

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="Ask the web from your terminal 🧠",
    pretty_exceptions_enable=True,
    pretty_exceptions_show_locals=False,
    context_settings={"help_option_names": ["-h", "--help"]},
    )
console = Console()
provider = OpenAISearchProvider()


app.version = __version__

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    q: Optional[str] = typer.Option(
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
    """webai – Ask the web from your terminal 🧠"""

    # If no question provided, just show help and exit.
    if q is None:
        console.print(ctx.get_help())
        raise typer.Exit()

    # If user supplied a different context size, patch provider for this call.
    if context:
        provider.context_size = context  # type: ignore[attr-defined]

    answer = asyncio.run(provider.ask(q))
    print_answer(q, answer)


if __name__ == "__main__":  # pragma: no cover
    app()