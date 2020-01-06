"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Solution:
We need to keep track of the current_max product and the current_min product.
The current_min will be used to multiply negative numbers together to get a larger positive number.
Runtime: O(N)
Space: O(1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        current_min = nums[0]
        current_max = nums[0]
        res = nums[0]
        
        
        for i in range(1, len(nums)):
            temp = current_max
            
            current_max = max(nums[i], max(current_max * nums[i], current_min * nums[i]))
            
            current_min = min(nums[i], min(temp * nums[i], current_min * nums[i]))
            res = max(res, current_max)
        return res