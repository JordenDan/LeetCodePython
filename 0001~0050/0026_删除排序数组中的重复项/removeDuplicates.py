#https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        idxi = 0
        idxj = 1
        while idxj < len(nums):
            if nums[idxj] == nums[idxi]:
                nums.__delitem__(idxj)
            else:
                idxi = idxj 
                idxj = idxi + 1
       
        return len(nums)
