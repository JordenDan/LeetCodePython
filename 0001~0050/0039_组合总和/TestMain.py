import unittest
from combinationSum import Solution
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
        candidates = [2, 3, 6, 7]
        target = 7
        expect = self.sortedLst([[7], [2, 2, 3]])
        ans = self.sortedLst(self.sln.combinationSum(candidates, target))
        self.assertEqual(expect, ans)

    def test_TestCase2(self):
        candidates = [2, 3, 5]
        target = 8
        expect = self.sortedLst([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
        ans = self.sortedLst(self.sln.combinationSum(candidates, target))
        self.assertEqual(expect, ans)

    def test_TestCase3(self):
        candidates = [2, 3]
        target = 8
        expect = self.sortedLst([[2, 3, 3], [2, 2, 2, 2]])
        ans = self.sortedLst(self.sln.combinationSum(candidates, target))
        self.assertEqual(expect, ans)


if __name__ == "__main__":
    unittest.main()
