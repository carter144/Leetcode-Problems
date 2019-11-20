"""
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

Solution:
1. Perform a DFS and add 1 at each time we call the dfs function
2. We can also perform a BFS to keep track of each level for each node

Both of the same runtime of O(N) since we traverse every node.
Both have the same space O(N): DFS for call stack, and BFS for queue

"""

# DFS
class Solution:
    
    def dfs(self, node):
        if node is None:
            return 0
        
        
        return 1 + max(self.dfs(node.left),self.dfs(node.right))
        
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        
        return 1 + max(left, right)

# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = 0
        if root is None:
            return 0
        
        queue = []
        
        queue.append({"node": root, "level": 1})
        
        while len(queue) > 0:
            current = queue.pop(0)
            
            curr_node = current["node"]
            curr_level = current["level"]
            res = max(res, curr_level)
            
            if curr_node.left is not None:
                queue.append({"node": curr_node.left, "level": curr_level + 1})
            if curr_node.right is not None:
                queue.append({"node": curr_node.right, "level": curr_level + 1})
        return res