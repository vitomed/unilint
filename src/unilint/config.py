autoflake_options = [
    "--in-place",
    "--recursive",
    "--remove-all-unused-imports",
    "--remove-unused-variables",
]

isort_options = [
    "--trailing-comma",
    "--line-length",
    "40",
    "--remove-redundant-aliases",
    "--verbose",
    "--use-parentheses",
    "--skip",
    ".env",
    "--skip",
    ".venv",
    "--skip",
    ".git",
    "--skip",
    ".mypy_cache",
    "--skip",
    ".pytest_cache",
    "--skip",
    "__pycache__",
    "--skip",
    "env",
    "--skip",
    "venv",
]

docformatter_options = [
    "--recursive",
    "--in-place",
    "--blank",
]

black_options = ["--fast", "--line-length", "100"]

pydocstyle_options = [
    "--count",
    "--ignore",
    "D100,D104,D107,D202,D211,D213,D400,D401,D407,D415",
]

flake8_options = [
    "--count",
    "--eradicate-aggressive",
    "--max-complexity 4",
    "--max-line-length 100",
    "--statistics",
]

mypy_options = [
    "--disallow-untyped-defs",
    "--ignore-missing-imports",
    "--warn-unused-configs",
    "--warn-unused-ignores",
]
