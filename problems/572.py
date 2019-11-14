"""
572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

Solution:
Have a helper function to check if two trees are exactly the same.
Recursive call this function passing in s and t, if they are not equal then recursively check s.left and s.right against t.

Runtime O(N)
Space: O(N)
"""
class Solution:
    
    def isSameTree(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None and t2 is not None:
            return False
        if t1 is not None and t2 is None:
            return False
        if t1.val != t2.val:
            return False
        
        
        if t1 is None and t2 is not None:
            return False
        if t1 is not None and t2 is None:
            return False
        
        
        return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
        
    
    
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        
        if self.isSameTree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right , t)