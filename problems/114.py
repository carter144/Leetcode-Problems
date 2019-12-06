"""
114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

Solution:
Perform a preorder traversal keep track of the previous node
set root.right to previous and root.left will always be none
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
    
    def __init__(self):
        self.prev = None
    def preOrder(self, root):
        if root == None:
            return
    
        
        self.preOrder(root.right)
        self.preOrder(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root
        
        
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        
        self.preOrder(root)
