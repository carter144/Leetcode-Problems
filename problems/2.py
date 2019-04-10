"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


Solution:

Loop through the two linked lists until one of them is Null/None and create a node for each time we add the two nodes together.
Check to make sure if the sum of the two nodes are greater than or equal to 10, if so we mod by 10 to get the right digit and set a carry flag to 1
Create nodes for remainder of the lists if they are different sizes and add the carry if there is one.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        dummy = res
        
        p = l1
        q = l2

        carry  = 0

        while p is not None and q is not None:
            temp_sum = p.val + q.val + carry


            if temp_sum >= 10:
                carry = 1
                dummy.next = ListNode(temp_sum % 10)
            else:
                carry = 0
                dummy.next = ListNode(temp_sum)


            dummy = dummy.next
            p = p.next
            q = q.next

        while p is not None:
            temp_sum = p.val + carry

            if temp_sum >= 10:
                carry = 1
                dummy.next = ListNode(temp_sum % 10)
            else:
                carry = 0
                dummy.next = ListNode(temp_sum)
            dummy = dummy.next
            p = p.next

        while q is not None:
            temp_sum = q.val + carry
            if temp_sum >= 10:
                carry = 1
                dummy.next = ListNode(temp_sum % 10)
            else:
                carry = 0
                dummy.next = ListNode(temp_sum)
            dummy = dummy.next
            q = q.next
            
        if carry:
            dummy.next = ListNode(1)
        return res.next