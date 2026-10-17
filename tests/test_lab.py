import unittest

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


if __name__ == "__main__":
    unittest.main()
