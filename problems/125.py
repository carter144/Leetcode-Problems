"""

125. Valid Palindrome


Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

Solution:
Use regular expression to remove white spaces and other characters that aren't alphanumeric
Check if the reversed is equal to the current.
Runtime: O(N)
Space: O(1)
"""
import re
import re, string; 

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        if len(s) == 1:
            return True
        l = re.sub(r'\W+', '', s)
        return l.lower() == l.lower()[::-1]