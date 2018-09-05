class Solution:
    def generateParenthesis(self, n):
        dictTmp = {"": 0}
        for idx in range(n * 2):
            dictTmp = self.__getNextParens(dictTmp, idx, n)

        rtn = []
        for key in dictTmp.keys():
            if dictTmp[key] != 0:
                continue
            rtn.append(key)
        return rtn

    def __getNextParens(self, dictTmp, idx, n):
        dictNew = {}
        for key in dictTmp.keys():
            stack = dictTmp[key]
            # a + b = idx
            # a - b = stack
            if stack > n or idx + stack > 2 * n or idx - stack > 2 * n:  # too many (
                continue

            if n > stack > 0:
                if 2 * n - idx - 1 > stack:
                    dictNew[key + "("] = stack + 1
                dictNew[key + ")"] = stack - 1
            elif stack == 0:
                dictNew[key + "("] = stack + 1
            else:  # stack == n
                dictNew[key + ")"] = stack - 1
        return dictNew
