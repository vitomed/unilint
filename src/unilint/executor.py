import subprocess

import click

from unilint.exceptions import (
    CodeStyleException,
)


class CodeStyleExecutor:

    """Lint executor class."""

    @classmethod
    def run(cls, command: str) -> None:
        """Run linting process."""
        click.echo(command)
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        stdout, stderr = process.communicate()
        exit_code = process.wait()
        click.echo(stdout)
        click.echo(stderr)
        if exit_code != 0:
            raise CodeStyleException
