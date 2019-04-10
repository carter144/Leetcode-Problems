"""
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

Solution:
The easy way is to convert the integer to a string and check if the reversed string is equal to the original string.  Another way is to only check half of the digits from x.  We do so by modding x by 10 to get the digit and multiplying by 10.  Then we will know that we have checked half the digits once x is < reverseNum.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        
        
        reverseNum = 0
        
        
        while x > reverseNum:
            reverseNum = reverseNum * 10 + x % 10
            x = x // 10
            
        
        if x == reverseNum or x == reverseNum // 10:
            return True
        else:
            return False