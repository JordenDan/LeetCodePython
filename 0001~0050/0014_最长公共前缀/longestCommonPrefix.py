#https://leetcode-cn.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if 0 == len(strs):
            return ""
        if 1 == len(strs):
            return strs[0]

        strs.sort(key=lambda t: len(t))

        firstStr = strs[0]
        subStrLen = len(firstStr)
        for idx in range(1, len(strs)):
            subStrLen = self.interSect(firstStr[:subStrLen], strs[idx])
            if subStrLen == 0:
                return ""
        return firstStr[:subStrLen]

    def interSect(self, str1, str2):
        """
        两个字符串取公共首字符串,str1长度小于str2
        :param str1:
        :param str2:
        :return: 返回公共首字符串的长度
        """
        for subLen in range(len(str1), 0, -1):
            try:
                if str2.index(str1[:subLen]) == 0:
                    return subLen
            except:
                continue
        return 0

sln = Solution()

print("TestCase1: ", sln.longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print("TestCase2: ", sln.longestCommonPrefix(["dog", "racecar", "car"]) == "")


#最优方法
class SolutionBest:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest=min(strs, key=len)
        for x, y in enumerate(shortest):
            for s in strs:
                if s[x]!=y:
                    return shortest[:x]
        return shortest
