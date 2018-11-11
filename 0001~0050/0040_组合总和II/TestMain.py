import unittest
from combinationSum2 import Solution
from functools import cmp_to_key


def comp(lst1, lst2):
    str1 = ",".join([str(i) for i in lst1])
    str2 = ",".join([str(i) for i in lst2])
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0


class TestMain(unittest.TestCase):
    sln = Solution()

    def sortedLst(self, lst):
        for idx in range(len(lst)):
            lst[idx].sort()
        return sorted(lst, key=cmp_to_key(comp))

    def test_TestCase1(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expect = self.sortedLst([[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]])
        ans = self.sortedLst(self.sln.combinationSum2(candidates, target))
        self.assertEqual(expect, ans)

    def test_TestCase2(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expect = self.sortedLst([[1, 2, 2], [5]])
        ans = self.sortedLst(self.sln.combinationSum2(candidates, target))
        self.assertEqual(expect, ans)


if __name__ == "__main__":
    unittest.main()
