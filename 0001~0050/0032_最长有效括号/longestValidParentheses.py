class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        parenMap = {}
        maxLen = 0
        for idx in range(0, len(s)):
            if "(" == s[idx]:
                for key in parenMap.keys():
                    parenMap[key][0], parenMap[key][1] = parenMap[key][0] + 1, parenMap[key][1] + 1
                parenMap[idx] = [1, 1]
            elif ")" == s[idx]:
                for key in list(parenMap.keys()):
                    if parenMap[key][1] > 0:
                        parenMap[key][0], parenMap[key][1] = parenMap[key][0] + 1, parenMap[key][1] - 1
                        if parenMap[key][1] == 0 and parenMap[key][0] > maxLen:
                            maxLen = parenMap[key][0]
                    else:
                        del parenMap[key]
            else:
                return 0

        return maxLen
