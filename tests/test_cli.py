import subprocess
import unittest

import unilint


class TestUniLint(unittest.TestCase):
    def test_show_version(self) -> None:
        command = "unilint version"
        result = subprocess.run(command, capture_output=True, shell=True)
        assert result.stdout.decode("utf-8").strip() == unilint.__version__

    def test_run_linting_without_excluding_files(self) -> None:
        command = "unilint linting"
        result = subprocess.run(command, capture_output=True, shell=True)
        assert b"All done!" in result.stderr

    def test_run_linting_exclude_utils(self) -> None:
        command = "unilint linting -e src/unilint/utils.py"
        result = subprocess.run(command, capture_output=True, shell=True)
        assert b"All done!" in result.stderr

    def test_run_typing_check_src(self) -> None:
        command = "unilint typing -d src"
        result = subprocess.run(command, capture_output=True, shell=True)
        assert b"Success: no issues found" in result.stdout

    def test_run_typing_check_src_exclude_utils(self) -> None:
        command = "unilint typing -d src -e src/unilint/utils.py"
        result = subprocess.run(command, capture_output=True, shell=True)
        assert b"Success: no issues found" in result.stdout


if __name__ == "__main__":
    unittest.main()
