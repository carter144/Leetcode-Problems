"""
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

Solution:

1. Make a variable called temp that will point to the head
2. Check edge case when head is null (empty linked list)
3. Remove elements at the beginning of the list by moving temp to the next in a while loop when the values are equal.
4. Have another pointer curr that points at temp, we will use this variable to iterate the remaining linked list elements.
5. If we found a node with the value, we keep moving curr to the next until the values are not equal. Then we set the previous node to the current node we land on.
6. The previous node will then be set to curr
7. return the temp variable
Runtime: O(N)
Space: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = head
        if head is None:
            return None
        
        
        while temp is not None and temp.val == val:
            temp = temp.next
        
        curr = temp
        
        
        prev = None
        while curr is not None:
            if curr.val == val:
                while curr is not None and curr.val == val:
                    curr = curr.next
                prev.next = curr
                
            
            prev = curr
            if curr is not None:
                curr = curr.next
        
        
        return temp