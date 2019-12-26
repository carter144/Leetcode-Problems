"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

Both of the given trees will have between 1 and 100 nodes.

Solution:
Perform a simple DFS and check if a node is a leaf. If it is a leaf then we add it to the array.
Do this for both trees and then compare the two arrays for matching elements.

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
    def dfs(self, root, leaves):
        
        
        
        if root is None:
            return
        
        if root.left is None and root.right is None:
            leaves.append(root.val)
        
        else:
            self.dfs(root.left, leaves)
            self.dfs(root.right, leaves)
        
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        leaf_1 = []
        leaf_2 = []
        
        
        self.dfs(root1, leaf_1)
        self.dfs(root2, leaf_2)
        
        if len(leaf_1) != len(leaf_2):
            return False
        
        
        for i in range(len(leaf_1)):
            if leaf_1[i] != leaf_2[i]:
                return False
            
        return True