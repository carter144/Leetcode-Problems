"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

Solution:
1. Create a 2d array of the size of the input
2. Iterate through the grid, and fill the new 2d array with the values it currently has
3. Fill the rest of the array by:
	3a. If i and j are both > 0 take the min of the left, or up
	3b. if i > 0 take the value of going up
	3c. if j > 0 take the value of going left
4. return the value in the bottom right corner
Runtime: O(M*N)
Space: O(M*N)
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for x in range(n)] for y in range(m)]
        
        
        for i in range(m):
            for j in range(n):
                
                # Fill the dp with the value at i, j
                dp[i][j] += grid[i][j]
                
                
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
                
                elif i > 0:
                    dp[i][j] += dp[i - 1][j]
                
                elif j > 0:
                    dp[i][j] += dp[i][j - 1]
                    
        return dp[m - 1][n - 1]