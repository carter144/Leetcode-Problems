"""
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1

Solution:
DP problem.
1. Create a dp array of length (amount + 1) and intialize all values to (amount + 1)
2. We use + 1 since arrays are 0 indexed, an we want to have each index of the array to be the answer for the amount. For example, index 10 in an array would be the answer to make value 10. However if our array is length 10, we only have indexes from 0-9.
3. Initialize 0 index to 0 since it takes 0 coins to make 0.
4. Loop through the dp array and check each coin(inner loop), see if we can take the coin, if so we add 1 + (the ANSWER OF (index - current coin))
5. If the index remains amount + 1, then we return -1
Runtime: O(m*n)
Space: O(n)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

    	# Initialize our dp array since each index will store the result
        dp = [amount + 1] * (amount + 1)

        # 0 coins to make 0
        dp[0] = 0

        # sort the coins so we can break out early
        coins = sorted(coins)
        
        # Loop through the dp array
        for i in range(1, amount + 1):
        	# loop through all coins at current index
            for j in range(len(coins)):

            	# if we subtract a coin, and we are within the array then this means we took a coin.
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
                else:
                	# if we are not able to take a coin we break
                    break
        
        
        # check if the last index was updated, if it wasn't then return -1
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]