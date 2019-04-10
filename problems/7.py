"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


Solution:

This is really easy if we are able to convert this into a string and reverse the string.  First we need to check if x is a negative number, if it is then we multiply it by -1 to make it positive.  Then we set a flag k to -1 to remember that we have to turn the reversed integer to negative.  Next we convert the integer to a string and reverse it and multply by k if it is negative.  We also have to check if it is a valid integer in between 2147483647 or -2147483648. If it is not valid we return 0.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        k = 1
        if (x < 0):
            k = -1
            x = x * -1
        if x == 0:
            return 0
        
        temp = str(x)
        res = int(temp[::-1]) * k
        
        if res >= 2147483647 or res <= -2147483648:
            return 0
        return res
        
        