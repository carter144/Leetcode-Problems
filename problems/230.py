"""
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Solution:
Since we know this is a BST, the in order traversal will provide us a sorted list. We just have to return the value in k - 1 position after the in order traversal of the tree.

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
    
    def inOrder(self, root, res):
        if root is None:
            return
        
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        res = []
        if root is None:
            return None
        
        
        self.inOrder(root, res)
        return res[k - 1]