import unittest
from firstMissingPositive import Solution


class TestMain(unittest.TestCase):
    sln = Solution()

    def test_TestCase1(self):
        self.assertEqual(self.sln.firstMissingPositive([1, 2, 0]), 3)

    def test_TestCase2(self):
        self.assertEqual(self.sln.firstMissingPositive([3, 4, -1, 1]), 2)

    def test_TestCase3(self):
        self.assertEqual(self.sln.firstMissingPositive([7, 8, 9, 11, 12]), 1)


if __name__ == "__main__":
    unittest.main()
