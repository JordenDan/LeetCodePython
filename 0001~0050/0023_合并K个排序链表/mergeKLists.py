from ListNode import ListNode


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        rtn = None
        for idx in range(len(lists)):
            rtn = self.mergeTwoLst(rtn, lists[idx])
        return rtn

    def mergeTwoLst(self, listA, listB):
        if listA is None:
            return listB
        if listB is None:
            return listA

        headA = listA
        headB = listB
        rtn = ListNode(0)
        headRtn = rtn

        while headA is not None and headB is not None:
            # both are not none.
            # print("headA.val=%d, headB.val=%d" % (headA.val, headB.val))
            if headA.val <= headB.val:
                headRtn.next = headA
                headRtn = headRtn.next
                headA = headA.next
            else:
                headRtn.next = headB
                headRtn = headRtn.next
                headB = headB.next

        if headA is None:
            headRtn.next = headB
        else:
            headRtn.next = headA
        return rtn.next
