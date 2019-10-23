"""
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Solution:
(Backtracking)
1. Initialize a boolean array that is initially set to False
2. Write the recursive function to simulate taking an element and removing it.
	2a. Base case: when the permutation length is equal to the length of nums
	2b. Loop through index of nums and check if the number is being used or not (bool_array)
	2c. If the number is used, continue on. If it is not, set the position of bool_array[i] to True and add the number to the temporary permutation variable
	2d. Recursive call
	2e. After the recursive call, remove the last element and reset the bool_array[i] to False to simulate not using the number anymore
O(N!) runtime since we are generating all permutations

"""

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # bool array to keep track of what number is being used
        bool_array = [False] * len(nums)

        # temporary permutation array that will store auxillary results
        permutation = []
        res = []
        
        # recursive function
        def helper(nums, permutation, bool_array):

        	# BASE CASE when the permutation and nums length are equal add to result array and return
            if len(permutation) == len(nums):
                temp = []
                for elem in permutation:
                    temp.append(elem)
                
                res.append(temp)
                return

            # Loop through each number in nums
            for i in range(len(nums)):

            	# If the current number is being used then continue searching
                if bool_array[i] == True:
                    continue

                # Set the current number to being used
                bool_array[i] = True

                # add the number to temporary premutation array
                permutation.append(nums[i])

                # Recursive call
                helper(nums, permutation, bool_array)

                # remove the last element
                del permutation[-1]

                # reset the bool array so that we aren't using it anymore
                bool_array[i] = False
        
        # recursive call from the main function
        helper(nums, permutation, bool_array)
        
        return res