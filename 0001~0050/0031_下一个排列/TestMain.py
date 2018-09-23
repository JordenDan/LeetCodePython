import unittest
from nextPermutation import Solution


class TestClass(unittest.TestCase):
    sln = Solution()

    def test_TestCase1(self):
        ioput = [1, 2, 3]
        self.sln.nextPermutation(ioput)
        expect = [1, 3, 2]
        self.assertEqual(ioput, expect)

    def test_TestCase2(self):
        ioput = [3, 2, 1]
        self.sln.nextPermutation(ioput)
        expect = [1, 2, 3]
        self.assertEqual(ioput, expect)

    def test_TestCase3(self):
        ioput = [1, 1, 5]
        self.sln.nextPermutation(ioput)
        expect = [1, 5, 1]
        self.assertEqual(ioput, expect)

    def test_TestCase3(self):
        ioput = [1, 2, 3, 5, 4, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.sln.nextPermutation(ioput)
        expect = [1, 2, 3, 5, 5, 1, 2, 3, 4, 4, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(ioput, expect)

    def test_TestCase4(self):
        ioput = [1, 2, 3, 5, 11, 13, 12, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.sln.nextPermutation(ioput)
        expect = [1, 2, 3, 5, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 12, 13]
        self.assertEqual(ioput, expect)

if __name__ == "__main__":
    unittest.main()
