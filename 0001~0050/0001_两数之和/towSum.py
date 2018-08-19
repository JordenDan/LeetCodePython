# https://leetcode-cn.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtn = []
        for idxA in range(len(nums)):
            for idxB in range(idxA + 1, len(nums)):
                if (nums[idxA] + nums[idxB] == target):
                    rtn.append(idxA)
                    rtn.append(idxB)
                    return rtn
