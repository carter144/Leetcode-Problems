"""
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

Solution:
Simply iterate through the array and have a hash map or dictionary that has the element has keys and the frequency as values

In example 1 we would have:
{
	3: 2
	2: 1
}

In example 2:
{
	2: 4
	1: 3
}

THen iterate through the hash map and find the maximum value and return that key.

Runtime: O(N)
Space: O(N)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hash_map = {}
        for key in nums:
            if key not in hash_map:
                hash_map[key] = 1
                
            else:
                hash_map[key] += 1
        
        
        curr_max = 0
        curr_res = None
        for key in hash_map.keys():
            
            if hash_map[key] > curr_max:
                curr_max = hash_map[key]
                curr_res = key
            
        return curr_res