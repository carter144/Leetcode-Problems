"""
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].



Solution: 
Create a hashmap/dictionary to store the difference between the target and nums[i] as the key and index as the value

Loop through the array, for each number in nums take the difference of (target - nums[i]) and place into the hashmap with the index as value
if nums[i] exists in the hashmap then we return the current index we are at along with the index of the corresponding key.

Runtime: O(N) - N is the size of nums
space: O(N) - N is the size of nums
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            else:
                hashmap[difference] = i