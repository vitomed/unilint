from typing import List, Optional


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
