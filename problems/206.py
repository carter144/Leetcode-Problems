"""
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

Solution:
Have three pointers: prev, curr, and next
On each iteration we set the next to curr.net
then we set curr.next to previous
and the prev pointer becomes curr
then set curr to next
Runtime: O(N)
Space: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        
        prev = None
        curr = head
        next = head.next
        res = head
        
        while curr is not None:
            
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev