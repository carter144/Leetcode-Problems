"""
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

Solution:
1. We use the string split function to split s into an array of words
2. We grab the last index and iterate backwards until we have a valid word
3. We return the length of the index we end up on
Runtime: O(N)
Space: O(N)
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        splitted = s.split(" ")
        
        index = len(splitted) - 1
        
        while splitted[index] == '':
            if index == 0:
                return 0
            index -= 1
        
        return len(splitted[index])