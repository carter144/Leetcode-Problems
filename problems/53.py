"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6

Solution:
1. Have two variables: max_so_far, and max_here set them to the first element
2. Iterate from 1 to the length of the array
3. max_so_far is set to the max(max_so_far + nums[i], nums[i])
	3a. We are choosing to extend the subarray or start a new one.
4. Max_here is recalculated every time.

Runtime: O(N)
Space: O(1)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_so_far = nums[0]
        max_here = nums[0]
        
        
        for i in range(1, len(nums)):
            
            max_so_far = max(max_so_far + nums[i], nums[i])
            max_here = max(max_here, max_so_far)
            
        return max_here