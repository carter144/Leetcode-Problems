"""
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

Solution:
This problem is similar to the level order traversal.
We will start with a queue to utilize BFS. Each will use a hash_map to store the nodes on each level
 {
	"level": [nodes]
 }

 We will then iterate through the keys (levels) in the hash map and reverse the  odd number levels to make the zig zag pattern

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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        
        res = []
        hash_map = {}
        if root is None:
            return root
        
        
        queue.append({"node": root, "level": 0})
        
        
        while len(queue) > 0:
            
            curr_item = queue.pop(0)
            curr_level = curr_item["level"]
            curr_node = curr_item["node"]
            
            if curr_level not in hash_map:
                hash_map[curr_level] = []
            hash_map[curr_level].append(curr_node.val)
            
            if curr_node.left is not None:
                queue.append({"node": curr_node.left, "level": curr_level + 1})
            if curr_node.right is not None:
                queue.append({"node": curr_node.right, "level": curr_level + 1})
                
        for key in sorted(hash_map.keys()):
            if key % 2 == 1:
                res.append(hash_map[key][::-1])
            else:
                res.append(hash_map[key])
        return res