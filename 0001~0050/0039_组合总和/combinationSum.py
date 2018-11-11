class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ansLst = []
        self.getCombination(candidates, target, ansLst)
        return ansLst

    def getCombination(self, candidates, target, ansLst):
        if not candidates:
            return
        firstCand = candidates[0]
        cnt = 0
        while firstCand * cnt <= target:
            targetLeft = target - firstCand * cnt
            if targetLeft == 0 and cnt != 0:
                ansLst.append([firstCand] * cnt)
                break

            ansLstTmp = []
            self.getCombination(candidates[1:], targetLeft, ansLstTmp)
            if not ansLstTmp:
                cnt += 1
                continue
            for idx in range(len(ansLstTmp)):
                ansLstTmp[idx].extend([firstCand] * cnt)
                ansLst.append(ansLstTmp[idx])
            cnt += 1