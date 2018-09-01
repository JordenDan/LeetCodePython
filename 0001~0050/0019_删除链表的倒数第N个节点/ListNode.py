# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def printNode(head):
        pCur = head
        valLst = []
        while pCur:
            valLst.append(pCur.val)
            pCur = pCur.next
        return ",".join([str(i) for i in valLst])

    @staticmethod
    def createLst(valLst):
        preHead = ListNode(-1)
        tail = preHead
        for num in valLst:
            tail.next = ListNode(num)
            tail = tail.next
        return preHead.next
