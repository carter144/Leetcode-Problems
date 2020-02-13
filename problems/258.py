"""
258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Solution:

We know the answer must be between 0-9
If the number is 0 then we return 0
If the number % 9 ==0 we return 9
otherwise we return number % 9
Runtime: O(1)
Space: O(1)
"""

class Solution:
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9