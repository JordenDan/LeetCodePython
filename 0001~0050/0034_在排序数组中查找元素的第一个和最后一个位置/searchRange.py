class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sPos = self.searchVal(nums, target)
        if sPos == -1:
            return [-1, -1]
        else:
            return [self.searchRangeEq(nums, sPos, -1), self.searchRangeEq(nums, sPos, 1)]

    def searchRangeEq(self, nums, idx, dir):
        numLen = len(nums)
        if dir == 1:
            while idx < numLen - 1 and nums[idx + dir] == nums[idx]:
                idx += dir
        else:
            while idx > 1 and nums[idx + dir] == nums[idx]:
                idx += dir
        return idx

    def searchVal(self, nums, target):
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