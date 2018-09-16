from ListNode import ListNode
from heapq import heappush, heappop, heapify


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(node.val, index, node) for index, node in enumerate(lists) if node]
        heapify(h)
        sorted_head = ListNode(-1)
        cur = sorted_head
        while h:
            (cur_min, index, node) = heappop(h)
            next_node = node.next
            if next_node:
                heappush(h, (next_node.val, index, next_node))
            node.next = None
            cur.next = node
            cur = cur.next
        return sorted_head.next
