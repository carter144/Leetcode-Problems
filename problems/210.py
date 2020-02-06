"""
210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

Solution:

Perform a topoligical sort using dfs. We also have to check if it is impossible to take the courses by checking if there is a cyccle in the graph.
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
    
    
    def topSort(self, current, visited, stack):
        if current in visited:
            return
        visited.add(current)
        if len(current.neighbors) == 0:
            stack.append(current)
            return
        
        for neighbor in current.neighbors:
            self.topSort(neighbor, visited, stack)
        stack.append(current)
        return
        
        
        
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        Nodes = [None] * (numCourses)
        
        for i in range(numCourses):
            Nodes[i] = Node(i, [])
            
            
        for path in prerequisites:
            start = path[0]
            end = path[1]
            
            Nodes[start].neighbors.append(Nodes[end])
        
        stack = []
        visited = set()
        
        whiteSet = set()
        greySet = set()
        blackSet = set()
        for node in Nodes:
            whiteSet.add(node)

        for node in Nodes:
            if self.hasCycle(node, whiteSet, greySet, blackSet):
                return []
        
        
        
        
        for node in Nodes:
            self.topSort(node, visited, stack)
        res = []
        for elem in stack:
            res.append(elem.val)
        return res
