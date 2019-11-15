"""
72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Solution:
1. Create a 2D array for DP, the number of rows is the length of the first word + 1 and the number of columns is the length of the second word + 1.
2. Make a for loop from i to the length of row and set dp[i][0] = i, Do the same for columns.
3. Loop from 1 to m (outer loop) loop from 1 to n (inner loop)
		3a. If word2[row -  1] == word1[col - 1] then dp[row][col] = dp[row - 1][col - 1]
		3b. else: dp[row][col] = 1 + min(dp[row - 1][col, dp[row][col - 1], dp[row - 1][col - 1])
4. return dp[m - 1][ n - 1]
Runtime: O(M*N) 
Space: O(M*N)
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) + 1
        n = len(word2) + 1
        dp = [[0 for x in range(m)] for y in range(n)]
        
        dp[0][0] = 0
        for i in range(1, n):
            
            dp[i][0] = i
            
            
        for j in range(1, m):
            dp[0][j] = j
            
        for row in range(1, n):
            for col in range(1, m):
                if word2[row - 1] == word1[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    dp[row][col] = 1 + min(dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1])
        return dp[n - 1][m - 1]