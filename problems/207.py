"""
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

Solution:
Perform a DFS to check if there is a cycle in the graph. If there is a cycle then we return false.
Runtime: O(N)
Space: O(N)
"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
class Solution:

    def hasCycle(self, current, whiteSet, greySet, blackSet):
        if current in whiteSet:
            whiteSet.remove(current)
        if current in greySet:
            return True
        if current in blackSet:
            return False
        greySet.add(current)
        for neighbor in current.neighbors:
            if (self.hasCycle(neighbor, whiteSet, greySet, blackSet)):
                return True
        
        greySet.remove(current)
        blackSet.add(current)
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        Nodes = [None] * numCourses
        
        for i in range(numCourses):
            Nodes[i] = Node(i, [])
            
        for path in prerequisites:
            start = path[0]
            end = path[1]
            
            Nodes[start].neighbors.append(Nodes[end])
        whiteSet = set()
        greySet = set()
        blackSet = set()
        for node in Nodes:
            whiteSet.add(node)

        for node in Nodes:
            if self.hasCycle(node, whiteSet, greySet, blackSet):
                return False
        return True

        
        
