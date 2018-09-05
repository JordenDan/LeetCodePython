import unittest
from generateParenthesis import Solution


class TestIsValid(unittest.TestCase):

    def test_TestCase1(self):
        sln = Solution()
        expect = ["()"]
        actual = sln.generateParenthesis(1)
        expect.sort()
        actual.sort()
        self.assertEqual(actual, expect)

    def test_TestCase2(self):
        sln = Solution()
        expect = ["()()", "(())"]
        actual = sln.generateParenthesis(2)
        expect.sort()
        actual.sort()
        self.assertEqual(actual, expect)

    def test_TestCase3(self):
        sln = Solution()
        expect = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        actual = sln.generateParenthesis(3)
        expect.sort()
        actual.sort()
        self.assertEqual(actual, expect)

    def test_TestCase4(self):
        sln = Solution()
        expect = [
            "((()))()", "(()())()", "(())()()", "()()()()",
            "()((()))", "()(()())", "()(())()", "()()(())", "(())(())",
            "(((())))", "((()()))", "((())())", "(()(()))", "(()()())"]
        actual = sln.generateParenthesis(4)
        expect.sort()
        actual.sort()
        self.assertEqual(actual, expect)

if __name__ == "__main__":
    unittest.main()
