#https://leetcode-cn.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        valStr = str(x)
        return valStr == valStr[::-1]

