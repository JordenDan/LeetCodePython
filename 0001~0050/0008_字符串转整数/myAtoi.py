#https://leetcode-cn.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        for idx, char in enumerate(str):
            if str[idx] == " ":
                continue
            if str[idx] == "-":
                if len(str) == 1:
                    return 0
                return self.cvt(str[idx+1:], -1)
            if str[idx] == "+":
                if len(str) == 1:
                    return 0
                return self.cvt(str[idx+1:], 1)
            if not str[idx] in "0123456789":
                return 0
            return self.cvt(str[idx:], 1)
        return 0

    def cvt(self, str, positive):
        if not str[0] in "0123456789":
            return 0

        idxEnd = -1
        for idx, char in enumerate(str):
            if char in "0123456789":
                continue
            idxEnd = idx
            break

        if idxEnd == -1:
            longVal = int(str[:])
        else:
            longVal = int(str[:idxEnd])

        if positive == 1 and longVal > CstMaxInt:
            return CstMaxInt
        if positive == -1 and longVal > CstMinInt:
            return -CstMinInt
        return longVal * positive

CstMaxInt = 2**31 - 1
CstMinInt = 2**31
