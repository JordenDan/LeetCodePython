class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        nums.sort()

        firstPos = 1
        for idx in range(len(nums)):
            if nums[idx] <= 0:
                continue
            if nums[idx] > firstPos:
                return firstPos
            else:
                firstPos = nums[idx] + 1
        return firstPos

