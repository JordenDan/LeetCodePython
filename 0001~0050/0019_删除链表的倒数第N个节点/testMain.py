import time
from removeNthFromEnd import Solution
#from removeNthFromEndDemo import Solution

from ListNode import ListNode

if __name__ == "__main__":
    sln = Solution()

    lstHead = ListNode.createLst([1])
    tic = time.clock()
    lstRst = sln.removeNthFromEnd(lstHead, 1)
    toc = time.clock()
    expectRst = ""
    print("TestCase1:", ListNode.printNode(lstRst) == expectRst, " —— take %.3f ms" % ((toc - tic) * 1000))

    lstHead = ListNode.createLst([1, 2, 3, 4, 5])
    tic = time.clock()
    lstRst = sln.removeNthFromEnd(lstHead, 2)
    toc = time.clock()
    expectRst = "1,2,3,5"
    print("TestCase2:", ListNode.printNode(lstRst) == expectRst, " —— take %.3f ms" % ((toc - tic) * 1000))

    lstHead = ListNode.createLst([5, 2, 3, 4, 5, -8, 10, 22, -12, -23, 11, 0, 13, 22, 100])
    tic = time.clock()
    lstRst = sln.removeNthFromEnd(lstHead, 6)
    toc = time.clock()
    expectRst = "5,2,3,4,5,-8,10,22,-12,11,0,13,22,100"
    print("TestCase3:", ListNode.printNode(lstRst) == expectRst, " —— take %.3f ms" % ((toc - tic) * 1000))

