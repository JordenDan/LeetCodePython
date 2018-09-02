from ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lCNode, rCNode = l1, l2
        pHead = ListNode(-1)
        pCur = pHead
        while lCNode is not None and rCNode is not None:
            if lCNode.val <= rCNode.val:
                pCur.next = lCNode
                pCur = lCNode
                lCNode = lCNode.next
            else:
                pCur.next = rCNode
                pCur = rCNode
                rCNode = rCNode.next
        while lCNode is not None:
            pCur.next = lCNode
            pCur = lCNode
            lCNode = lCNode.next
        while rCNode is not None:
            pCur.next = rCNode
            pCur = rCNode
            rCNode = rCNode.next

        return pHead.next