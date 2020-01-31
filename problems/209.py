"""
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

Solution:

Have two pointers begin and end
Keep adding the values to a sum variable each time we move end to the right by 1
IF the sum variable is too big we move begin to the right and subtract the values from sum
Then keep track of the minimum distance between begin and end

Runtime: O(N)
Space: O(1)
"""

import sys
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        2,3,1,2,4,3,5,4,7,8,9,10,12,1
                              p
                              q
        """
        
        
        begin = 0
        end = 0
        res = sys.maxsize
        temp_sum = 0
        if s in nums:
            return 1
        
        if len(nums) == 0 or nums is None:
            return 0
        
        while end < len(nums):
            
            if temp_sum < s:
                temp_sum = temp_sum + nums[end]
                end = end + 1
                
            else:
                res = min(res, end - begin)
                temp_sum = temp_sum - nums[begin]
                begin = begin + 1
        
        
        if temp_sum >= s:
            res = min(res, end - begin)
        while begin < len(nums):
            temp_sum = temp_sum - nums[begin]
            begin = begin + 1
            if temp_sum >= s:
                res = min(res, end - begin)
        if res == sys.maxsize:
            return 0
        
        return res
        