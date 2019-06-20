"""
39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

Solution:
A brute force way to solve this problem is to just try every single possibility.
On each recursive call we have the following 3 options:
1. Take the current element and stay on the current element
2. Not take the current element and move onto the next
3. Take the current and move onto the next element

We will simulate the 3 options with recursive dfs
"""


class Solution:
    
    def __init__(self):
        self.res = []
    def helper(self, nums, index, target, temp_array):
        if index >= len(nums):
            return
        
        if target < 0:
            return
        if nums[index] == target:
            temp_array.append(nums[index])
            self.res.append(temp_array)
            return
        
        
        self.helper(nums, index, target - nums[index], temp_array + [nums[index]])
        self.helper(nums, index + 1, target - nums[index], temp_array + [nums[index]])
        self.helper(nums, index + 1, target,temp_array)
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        
        
            
        index = 0
        
        self.helper(sorted(candidates), index, target, [])
        b = []
        
        for sublist in self.res:
            if sublist not in b:
                b.append(sublist)
        print(self.res)
        
        
        return b