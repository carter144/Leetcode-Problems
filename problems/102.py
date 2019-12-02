"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

Solution:
Use BFS and queue to create a level order traversal.
We start with the root element in the queue and keep track of its level by a dictionary object.
It will look like this:
{
	"node": root
	"level": 1
}

We have a while loop that executes while the queue is not empty.
We pop from the queue and increment level by 1 each time we add a new item to the queue.
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        temp = []
        if root is None:
            return []
        level = 0
        queue.append({"node": root, "level": 0})
        res = []
        while (queue):
            
            temp_node = queue.pop(0)
            node_level = temp_node["level"]
            curr_node = temp_node["node"]
            
            
                
            if node_level > level:
                res.append(temp)
                temp = []
                level = level + 1
            temp.append(curr_node.val)
            
            
            
            if curr_node.left is not None:
                queue.append({"node": curr_node.left, "level": node_level + 1})
                
            if curr_node.right is not None:
                queue.append({"node": curr_node.right, "level": node_level + 1})
                
            
        res.append(temp)
        return res