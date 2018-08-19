#https://leetcode-cn.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = -1
        for idx in range(len(nums)):
            if nums[idx] != val:
                index += 1
                nums[index] = nums[idx]
        return index + 1
