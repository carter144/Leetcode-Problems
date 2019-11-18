"""
78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Solution:
Perform a DFS recursively. At each call we have two choices, to skip the current element or take the current element to the current result

The base case is when we have the index >= length of the array
Runtime: O(2^N)
Space: O(2^N)
"""
class Solution:
    
    
    def helper(self, nums, index, current, result):
        
        # base case
        if index >= len(nums):
            result.append(current)
            return
        
        # skip the current number
        self.helper(nums, index + 1, current, result)

        #take the current number
        self.helper(nums, index + 1, current + [nums[index]], result)
        
        
    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        self.helper(nums, 0, [], res)

        return res