import unittest
from searchRange import Solution


class TestClass(unittest.TestCase):
    sln = Solution()

    def test_TestCase1(self):
        input = []
        target = 0
        self.assertEqual(self.sln.searchRange(input, target), [-1, -1])

    def test_TestCase2(self):
        input = [2, 2]
        target = 2
        self.assertEqual(self.sln.searchRange(input, target), [0, 1])

    def test_TestCase3(self):
        input = [5, 7, 7, 8, 8, 10]
        target = 8
        self.assertEqual(self.sln.searchRange(input, target), [3, 4])

    def test_TestCase4(self):
        input = [5, 7, 7, 8, 8, 10]
        target = 6
        self.assertEqual(self.sln.searchRange(input, target), [-1, -1])

    def test_TestCase5(self):
        input = [5, 7, 7, 8, 8, 10]
        target = 7
        self.assertEqual(self.sln.searchRange(input, target), [1, 2])

    def test_TestCase6(self):
        input = list(range(10000)) + [10000] * 3129 + list(range(20000, 50000))
        target = 10000
        self.assertEqual(self.sln.searchRange(input, target), [10000, 13128])


if __name__ == '__main__':
    unittest.main()
