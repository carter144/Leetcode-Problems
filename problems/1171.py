"""
1171. Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]

Solution:
1. Convert the linked list to an array
2. Iterate through the array and keep track of seen elements with a stack
3. Try to reach a 0 sum by looking at the current element and summing items from the top of the stack.
	3a. If we are able to reach 0 sum then we continue on with the iteration
	3b. Otherwise we have to add the items back onto the stack along with the current element.
4. Convert the stack into a linked list
5. return the linked list

Runtime: O(N^2)
Space: O(N)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        converted = []
        
        stack = []
        if head is None:
            return None
        while head is not None:
            converted.append(head.val)
            head = head.next
        
        #stack.append(converted[0])
        
        
        for i in range(0, len(converted)):
            if converted[i] == 0:
                continue
            if len(stack) == 0:
                stack.append(converted[i])
                continue
            top = stack[-1]
            
            if top + converted[i] == 0:
                stack.pop()
                continue
            else:
                
                curr_num = converted[i]
                num_to_be_popped = -1
                
                for j in range(len(stack)):
                    curr_num += stack[len(stack) - 1 -j]
                    if curr_num == 0:
                        num_to_be_popped = j + 1
                        break
                if num_to_be_popped != -1:
                    while num_to_be_popped > 0:
                        stack.pop()
                        num_to_be_popped -= 1
                
                
                else:
                    stack.append(converted[i])
                    
                    
        if len(stack) == 1:
            if stack[0] == 0:
                return None
                    
        res = ListNode(None)
        res1 = res
        for item in stack:
            res.next = ListNode(item)
            res = res.next
        return res1.next