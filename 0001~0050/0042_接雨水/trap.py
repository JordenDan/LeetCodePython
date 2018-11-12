class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        hLen = len(height)
        if hLen <= 1:
            return 0

        addedV = [0 for _ in range(hLen)]
        left, right = 0, 1
        while right < hLen:
            if height[right] < height[left]:
                right += 1
            else:
                self.addVLeft(left, right, height, addedV)
                left, right = right, right + 1

        left, right = hLen - 2, hLen - 1
        while left >= 0:
            if height[left] < height[right]:
                left -= 1
            else:
                self.addVRight(left, right, height, addedV)
                left, right = left - 1, left

        return sum(addedV)

    def addVLeft(self, left, right, height, addedV):
        for idx in range(left, right):
            addedV[idx] = max(height[left] - height[idx], addedV[idx])

    def addVRight(self, left, right, height, addedV):
        for idx in range(right, left, -1):
            addedV[idx] = max(height[right] - height[idx], addedV[idx])