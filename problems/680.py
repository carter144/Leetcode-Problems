"""
680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Solution:
Have a two pointer approach. (Left and right)
Move inwards until s[left] != s[right]
Once we have a mismatch, check if there is a palindrome if we delete the left letter.
Check if there is a palindrome if the delete the right letter.
If either is true, we return true, false otherwise

If we make it to the middle then the whole string is a palindrome and we return true.
Runtime: O(N)
Space: O(1)
"""
class Solution:
    
    
    def isPalindrome(self, s):
        
        return s[::-1] == s
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        
        
        
        
        low = 0
        high = len(s) - 1
        
        temp_list = list(s)
        
        
        while low <= high:
            
            if temp_list[low] != temp_list[high]:
                return self.isPalindrome(temp_list[:low] + temp_list[(low + 1):]) or self.isPalindrome(temp_list[:high] + temp_list[(high + 1):])
            low = low + 1
            high = high - 1
        return True