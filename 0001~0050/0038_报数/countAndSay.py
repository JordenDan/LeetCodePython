class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ""
        maxCountAndSay = "1"
        for _ in range(1, n):
            maxCountAndSay = self.getNextVal(maxCountAndSay)
        return maxCountAndSay

    def getNextVal(self, maxCountAndSay):
        firstChar = maxCountAndSay[0]
        count = 0
        tmpCountAndSay = ""
        for idx in range(len(maxCountAndSay)):
            if maxCountAndSay[idx] == firstChar:
                count += 1
                continue
            tmpCountAndSay += str(count) + firstChar
            firstChar = maxCountAndSay[idx]
            count = 1
        if 0 != count:
            tmpCountAndSay += str(count) + firstChar
        return tmpCountAndSay
