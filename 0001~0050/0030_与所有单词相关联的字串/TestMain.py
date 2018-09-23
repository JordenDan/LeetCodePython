import unittest

from findSubstring import Solution


class TestMain(unittest.TestCase):
    sln = Solution()

    def test_TestCase1(self):
        str = "wordgoodstudentgoodword"
        words = ["g", "o", "o"]
        rtn = self.sln.findSubstring(str, words)
        acutal = set(rtn)
        expect = set(list([4, 15]))
        self.assertEqual(acutal, expect)

    def test_TestCase2(self):
        str = "wordgoodstudentgoodword"
        words = ["word", "good"]
        rtn = self.sln.findSubstring(str, words)
        acutal = set(rtn)
        expect = set(list([0, 15]))
        self.assertEqual(acutal, expect)

    def test_TestCase3(self):
        str = "wordgoodstudentgoodword"
        words = ["word", "goodstudent"]
        rtn = self.sln.findSubstring(str, words)
        acutal = set(rtn)
        expect = set(list([]))
        self.assertEqual(acutal, expect)

    def test_TestCase4(self):
        str = "barfoothefoobarman"
        words = ["foo", "bar"]
        rtn = self.sln.findSubstring(str, words)
        acutal = set(rtn)
        expect = set(list([0, 9]))
        self.assertEqual(acutal, expect)

    def test_TestCase5(self):
        str = "barfo"
        words = ["foo", "bar"]
        rtn = self.sln.findSubstring(str, words)
        acutal = set(rtn)
        expect = set(list([]))
        self.assertEqual(acutal, expect)


if __name__ == "__main__":
    unittest.main()
