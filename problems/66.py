"""
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Solution:
1. Try adding 1 to the last element of the array. If it is less than 10, then we just return the array after adding 1
2. Loop backwards adding 1 to each index of the element of the array
	2a. We have to check if we end up at the beginning of the array, we might have to add 1 to the array itself.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1

        # If the last element is less than 9 we can just add 1 and return
        if digits[n] < 9:
            digits[n] += 1
            return digits
        
        else:
            index = n
            digits[index] = 0
            index -= 1
            
            # If we end up at the beginning of the array we just add 1 and return
            # ex: [9]
            if index < 0:
                digits.insert(0, 1)
                return digits
            
            # while each time we add 1 and it equals to 10 we keep moving backwards
            while digits[index] + 1 == 10:
                if index > 0:
                    digits[index] = 0
                    index -= 1
                # if we end up at the beginning then we just insert 1 and return
                elif index == 0:
                    digits[index] = 0
                    digits.insert(0, 1)
                    return digits
            # If we end up somewhere in the middle of the array we just add 1 and return
            if index >= 0:
                digits[index] += 1
            return digits
            
            
            
            
            
                
        
