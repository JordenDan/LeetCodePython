class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums or target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        sBegin, sEnd = 0, len(nums) - 1
        while sBegin < sEnd:
            sMidd = (sBegin + sEnd) // 2
            if nums[sBegin] == target:
                return sBegin
            if nums[sEnd] == target:
                return sEnd
            if sBegin == sMidd:
                return sBegin + 1
            if nums[sMidd] == target:
                return sMidd

            if target > nums[sMidd]:
                sBegin = sMidd
            else:
                sEnd = sMidd
        if nums[sBegin] == target:
            return sBegin
        else:
            return sBegin + 1
