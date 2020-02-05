"""
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

Solution:
Brute force perform a dfs and add 1 each time we encounter a node.
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
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        
        if root.left is None and root.right is not None:
            return 1 + self.countNodes(root.right)
        
        if root.right is None and root.left is not None:
            return 1 + self.countNodes(root.left)
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1