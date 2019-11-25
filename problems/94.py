"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

Solution:
Perform an in-order traversal using recursion. Append each element to a list and return it instead of printing. In order is left, root, right
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
    
    
    def inorder(self, root, temp):
        if root is None:
            return
        
        self.inorder(root.left, temp)
        temp.append(root.val)
        self.inorder(root.right, temp)
    
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        temp = []
        
        self.inorder(root, temp)
        
        return temp

