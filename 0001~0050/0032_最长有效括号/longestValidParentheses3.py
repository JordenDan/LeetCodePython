class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)

        if sLen <= 1:
            return 0

        maxLen = []
        if s[0:2] == "()":
            maxLen = [0, 2]
        else:
            maxLen = [0, 0]

        for idx in range(2, sLen):
            if "(" == s[idx]:
                maxLen.append(0)
                continue
            if s[idx - 1] == "(":
                maxLen.append(maxLen[idx - 2] + 2)
                continue
            idxPre = idx - 1 - maxLen[idx - 1]
            if idxPre < 0 or s[idxPre] != "(":
                maxLen.append(0)
                continue
            if idxPre == 0:
                maxLen.append(maxLen[idx-1] + 2)
                continue
            maxLen.append(maxLen[idx-1] + maxLen[idxPre - 1] + 2)

        maxLen.sort()
        return maxLen[-1]
