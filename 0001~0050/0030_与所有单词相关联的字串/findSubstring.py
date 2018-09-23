from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        rtn = []
        wordsIdx, wordLen = self.getWordsMap(words)
        if wordLen == -1:
            return rtn
        wordCnt = len(words)
        alreadyFoundSet = set()
        for shiftVal in range(0, wordLen):
            lst = self.cutTxt(s[shiftVal:], wordLen)
            if len(lst) < wordCnt:
                break
            ableLst = self.checkLst(lst, wordCnt, wordsIdx, shiftVal, wordLen, alreadyFoundSet)
            rtn += [idx * wordLen + shiftVal for idx in ableLst]
        return rtn

    def checkLst(self, lst, wordCnt, wordsIdx, shiftVal, wordLen, alreadyFoundSet):
        rtn = []
        for shift in range(0, len(lst) - wordCnt + 1):
            beginIdx = shiftVal + wordLen * shift
            endIdx = beginIdx + wordCnt * wordLen
            if (beginIdx, endIdx) in alreadyFoundSet:
                continue
            alreadyFoundSet.add((beginIdx, endIdx))
            wordsCheck, subLen = self.getWordsMap(lst[shift: shift + wordCnt])
            if wordsCheck == wordsIdx:
                rtn.append(shift)
        return rtn

    def cutTxt(self, rawStr, segLen):
        lst = []
        rawStrLen = len(rawStr)
        for idx in range(0, rawStrLen, segLen):
            endIdx = idx + segLen
            if endIdx <= rawStrLen:
                lst.append(rawStr[idx: endIdx])
        return lst

    def getWordsMap(self, words):
        wordsIdx = Counter(words)
        lenPre = -1
        for word in words:
            lenWord = len(word)
            if lenPre != -1 and lenPre != lenWord:
                return Counter(), -1
            lenPre = lenWord
        return wordsIdx, lenPre
