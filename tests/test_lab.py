import unittest
import json
from pathlib import Path

from lab import ROWS, group_mean, mean, pearson_correlation


class LabTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([2, 4, 6]), 4)

    def test_group_means_cover_groups(self):
        self.assertEqual(set(group_mean(ROWS, "group", "score")), {"A", "B"})

    def test_perfect_positive_correlation(self):
        self.assertAlmostEqual(pearson_correlation([1, 2, 3], [2, 4, 6]), 1)

    def test_invalid_mean_raises(self):
        with self.assertRaises(ValueError):
            mean([])

    def test_learning_notebooks_are_valid_and_present(self):
        notebooks = sorted(Path("notebooks").glob("*.ipynb"))
        self.assertGreaterEqual(len(notebooks), 2)
        for path in notebooks:
            content = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(content["nbformat"], 4)
            self.assertTrue(content["cells"])


if __name__ == "__main__":
    unittest.main()
