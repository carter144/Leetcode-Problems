"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

Solution:
Perform a BFS with a queue
On each iteration of the while loop we look at the items currently in the queue.
We want to take th e most right element which would be the last item of the queue
We have to loop through the elements and check if the index is the last item and if is, we add it to the result array.
Runtime: O(N)
Space: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        queue = []
        res = []
        if root is None:
            return []
        queue.append(root)
        
        
        
        while (queue):
            size = len(queue)
            for i in range(size):
                current = queue.pop(0)
                
                if (i == size - 1):
                    res.append(current.val)
            
                if current.left is not None:
                    queue.append(current.left)
                    
                if current.right is not None:
                    queue.append(current.right)
        return res