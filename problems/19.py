"""
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

Solution:
To do this in one pass we need two pointers p1 and p2.
We move p1 n amount of times down the linked list.
Then we make a loop that moves p1 and p2 down the list (p2 starts at head and p1 starts at wherever n is)
Once p1 hits the end of the list we know that the element we need to remove is p2.
To remove the element that p2 is pointing at we need to keep track of the previous node.
We simply set the previous node to p2's next node.

O(N) runtime
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = head
        prev = None
        res = head
        if head is None:
            return None
        if head.next is None and n == 1:
            return None
        if head.next is None:
            return head

        

        for i in range(n):
            p1 = p1.next
        
        while p1 is not None:
            p1 = p1.next
            prev = p2
            p2 = p2.next
        if prev is None:
            return res.next
        else:
            prev.next = p2.next
        
        return res