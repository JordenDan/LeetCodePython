#https://leetcode-cn.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        maxLen = 0
        maxStr = ""
        for i in range(len(s)):
            if i + maxLen > len(s):
                break
            for j in range(i + maxLen, len(s) + 1):
                subStr = s[i:j]
                revStr = subStr[::-1]
                if len(subStr) >= maxLen and subStr == revStr:
                    maxLen = len(subStr)
                    maxStr = subStr
        return maxStr
