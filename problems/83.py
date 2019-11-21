"""
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

Solution:
We iterate through the linked list like normally. Since the list is sorted we know that duplicate elements will be adjacent to each other. Therefore we have to check the next node at each iteration of the current node. If they have the same value we set current's node to the next element that is different.
Runtime: O(N)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
       
        while curr is not None:
            next_node = curr.next
            if next_node is None:
                break
            while next_node.val == curr.val:
                next_node = next_node.next
                if next_node is None:
                    curr.next = None
                    return head
            curr.next = next_node
            curr = curr.next
        return head