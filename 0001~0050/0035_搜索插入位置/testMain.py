import unittest
from searchInsert import Solution


class TestClass(unittest.TestCase):
    sln = Solution()

    def test_TestCase1(self):
        input = []
        target = 0
        self.assertEqual(self.sln.searchInsert(input, target), 0)

    def test_TestCase2(self):
        input = [1, 3, 5, 6]
        target = 5
        self.assertEqual(self.sln.searchInsert(input, target), 2)

    def test_TestCase3(self):
        input = [1, 3, 5, 6]
        target = 2
        self.assertEqual(self.sln.searchInsert(input, target), 1)

    def test_TestCase4(self):
        input = [1, 3, 5, 6]
        target = 7
        self.assertEqual(self.sln.searchInsert(input, target), 4)

    def test_TestCase5(self):
        input = [1, 3, 5, 6]
        target = 0
        self.assertEqual(self.sln.searchInsert(input, target), 0)

    def test_TestCase6(self):
        input = list(range(0, 61803)) + list(range(61804, 100000))
        target = 61803
        self.assertEqual(self.sln.searchInsert(input, target), 61803)

    def test_TestCase7(self):
        input = [1]
        target = 1
        self.assertEqual(self.sln.searchInsert(input, target), 0)

if __name__ == '__main__':
    unittest.main()
