"""
23. Merge k sorted lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


Solution:
The solution is pretty simple. We create a min heap and put all the nodes into the min heap.  Then we pop everything off the heap and it will be in sorted order

O(n log k) where n is the number of nodes and k is the number of linked lists
O(n) space for the heap
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        
        heap = []
        for head in lists:
            curr_node = head
            
            
            while curr_node is not None:
                heapq.heappush(heap, curr_node.val)
                curr_node = curr_node.next
                
        res = ListNode(-1)
        
        res_temp = res
        
        while len(heap) > 0:
            res_temp.next = ListNode(heapq.heappop(heap))
            res_temp = res_temp.next
        return res.next