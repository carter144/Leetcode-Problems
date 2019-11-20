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
Perform a recursive binary search. At each recursive call create a node then set the left and right pointers to the recursive call return value. The left will be everything on the left side up to the mid - 1 and the right will be everything from mid + 1 to the right side.
Runtime: O(log N)
Space: O(log N)
"""

class Solution:
    
    def helper(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, left, mid - 1)
        node.right = self.helper(nums, mid + 1, right)
        return node
        
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        return self.helper(nums, 0, len(nums) - 1)