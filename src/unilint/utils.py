from typing import List, Optional

from unilint.config import (
    autoflake_options,
    black_options,
    docformatter_options,
    flake8_options,
    isort_options,
    mypy_options,
    pydocstyle_options,
)


def exclude_dir(flag: str, exclude: List[str]) -> str:
    """Exclude list of dirs/files."""
    if len(exclude) == 0:
        return ""
    return " ".join([f"--{flag} {e} " for e in exclude])


def command_builder(pkg_name: str, dest: str, options: str, extra: Optional[str] = None) -> str:
    """Create cmd command."""
    if extra is None:
        extra = ""
    if dest is None:
        dest = "."
    command = f"{pkg_name} {dest} {options} {extra}"
    return command


def get_linting_cmd(exclude: List[str]) -> List[str]:
    """Generate linting cmd."""
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

    return command


def get_typing_cmd(dirs: List[str], exclude: List[str]) -> str:
    """Generate typing cmd."""
    command = command_builder(
        pkg_name="mypy",
        dest=" ".join(dirs),
        options=" ".join(mypy_options),
        extra=exclude_dir(flag="exclude", exclude=exclude),
    )
    return command
