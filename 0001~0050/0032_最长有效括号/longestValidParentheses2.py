class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        sLen = len(s)

        stack = [-1]
        for idx in range(sLen):
            if "(" == s[idx]:
                stack.append(idx)
                continue
            # if ")"
            stack.pop()
            if len(stack) == 0:
                stack.append(idx)
            else:
                maxLen = max(maxLen, idx - stack[-1])
        return maxLen
