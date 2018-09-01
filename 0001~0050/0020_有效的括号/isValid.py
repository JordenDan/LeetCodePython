from collections import deque


class Solution:
    def isValid(self, s):
        dict = {'(': -1, ')': 1, '[': -2, ']': 2, '{': -3, '}': 3}
        validChar = "()[]{}"
        if not s:
            return True

        stack = deque()
        for ch in s:
            if ch not in validChar:
                return False
            val = dict[ch]
            if not stack:
                if val > 0:
                    return False
                else:
                    stack.append(val)
                    continue

            if stack[-1] + val == 0:
                stack.pop()
            elif val < 0:
                stack.append(val)
            else:
                return False

        return len(stack) == 0
