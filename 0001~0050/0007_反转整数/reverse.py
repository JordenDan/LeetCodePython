#https://leetcode-cn.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.getSign(x) * self.getRevert(abs(x));
        
    def getSign(self, x):
        if (x >= 0):
            return 1
        else:
            return -1;
        
    def getRevert(self, val):
        valLst = list()
        tmp = val
        while 1 :
            valLst.append(tmp % 10) 
            if (tmp >= 0 and tmp < 10):
                break
            tmp = tmp // 10
        return self.cvtLst2Val(valLst)

    def cvtLst2Val(self, valLst):
        rtnVal = 0
        for idx in range(len(valLst)):
            rtnVal = rtnVal * 10 + valLst[idx]
            if (rtnVal > 2 ** 31 - 1): #发生翻转
                return 0
        return rtnVal 
