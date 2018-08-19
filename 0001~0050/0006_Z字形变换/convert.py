# https://leetcode-cn.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str,
        """
        if numRows == 1:
            return s

        zMap = dict()
        for idx in range(len(s)):
            rowIdx = self.getPos(numRows, idx)
            if not rowIdx in zMap:
                zMap[rowIdx] = []
            zMap[rowIdx].append(s[idx])
        sLst = []
        for key in zMap.keys():
            sLst.extend(zMap[key])
        return "".join(sLst)

    def getPos(self, numRows, idx):
        zSize = numRows * 2 - 2
        nZCnt = idx // zSize
        nZPos = idx - nZCnt * zSize
        if nZPos < numRows:
            return nZPos
        else:
            return 2 * numRows - 2 - nZPos
