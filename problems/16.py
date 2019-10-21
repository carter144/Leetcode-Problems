"""
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Solution:
1. Start with the first 3 numbers as the result.
2. Sort the numbers in nums
3. At each index of the sorted array perform a two sum problem to calculate current_sum
4. Update the result at each iteration if there is a new answer
O(N^2) since we are looping through each element followed by a search from the next element to the end of the array.
O(1) space since we are not using extra space. O(N) if we consider the result array
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

    	# the result will be originally the first three numbers
        res = nums[0] + nums[1] + nums[2]
        
        # sort the numbers in nums similar
        k = sorted(nums)
        
        # we loop through each index of the sorted array
        for i in range(len(k)):

        	# perform a two sum search problem by:

        	# 1. setting left to the next element
            left = i + 1

            # 2. setting right to the end of the array
            right = len(k) - 1
            
            
            
            while left < right:

            	# calculate the current_sum of the three elements
                current_sum = k[left] + k[right] + k[i]
                
                # if the current_sum is too big we move right to the left by one
                if current_sum > target:
                    right -= 1
                # if the current_sum is too small we move left to the right by one
                else:
                    left += 1
                
                # update our result by calculating the distance by taking absolute difference values 
                if abs(current_sum - target) < abs(res - target):
                    res = current_sum
        return res
                
                