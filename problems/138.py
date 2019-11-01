"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.

Solution:
1. Create a hash_map
2. For each item in the list, create a node and place it into the hash_map
	2a. Do not set any pointers of next or random yet.
3. Loop through the list again and retrieve each node to set the next and random pointers to the current node's hash.

Runtime: O(N)
Space: O(N)
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hash_map = {}
        
        
        if head is None:
            return None
        
        
        curr = head
        
        while curr is not None:
            hash_map[curr] = Node(curr.val, None, None)
            curr = curr.next
            
        curr = head
        
        while curr is not None:
            if curr.next is None:
                hash_map[curr].next = None
            else:
                hash_map[curr].next = hash_map[curr.next]
            if curr.random is None:
                hash_map[curr].random = None
            else:
                hash_map[curr].random = hash_map[curr.random]
            curr = curr.next
        
        return hash_map[head]