import time
from mergeTwoLists import Solution

from ListNode import ListNode

if __name__ == "__main__":
    sln = Solution()

    l1 = ListNode.createLst([1, 2, 4])
    l2 = ListNode.createLst([1, 3, 4])
    tic = time.clock()
    lstRst = sln.mergeTwoLists(l1, l2)
    toc = time.clock()
    expectRst = "1,1,2,3,4,4"
    print("TestCase1:", ListNode.printNode(lstRst) == expectRst, " —— take %.3f ms" % ((toc - tic) * 1000))
