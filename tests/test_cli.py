import subprocess
import unittest
from typing import Tuple

import unilint

STDOUT, STDERR, STATUS_CODE = bytes, bytes, int


def run(command) -> Tuple[STDOUT, STDERR, STATUS_CODE]:
    """Run tests."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    exit_code = process.wait()
    return stdout, stderr, exit_code


class TestMlopsLint(unittest.TestCase):
    def test_show_version(self) -> None:
        command = "unilint version"
        stdout, _, code = run(command)
        assert stdout.decode("utf-8").strip() == unilint.__version__
        assert code == 0

    def test_run_linting_without_excluding_files(self) -> None:
        command = "unilint linting -e tests"
        stdout, _, code = run(command)
        print(stdout)
        assert code == 0
        assert b"All done!" in stdout

    def test_run_linting_exclude_utils(self) -> None:
        command = "unilint linting -e src"
        _, _, code = run(command)
        assert code == 1

    def test_run_linting_fails(self) -> None:
        command = "unilint linting"
        _, _, code = run(command)
        assert code == 1

    def test_run_typing_check_src(self) -> None:
        command = "unilint typing -d src"
        stdout, _, code = run(command)
        assert code == 0
        assert b"Success: no issues found" in stdout

    def test_run_typing_check_src_exclude_utils(self) -> None:
        command = "unilint typing -d src -e src/unilint/utils.py"
        stdout, _, code = run(command)
        assert code == 0
        assert b"Success: no issues found" in stdout

    def test_run_typing_check_fixtures_fail(self) -> None:
        command = "unilint typing -d tests/testcase -e src"
        stdout, _, code = run(command)
        assert code == 1


if __name__ == "__main__":
    unittest.main()
