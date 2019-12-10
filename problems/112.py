"""
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Solution:
Recursively traverse the tree and subtract the root.val from the sum and check if the current val is equal to the sum.
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
    
    
    def helper(self, root, target):
        
        if root is None:
            return False
        
        if target == root.val and root.left is None and root.right is None:
            return True
        
        return self.helper(root.left, target-root.val) or self.helper(root.right, target-root.val)
        
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        
        return self.helper(root.left, sum-root.val) or self.helper(root.right, sum-root.val)