import traceback
from datetime import datetime
from typing import List

import click

import unilint
from unilint.exceptions import (
    CodeStyleException,
)
from unilint.executor import (
    CodeStyleExecutor,
)
from unilint.utils import (
    get_linting_cmd,
    get_typing_cmd,
)


@click.group()
def cli() -> None:  # noqa: D103
    pass


@click.command(help="A run of formatters and linters.")
@click.option("--exclude", "-e", default=[], multiple=True, help="Exclude dir/file by path.")
def linting(exclude: List[str]) -> None:
    """Code style and formatting."""
    click.echo(f"linting: {datetime.now()}")
    try:
        command = get_linting_cmd(exclude)
        CodeStyleExecutor.run(";".join(command))

    except CodeStyleException:
        click.echo(traceback.format_exc())
        exit(1)
    except Exception:
        click.echo(traceback.format_exc())
        exit(1)


@click.command()  # noqa: C901
@click.option("--dirs", "-d", required=True, multiple=True, help="Dir/file path.")  # noqa: C901
@click.option("--exclude", "-e", default=[], multiple=True, help="Exclude dir/file by path.")
def typing(dirs: List[str], exclude: List[str]) -> None:
    """Check types using mypy."""
    click.echo(f"typing: {datetime.now()}")
    try:
        command = get_typing_cmd(dirs, exclude)
        click.echo(command)
        CodeStyleExecutor.run(command)

    except CodeStyleException:
        click.echo(traceback.format_exc())
        exit(1)
    except Exception:
        print(traceback.format_exc())
        exit(1)


@click.command(help="Print version info.")  # noqa: C901
def version() -> None:
    """Package version."""
    click.echo(unilint.__version__)


cli.add_command(linting)
cli.add_command(typing)
cli.add_command(version)

if __name__ == "__main__":
    cli()
