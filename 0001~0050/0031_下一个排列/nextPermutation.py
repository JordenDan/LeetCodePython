class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        if numsLen < 2:
            return

        for idx in range(numsLen - 2, -1, -1):
            if nums[idx] >= nums[idx + 1]:
                continue
            nextBiggerIdx = -1
            for idxSub in range(numsLen - 1, idx, -1):
                if nums[idxSub] > nums[idx]:
                    nextBiggerIdx = idxSub
                    break
            nums[idx], nums[nextBiggerIdx] = nums[nextBiggerIdx], nums[idx]
            pLhs, pRhs = idx + 1, numsLen - 1
            while pLhs < pRhs:
                nums[pLhs], nums[pRhs] = nums[pRhs], nums[pLhs]
                pLhs, pRhs = pLhs + 1, pRhs - 1
            return
        nums.sort()
        return
