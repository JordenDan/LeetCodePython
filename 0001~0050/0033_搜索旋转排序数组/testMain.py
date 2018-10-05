import unittest
from Search import Solution


class TestClass(unittest.TestCase):
    sln = Solution()

    def test_TestCase1(self):
        input = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.sln.search(input, target), 4)

    def test_TestCase2(self):
        input = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.sln.search(input, target), -1)

    def test_TestCase3(self):
        input = [5, 6, 7, 0, 1, 2, 3, 4]
        target = 3
        self.assertEqual(self.sln.search(input, target), 6)

    def test_TestCase4(self):
        input = []
        target = 3
        self.assertEqual(self.sln.search(input, target), -1)

    def test_TestCase5(self):
        input = [1, 3]
        target = 3
        self.assertEqual(self.sln.search(input, target), 1)

    def test_TestCase6(self):
        input = list(range(3000, 10000)) + list(range(0, 3000))
        target = 1467
        self.assertEqual(self.sln.search(input, target), 8467)

    def test_TestCase7(self):
        input = [0, 1, 2, 3, 4, 5, 6]
        target = 5
        self.assertEqual(self.sln.search(input, target), 5)


if __name__ == "__main__":
    unittest.main()
