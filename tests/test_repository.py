import unittest

from scripts.validate_repo import (
    validate_required_files,
    validate_readme,
)


class TestRepository(unittest.TestCase):

    def test_required_files_exist(self):
        self.assertEqual(validate_required_files(), [])

    def test_readme_contains_required_content(self):
        self.assertEqual(validate_readme(), [])


if __name__ == "__main__":
    unittest.main()
