"""
107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

Solution:
Perform a regular level order traversal with BFS and then reverse the result array.
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        queue = []
        res = []
        temp = []
        
        curr_level = 0
        
        if root is None:
            return []
        
        queue.append({"node": root, "level": 0})
        while (queue):
            elem = queue.pop(0)
            curr_node = elem["node"]
            node_level = elem["level"]
            
            if node_level > curr_level:
                res.append(temp)
                temp = []
                curr_level = curr_level + 1
            if curr_node.left is not None:
                queue.append({"node": curr_node.left, "level": node_level + 1})
            if curr_node.right is not None:
                queue.append({"node": curr_node.right, "level": node_level + 1})
            temp.append(curr_node.val)
            
        res.append(temp)
        return res[::-1]