"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

Solution:

For this problem, I took a brute force approach and it was accepted.  The idea here is to have a loop that starts from the beginning of the string and have another loop at i + 1 to check if it is a palindrome.  Then we retrieve the longest palindrome computed from the two loops and return it.
Runtime O(N^3)
"""

class Solution:
    
    
    def isPalindrome(self, s):
        return s == s[::-1]
    
    def longestPalindrome(self, s: 'str') -> 'str':
        
        if len(s) == 0 or s is None:
            return ""
        if self.isPalindrome(s):
            return s
        
        
        
        n = len(s)
        subseq = ""
        left = 0
        while left < n:
            right = left + 1
            while right <= n:
                substr = s[left:right]
                if self.isPalindrome(substr) and len(substr) > len(subseq):
                    subseq = substr 
                right += 1
            left += 1
        return subseq