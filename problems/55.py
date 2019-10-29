"""
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.

Solution:
Loop through all the elements of the array,

Once we find an element equal to 0:
	We check if max_index <= current_index and current_index < len(nums) - 1
	If the max_index is smaller and we are not at the end of the array:
	We will return false
If the current element is not 0 then we update our max_index to the max of
current max_index or nums[i] + index

return true at the end of the loop
Runtime: O(N)
Space: O(1)

"""
class Solution:       
    def canJump(self, nums: List[int]) -> bool:
        
        max_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                
                if max_index <= i and i < len(nums) - 1:
                    return False
            else:
                max_index = max(max_index, nums[i] + i)
        return True