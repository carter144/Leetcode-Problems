"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

Solution:
Run a regular BFS with a queue and add the nodes onto the queue at each step.
When we encounter a node with no children, we  return the level that the node was on.

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
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        
        if root.left is None and root.right is None:
            return 1
        
        queue = []
        level = 1
        queue.append({"level": level, "node": root})
        
        while (queue):
            temp_obj = queue.pop(0)
            temp_level = temp_obj["level"]
            temp_node = temp_obj["node"]
            
            if temp_node.left is None and temp_node.right is None:
                return temp_level
            if temp_node.left is not None:
                queue.append({"level": temp_level + 1, "node": temp_node.left})
            if temp_node.right is not None:
                queue.append({"level": temp_level + 1, "node": temp_node.right})