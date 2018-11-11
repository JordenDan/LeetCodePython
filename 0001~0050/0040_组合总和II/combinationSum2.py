class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        maxCnt = []
        for val in candidates:
            if not maxCnt or maxCnt[-1][0] != val:
                maxCnt.append([val, 1])
            else:
                maxCnt[-1][1] += 1

        ansLst = []
        self.getCombination(maxCnt, target, ansLst)


        return ansLst

    def getCombination(self, maxCnt, target, ansLst):
        if len(maxCnt) == 0:
            return

        if len(maxCnt) == 1 and target % maxCnt[0][0] == 0:
            maxC = target // maxCnt[0][0]
            if maxC <= maxCnt[0][1]:
                ansLst.append([maxCnt[0][0]] * maxC)
            return

        for cnt in range(0, maxCnt[0][1] + 1):
            targetLeft = target - cnt * maxCnt[0][0]
            if targetLeft < 0:
                break

            if targetLeft == 0:
                ansLst.append([maxCnt[0][0]] * cnt)
                break

            ansLstTmp = []
            self.getCombination(maxCnt[1:], targetLeft, ansLstTmp)
            if not ansLstTmp:
                continue

            for idx in range(len(ansLstTmp)):
                if cnt != 0:
                    ansLstTmp[idx].extend([maxCnt[0][0]] * cnt)
            ansLst.extend(ansLstTmp)