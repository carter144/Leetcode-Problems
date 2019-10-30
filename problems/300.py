"""
300. Longest Increasing Subsequence


Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

Solution:
1. Create a dp array of 1's with the length of nums
2. Have nested for loops for each element
	2a. On the inner loop go from 0 to i and if nums[j] > nums[i] then we update our dp array
		2ai. This checks if there is a smaller element before this position
	2b. Calculate result
Runtime: O(N^2)
Space: O(N)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        
        res = 0
        # Loop through all elements
        for i in range(len(nums)):
            
            # Start from the beginning and loop up to i
            for j in range(0, i):
                
                # If a number is smaller than the element at i
                if nums[j] < nums[i]:
                    
                    # dp[i] holds the increase dp[j] + 1 and store it in the i pos
                    dp[i] = max(dp[j] + 1, dp[i])
                    
            # update our result
            res = max(res, dp[i])
        return res