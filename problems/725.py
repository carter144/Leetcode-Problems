"""
725. Split Linked List in Parts

Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].

Solution:
1. Calculate the length of each the entire linked list
2. We will have to divide the linked list into k buckets.
	2a. Calculate the max_width (max amount of items a bucket can hold)
	2b. If there is a remainder, then the first buckets will have max_width + 1 elements
3. If there are more buckets than the length of the linked list, we just put one element in each bucket.
4. Continuously add elements to the current bucket, and when that gets full we change buckets.

Runtime: O(N)
Space: O(N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        res = []
        
        for i in range(k):
            res.append( ListNode(None))
        
        length = 0
        temp = root;
        while temp is not None:
            length += 1
            temp = temp.next
        
        max_width = length // k
       
        remainder = length % k
        
        if length < k:
            max_width = 1
            remainder = 0
        curr_node = root
        index = 0
        count = 0
        bucket_list = res[index]
        while curr_node is not None:
           
            if remainder > index:
                
                if count >= max_width + 1:
                    count = 0
                    index += 1
                    bucket_list = res[index]
                    
                
            else:
                
                if count >= max_width:
                    count = 0
                    index += 1
                    bucket_list = res[index]
            
            
            bucket_list.next = ListNode(curr_node.val)
            bucket_list = bucket_list.next
            
            curr_node = curr_node.next
            count += 1
        for i in range(k):
            res[i] = res[i].next
        return res
                    
                
