"""
200. Number of Islands


Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

Solution:
Loop through each cell in the matrix. When we encounter a 1 we increment the number of islands by 1. Then we perform a dfs to flip the adjacent 1's to 0's. Return the amount of islands we counted.
Runtime: O(M*N)
Space: O(M*N)
"""
class Solution(object):
    
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]):
            return
        
        if grid[row][col] == '0':
            return
        
        
        grid[row][col] = '0'
        
        
        
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
        
        
        
        
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                
                if grid[row][col] == '1':
                    res = res + 1
                    self.dfs(grid, row, col)
                    
                    
        return res