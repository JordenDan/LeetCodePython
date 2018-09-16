import time
#from mergeKLists import Solution
from bestDemo import Solution

from ListNode import ListNode

if __name__ == "__main__":
    sln = Solution()

    kLsts = ListNode.createLstLst([[1, 4, 5], [1, 3, 4], [2, 6]])

    tic = time.clock()
    lstRst = sln.mergeKLists(kLsts)
    toc = time.clock()
    expectRst = "1,1,2,3,4,4,5,6"
    print("TestCase1:", ListNode.printNode(lstRst) == expectRst, " —— take %.3f ms" % ((toc - tic) * 1000))

    kLsts = ListNode.createLstLst([[1, 4, 5, 11], [1, 3, 4], [2, 6], [6, 8, 9], [7]])

    tic = time.clock()
    lstRst = sln.mergeKLists(kLsts)
    toc = time.clock()
    expectRst = "1,1,2,3,4,4,5,6,6,7,8,9,11"
    print("TestCase2:", ListNode.printNode(lstRst) == expectRst, " —— take %.3f ms" % ((toc - tic) * 1000))

    with open('TestCase3.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(line)

    #
    # lstHead = ListNode.createLst([5, 2, 3, 4, 5, -8, 10, 22, -12, -23, 11, 0, 13, 22, 100])
    # tic = time.clock()
    # lstRst = sln.removeNthFromEnd(lstHead, 6)
    # toc = time.clock()
    # expectRst = "5,2,3,4,5,-8,10,22,-12,11,0,13,22,100"
    # print("TestCase3:", ListNode.printNode(lstRst) == expectRst, " —— take %.3f ms" % ((toc - tic) * 1000))

