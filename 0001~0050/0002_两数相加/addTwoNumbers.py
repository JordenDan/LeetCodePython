# https://leetcode-cn.com/submissions/detail/5462872/ 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getHeadVal(self, lst):
        if lst == None:
            return 0
        val = lst.val
        lst = lst.next
        return val

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1head = l1
        l2head = l2
        pTail = ListNode(0);
        pHeadPre = pTail;
        carryVal = 0
        while l1head != None or l2head != None:
            #val1 = self.getHeadVal(l1head)
            #val2 = self.getHeadVal(l2head)
            
            if l1head == None:
                val1 = 0
            else:    
                val1 = l1head.val
                l1head = l1head.next
            
            if l2head == None:
                val2 = 0
            else:    
                val2 = l2head.val
                l2head = l2head.next
                
            val = val1 + val2 + carryVal
            carryVal = val // 10;
            curNode = ListNode(val % 10)
            pTail.next = curNode
            pTail = curNode;
        if (carryVal != 0):
            curNode = ListNode(carryVal)
            pTail.next = curNode
            pTail = curNode;
            
        return pHeadPre.next
