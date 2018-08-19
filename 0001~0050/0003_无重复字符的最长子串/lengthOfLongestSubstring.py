#https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) <= 1:
            return len(s)

        longestLen = 1
        idxi = 0
        while idxi < len(s) - 1:
            idxj = idxi + longestLen
            while idxj < len(s):
                #print("substr=", s[idxi:idxj], ", nextChar=", s[idxj])
                strSet = set(s[idxi:idxj])
                if len(strSet) != idxj - idxi:
                    break
                if not s[idxi:idxj].__contains__(s[idxj]):
                    if idxj - idxi + 1 > longestLen:
                        longestLen = idxj - idxi + 1
                        #longestSubStrPos = (idxi, idxj + 1)
                    idxj += 1
                else:
                    break
            idxi += 1
        return longestLen
