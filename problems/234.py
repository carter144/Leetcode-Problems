"""
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

Solution:
Push every element from the linkedlist on to a stack
Iterate through every element of the linked list and make sure it is equal to the top of the stack while popping items off.
Runtime: O(N)
Space: O(N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        
        
        temp = head
        
        if head is None:
            return True
        
        if head.next is None:
            return True
        
        
        while temp is not None:
            stack.insert(0, temp.val)
            
            temp = temp.next
            
            
        
        
        temp = head
        
        
        while temp is not None:
            elem = stack.pop(0)
            
            
            if elem != temp.val:
                return False
            temp = temp.next
        return True