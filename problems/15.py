"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Solution:
1. sort the array of nums
2. loop through each element and perform a two sum search: for i in range(len(nums)):
	2a. start the left pointer at i + 1
	2b. start the right pointer at len(nums) - 1
	2c. if elements at nums[i] + nums[left] + nums[right] == 0 add to result array
	2d. if elements at nums[i] + nums[left] + nums[right] > 0 move right to the left by one 
	2e. if elements at nums[i] + nums[left] + nums[right] < 0 move left to the right by one
O(N^2) since we are looping through each element followed by a search from the next element to the end of the array.
O(1) space since we are not using extra space. O(N) if we consider the result array
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

    	# sort the numbers in nums
        k = sorted(nums)

        # create an empty array to store our result
        res = []

        # create a set to see which elements we already visited
        temp_set = set()

        # loop through every element in the sorted array
        for i in range(len(k)):
            
            curr_elem = k[i]
            
            # if we already have this element in the visited set we continue
            if curr_elem in temp_set:
                continue

            # we do a two sum problem here by setting the left(begin) pointer to the next element
            begin = i + 1

            # right pointer(end) to the end of the array
            end = len(nums) - 1
            
            while begin < end:

            	# if the current elem + left elem + right elem == 0
                if curr_elem + k[begin] + k[end] == 0:
                	# add it to the result set
                    res.append([curr_elem, k[begin], k[end]])
                    # add it to the visited set
                    temp_set.add(curr_elem)

                    # temporary variables to store so we don't have duplicates
                    begin_elem = k[begin]
                    end_elem = k[end]
                    # increment begin variable until we get a new number
                    while begin < end and k[begin] == begin_elem:
                        begin += 1
                    # decrement end variable until we a get a new number
                    while begin < end and k[end] == end_elem:
                        end -= 1
                        
                # if our sum is too big we have to move left one
                elif curr_elem + k[begin] + k[end] > 0:
                    end = end - 1
                # if our sum is too small we have to move right one
                elif curr_elem + k[begin] + k[end] < 0:
                    begin = begin + 1

        return res
            