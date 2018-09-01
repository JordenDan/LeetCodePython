import unittest
import isValid


class TestIsValid(unittest.TestCase):

    def test_TestCase1(self):
        sln = isValid.Solution()
        self.assertTrue(sln.isValid("()"))

    def test_TestCase2(self):
        sln = isValid.Solution()
        self.assertTrue(sln.isValid("()[]{}"))

    def test_TestCase3(self):
        sln = isValid.Solution()
        self.assertFalse(sln.isValid("(]"))

    def test_TestCase4(self):
        sln = isValid.Solution()
        self.assertFalse(sln.isValid("([)]"))

    def test_TestCase5(self):
        sln = isValid.Solution()
        self.assertTrue(sln.isValid("{[]}"))


if __name__ == "__main__":
    unittest.main()
