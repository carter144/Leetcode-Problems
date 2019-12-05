"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

Solution:
A balanced binary tree is as follows:
If the height of the left sub tree is <= 1 of the height of the right sub tree when we take the difference
So we have to take the depth of left sub tree and depth of right sub tree
take the absolute difference and return false if >= 2.
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
    
    def depth(self, root):
        if root is None:
            return 0
        
        else:
            return 1 + max(self.depth(root.left), self.depth(root.right))
    def isBalanced(self, root: TreeNode) -> bool:
        

        if root is None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        
       
        if abs(left - right) >= 2:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)