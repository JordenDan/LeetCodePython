import time
from ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head, n):
        lst = []
        pCur = head
        while pCur:
            lst.append(pCur)
            pCur = pCur.next

        lstLen = len(lst)
        if lstLen < n | n <= 0:
            return

        if lstLen == n:
            return head.next

        pPre = lst[-(n+1)]
        pCur = lst[-n]
        pPre.next = pCur.next
        return head



