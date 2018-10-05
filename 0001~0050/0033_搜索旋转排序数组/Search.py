class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        sBegin, sEnd, = 0, len(nums) - 1
        while sBegin < sEnd:
            sMidd = (sBegin + sEnd) // 2
            if nums[sBegin] == target:
                return sBegin
            if nums[sEnd] == target:
                return sEnd
            if sBegin == sMidd:
                return -1
            if nums[sMidd] == target:
                return sMidd

            if nums[sMidd] < nums[sEnd]:
                if nums[sMidd] < target < nums[sEnd]:
                    sBegin = sMidd
                else:
                    sEnd = sMidd
            else:
                if nums[sBegin] < target < nums[sMidd]:
                    sEnd = sMidd
                else:
                    sBegin = sMidd
        if nums[sBegin] == target:
            return sBegin
        else:
            return -1