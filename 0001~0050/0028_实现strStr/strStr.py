#https://leetcode-cn.com/problems/implement-strstr/description/

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


#使用index的方法会更加高效
#class Solution:
#    def strStr(self, haystack, needle):
#        """
#        :type haystack: str
#        :type needle: str
#        :rtype: int
#        """
#        try:
#            index = haystack.index(needle)
#            return index
#        except:
#            return -1
#
