import time


class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []

        nums.sort()
        rtnLst = []
        numsLen = len(nums)
        for idx in range(0, numsLen - 3):
            rst = self.getThreeSum(nums[idx + 1:], target - nums[idx])
            for threeVals in rst:
                ans = [nums[idx]] + threeVals
                if ans not in rtnLst:
                    rtnLst.append([nums[idx]] + threeVals)
        return rtnLst

    @staticmethod
    def getThreeSum(subNums, target3):
        numLen = len(subNums)
        if numLen < 3:
            return []
        rtn = []
        for idxi in range(0, numLen - 2):
            idxj, idxk = idxi + 1, numLen - 1
            diff = target3 - subNums[idxi]
            while idxj < idxk:
                sumjk = subNums[idxj] + subNums[idxk]
                if sumjk > diff:  # should make it smaller
                    idxk -= 1
                elif sumjk < diff:  # should make it bigger
                    idxj += 1
                else:
                    rtn.append([subNums[idxi], subNums[idxj], subNums[idxk]])
                    idxj = Solution.getNextDiffPos(subNums, idxj, idxk + 1, 1)
                    if idxj == -1:
                        break
                    idxk = Solution.getNextDiffPos(subNums, idxk, idxj - 1, -1)
                    if idxk == -1:
                        break
        return rtn

    @staticmethod
    def getNextDiffPos(subNums, begin, end, step):
        nextDiffJ = begin
        for j in range(begin + step, end, step):
            if subNums[j] != subNums[begin]:
                nextDiffJ = j
                break
        if nextDiffJ != begin:
            return nextDiffJ
        return -1


sln = Solution()

begin = time.clock()
nums = [1, 0, -1]
expect = []
target = 10
print("TestCase1: ", sln.fourSum(nums, target) == expect, " ——take %.3f ms" % ((time.clock() - begin) * 1000))

nums = [1, 0, -1, 0, -2, 2]
target = 0
expect = [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
expect.sort()
begin = time.clock()
actual = sln.fourSum(nums, target)
end = time.clock()
actual.sort()
print("TestCase2: ", actual == expect, " ——take %.3f ms" % ((end - begin) * 1000))

nums = [-3, -2, -1, 0, 0, 1, 2, 3]
target = 0
expect = [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3],
          [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
expect.sort()
begin = time.clock()
actual = sln.fourSum(nums, target)
end = time.clock()
actual.sort()
print("TestCase3: ", actual == expect, " ——take %.3f ms" % ((end - begin) * 1000))
