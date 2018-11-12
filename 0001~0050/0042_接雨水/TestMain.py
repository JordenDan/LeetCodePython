import unittest
from trap import Solution


class TestMain(unittest.TestCase):
    sln = Solution()

    def test_TestCase1(self):
        self.assertEqual(self.sln.trap([10]), 0)

    def test_TestCase2(self):
        self.assertEqual(self.sln.trap([2, 0, 2]), 2)

    def test_TestCase3(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(self.sln.trap(height), 6)

    def test_TestCase4(self):
        height = [7, 26, 27, 4, 0, 3, 10, 26, 13, 10, 29, 10, 25, 16, 22, 27, 22, 3, 22, 14, 6, 28, 27, 14, 24, 21];
        self.assertEqual(self.sln.trap(height), 246)


if __name__ == "__main__":
    unittest.main()
