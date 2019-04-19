"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Solution:
This problem is trivial where we have two pointers. Pointer 1 loops through the first list and Pointer 2 loops through the second list.  At each step, we compare the two node's values at each pointer. We add the smaller value to the result and then increment the pointer of the smaller value.  At the end we take the rest of the remaining list.

O(M + N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(None)
        k = res
        while l1 is not None and l2 is not None:
            
            if l1.val <= l2.val:
                res.next = ListNode(l1.val)
                res = res.next
                l1 = l1.next
                continue
            if l1.val > l2.val:
                res.next = ListNode(l2.val)
                res = res.next
                l2 = l2.next
                continue
        
        while l1 is not None:
            res.next = ListNode(l1.val)
            res = res.next
            l1 = l1.next
        while l2 is not None:
            res.next = ListNode(l2.val)
            res = res.next
            l2 = l2.next
        return k.next


