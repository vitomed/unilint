import subprocess
import traceback
from datetime import datetime
from typing import List

import click

import unilint
from unilint.config import (
    autoflake_options,
    black_options,
    docformatter_options,
    flake8_options,
    isort_options,
    mypy_options,
    pydocstyle_options,
)
from unilint.utils import (
    command_builder,
    exclude_dir,
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
        command = [
            command_builder(
                pkg_name="autoflake",
                dest=".",
                options=" ".join(autoflake_options),
                extra=exclude_dir(flag="exclude", exclude=exclude),
            ),
            command_builder(
                pkg_name="isort",
                dest=".",
                options=" ".join(isort_options),
                extra=exclude_dir(flag="skip", exclude=exclude),
            ),
            command_builder(
                pkg_name="docformatter",
                dest=".",
                options=" ".join(docformatter_options),
                extra=exclude_dir(flag="exclude", exclude=exclude),
            ),
            command_builder(
                pkg_name="black",
                dest=".",
                options=" ".join(black_options),
                extra=exclude_dir(flag="exclude", exclude=exclude),
            ),
            command_builder(
                pkg_name="pydocstyle",
                dest=".",
                options=" ".join(pydocstyle_options),
            ),
            command_builder(
                pkg_name="flake8",
                dest=".",
                options=" ".join(flake8_options),
                extra=exclude_dir(flag="exclude", exclude=exclude),
            ),
        ]
        click.echo("\n".join(command))
        subprocess.run(";".join(command), shell=True)
    except Exception:
        print(traceback.format_exc())
        exit(1)


@click.command()  # noqa: C901
@click.option("--dir", "-d", required=True, multiple=True, help="Dir/file path.")  # noqa: C901
@click.option("--exclude", "-e", default=[], multiple=True, help="Exclude dir/file by path.")
def typing(dir: List[str], exclude: List[str]) -> None:
    """Check types using mypy."""
    click.echo(f"typing: {datetime.now()}")
    try:
        command = command_builder(
            pkg_name="mypy",
            dest=" ".join(dir),
            options=" ".join(mypy_options),
            extra=exclude_dir(flag="exclude", exclude=exclude),
        )
        click.echo(command)
        subprocess.run(command, shell=True)
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
