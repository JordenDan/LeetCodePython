import time


class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return None
        rtn = nums[0] + nums[1] + nums[2]
        minDiff = abs(rtn - target)
        nums.sort()
        numLen = len(nums)

        for idxi in range(numLen - 1):
            idxj, idxk = idxi + 1, numLen - 1
            tryVal = nums[idxj] + nums[idxk]
            while idxj < idxk:
                tmp = nums[idxi] + tryVal
                if tmp == target:
                    return target

                trySumL = nums[idxj + 1] + nums[idxk]
                trySumR = nums[idxj] + nums[idxk - 1]
                if tmp > target:  # should make sum smaller
                    diff = tmp - target
                    if trySumL < trySumR:
                        idxj += 1
                        tryVal = trySumL
                    else:  # if equal should go in this branch
                        idxk -= 1
                        tryVal = trySumR
                else:  # should make sum bigger
                    diff = target - tmp
                    if trySumL < trySumR:
                        idxk -= 1
                        tryVal = trySumR
                    else:
                        idxj += 1
                        tryVal = trySumL

                if diff < minDiff:
                    minDiff = diff
                    rtn = tmp
        return rtn


sln = Solution()

nums = [-1, 2, 1, -4]
target = 1
timeBegin = time.clock()
print("TestCase1:", sln.threeSumClosest(nums, target) == 2, ", task: %.3fms" % ((time.clock() - timeBegin) * 1000))

nums = [1, 2, 4, 8, 16, 32, 64, 128]
target = 82
timeBegin = time.clock()
print("TestCase2:", sln.threeSumClosest(nums, target) == 82, ", task: %.3fms" % ((time.clock() - timeBegin) * 1000))

nums = [-1, 2, 1, -4, 10, 4, 8, -7, 2, 4, 22, 13]
target = 5
timeBegin = time.clock()
print("TestCase3:", sln.threeSumClosest(nums, target) == 5, ", task: %.3fms" % ((time.clock() - timeBegin) * 1000))

nums = [13, 2, 0, -14, -20, 19, 8, -5, -13, -3, 20, 15, 20, 5, 13, 14, -17, -7, 12, -6, 0, 20, -19, -1, -15, -2, 8, -2,
        -9, 13, 0, -3, -18, -9, -9, -19, 17, -14, -19, -4, -16, 2, 0, 9, 5, -7, -4, 20, 18, 9, 0, 12, -1, 10, -17, -11,
        16, -13, -14, -3, 0, 2, -18, 2, 8, 20, -15, 3, -13, -12, -2, -19, 11, 11, -10, 1, 1, -10, -2, 12, 0, 17, -19,
        -7, 8, -19, -17, 5, -5, -10, 8, 0, -12, 4, 19, 2, 0, 12, 14, -9, 15, 7, 0, -16, -5, 16, -12, 0, 2, -16, 14, 18,
        12, 13, 5, 0, 5, 6]
target = -59
timeBegin = time.clock()
print("TestCase4:", sln.threeSumClosest(nums, target) == -58, ", task: %.3fms" % ((time.clock() - timeBegin) * 1000))
