import time
from reverseKGroup import Solution
from ListNode import ListNode

if __name__ == "__main__":
    sln = Solution()

    lst = ListNode.createLst([1, 2, 3, 4, 5])
    tic = time.clock()
    lstRst = sln.reverseKGroup(lst, 2)
    toc = time.clock()
    expectRst = "2,1,4,3,5"
    print("TestCase1:", ListNode.printNode(lstRst) == expectRst, " —— take %.3f ms" % ((toc - tic) * 1000))

    lst = ListNode.createLst([1, 2, 3, 4, 5])
    tic = time.clock()
    lstRst = sln.reverseKGroup(lst, 3)
    toc = time.clock()
    expectRst = "3,2,1,4,5"
    print("TestCase2:", ListNode.printNode(lstRst) == expectRst, " —— take %.3f ms" % ((toc - tic) * 1000))

    lst = ListNode.createLst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    tic = time.clock()
    lstRst = sln.reverseKGroup(lst, 4)
    toc = time.clock()
    expectRst = "4,3,2,1,8,7,6,5,12,11,10,9,13,14"
    print("TestCase3:", ListNode.printNode(lstRst) == expectRst, " —— take %.3f ms" % ((toc - tic) * 1000))
