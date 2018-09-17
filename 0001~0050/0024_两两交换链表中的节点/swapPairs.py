from ListNode import ListNode
from collections import deque


class Solution(object):
    def swapPairs(self, head):
        curHead = head
        rtnHead = ListNode(-1)
        preTail = rtnHead
        dock = deque()
        while curHead is not None:
            dock.append(curHead)
            curHead = curHead.next
            if len(dock) >= 2:
                while len(dock) > 0:
                    preTail.next = dock.pop()
                    preTail = preTail.next
        if len(dock) == 0:
            preTail.next = None
        else:
            preTail.next = dock.popleft()
        return rtnHead.next