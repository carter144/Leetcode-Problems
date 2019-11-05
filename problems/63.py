"""
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Solution:
Start at the bottom right corner and recursively move up or left.
if the row or column is 0, then we have to move only left or only up.
use a hash_map for memoization to store temporary results.
"""
class Solution:
    
    
    def helper(self, grid, row, col, memo):
        
        key = str(row) + '-' + str(col)
        
        
        if key in memo:
            return memo[key]
        
        if row == 0 and col == 0:
            return 1
        
        if grid[row][col] == 1:
            return 0
        
        
        if col == 0 and row > 0:
            memo[key] = 0 + self.helper(grid, row - 1, col, memo)
            return memo[key]
        
        if col > 0 and row == 0:
            0 + self.helper(grid, row, col - 1, memo)
            memo[key] = 0 + self.helper(grid, row, col - 1, memo)
            return memo[key]
        
        else:
            memo[key] =  0 + self.helper(grid, row - 1, col, memo) + self.helper(grid, row, col - 1, memo)
            return memo[key]
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        row = len(obstacleGrid) - 1
        col = len(obstacleGrid[0]) - 1
        
        if obstacleGrid[0][0] == 1:
            return 0
        if row == 0 and col == 0 and obstacleGrid[row][col] == 0:
            return 1
        if row == 0 and col == 0 and obstacleGrid[row][col] == 1:
            return 0
        
        memo = {}
        return self.helper(obstacleGrid, row, col, memo)