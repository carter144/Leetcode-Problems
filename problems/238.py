"""
238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

Solution:
Run through the array and update the result each time we see a number
Run through the array a second time going backwards and update the result each time we see a number
Have a variable to store the current product
Runtime: O(N)
Space: O(1)

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        
        multiplier = 1
        for i in range(len(nums)):
            
            res[i] = multiplier * res[i]
            multiplier = multiplier * nums[i]
        
        
        multiplier = 1
        for j in range(len(nums) -1, -1, -1):
            
            res[j] = multiplier * res[j]
            multiplier = multiplier * nums[j]
            
        return res