"""
1110. Delete Nodes And Return Forest
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Solution:
1. Perform a DFS on each node of the tree.
2. If the current node's value is to be deleted, we ignore it and add the left and right subtrees to the result array
3. Check if the root value is to be deleted, if it isn't then we add it to the result array

Runtime O(N) Must touch every single node.
Space: O(N) recursive stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self, node, toDelete, res):
        if node is None:
            return None

        node.left = self.dfs(node.left, toDelete, res)
        node.right = self.dfs(node.right, toDelete, res)
        
        if node.val in toDelete:
            
            if node.left is not None:
                res.append(node.left)
            if node.right is not None:
                res.append(node.right)
        
            return None
        return node
        
        
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        toDelete = set(to_delete)
        if root is None:
            return None
        res = []
        
        self.dfs(root, toDelete, res)
        if root.val not in toDelete:
            res.append(root)
        
        return res