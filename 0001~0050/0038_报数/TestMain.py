import unittest
from countAndSay import Solution


class TestMain(unittest.TestCase):
    sln = Solution()

    def test_TestCase_1(self):
        self.assertEqual("1", self.sln.countAndSay(1))

    def test_TestCase_2(self):
        self.assertEqual("11", self.sln.countAndSay(2))

    def test_TestCase_3(self):
        self.assertEqual("21", self.sln.countAndSay(3))

    def test_TestCase_4(self):
        self.assertEqual("1211", self.sln.countAndSay(4))

    def test_TestCase_5(self):
        self.assertEqual("111221", self.sln.countAndSay(5))

    def test_TestCase_6(self):
        self.assertEqual("312211", self.sln.countAndSay(6))

    def test_TestCase_7(self):
        self.assertEqual("13112221", self.sln.countAndSay(7))


if __name__ == "__main__":
    unittest.main()
