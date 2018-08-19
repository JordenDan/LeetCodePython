#https://leetcode-cn.com/problems/regular-expression-matching/description/

#is not finished yet.

class Solution:
    class MetaInfo:
        def __init__(self, str, beMore=False):
            # if beMore, str should be a charactor or "."
            # str: ".", char, string(beMore=False)
            self.str = str
            self.beMore = beMore

        def match(self, str):
            if self.str != ".":
                if not self.beMore:
                    return self.str == str
                else:
                    if len(self.str) > 1:
                        # string, but set beMore. invalid pattern
                        return False
                    if str == "":
                        return True
                    return self.str * len(str) == str
            else:  # "."
                if not self.beMore:
                    return len(str) == 1
                else:
                    return True

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0

        patternLst = []
        if not self.cvt2PatternLst(p, patternLst):
            return False

        return self.checkByPattern(s, patternLst)

    def checkByPattern(self, s, patternLst):



    def cvt2PatternLst(self, patternStr, patternLst):
        idxj = 0
        str = ""
        while idxj < len(patternStr):
            if patternStr[idxj] == ".":
                if len(str) != 0:
                    patternLst.append(Solution.MetaInfo(str))
                str = "."
            elif patternStr[idxj] == "*":
                if len(str) == 0:
                    return False
                elif len(str) == 1:
                    patternLst.append(Solution.MetaInfo(str, True))
                else:
                    patternLst.append(Solution.MetaInfo(str[:-1]))
                    patternLst.append(Solution.MetaInfo(str[-1], True))
                str = ""
            else:
                str += patternStr[idxj]


sln = Solution()
print(sln.isMatch("aa", "a") == False)
print(sln.isMatch("aa", "a*") == True)
print(sln.isMatch("ab", ".*") == True)
print(sln.isMatch("aab", "c*a*b") == True)
print(sln.isMatch("mississippi", "mis*is*p*.") == False)
print(sln.isMatch("mississippi", "mis*is*ip*.") == True)
print(sln.isMatch("avc", "*") == False)
print(sln.isMatch("missippi", "mis**is*ip*.") == False)
