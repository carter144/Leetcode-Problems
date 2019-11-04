"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

Solution:
Use dynamic programming.
1. Start from the bottom right corner and simulate moving up or left.
2. Have a recursive method to help.
	2a. Base case is when x == 0 and y == 0.
	2b. Check for cases when only x == 0 or only y == 0: return 1
	2c. return the recursive call to left + recursive call going up.
	2d. Use a hash_table to store results (memoization)
"""
class Solution:
    
    
    def helper(self, x, y, memo):
        
        key = str(x) + "-" + str(y)
        if key in memo:
            return memo[key]
        
        if x == 0 and y == 0:
            return 0
        
        if x == 0:
            return 1
        if y == 0:
            return 1
        
        memo[key] = self.helper(x - 1, y, memo) + self.helper(x, y - 1, memo)
        return memo[key]
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 and n == 1:
            return 1
        memo = {}
        return self.helper(m - 1, n - 1, memo)