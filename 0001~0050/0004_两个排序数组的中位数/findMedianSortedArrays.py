#https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        middLst = []
        lenNum = len(nums1)
        if lenNum % 2 == 0:
            return (nums1[lenNum // 2 - 1] + nums1[lenNum // 2]) / 2
        else:
            return nums1[lenNum // 2]
