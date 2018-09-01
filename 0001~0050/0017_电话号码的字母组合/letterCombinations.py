import time

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitMap = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        lst = []
        for num in digits:
            if num not in digitMap:
                return []
            curLetters = digitMap[num]
            if not lst:
                for char in curLetters:
                    lst.append(char)
            else:
                # lstTmp = []
                # for str, ch in [(str, ch) for str in lst for ch in curLetters]:
                #     lstTmp.append(str + ch)
                # lst = lstTmp
                lst = [str + ch for str in lst for ch in curLetters]
        return lst


sln = Solution()

expect = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
begin = time.clock()
print("TestCase1:", sln.letterCombinations("23") == expect, "take %.3fms" % ((time.clock() - begin) * 1000))

expect = ["mmp", "mmq", "mmr", "mms", "mnp", "mnq", "mnr", "mns",
          "mop", "moq", "mor", "mos", "nmp", "nmq", "nmr", "nms",
          "nnp", "nnq", "nnr", "nns", "nop", "noq", "nor", "nos",
          "omp", "omq", "omr", "oms", "onp", "onq", "onr", "ons",
          "oop", "ooq", "oor", "oos"]
begin = time.clock()
print("TestCase2:", sln.letterCombinations("667") == expect, "take %.3fms" % ((time.clock() - begin) * 1000))
