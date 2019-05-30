"""
28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


Solution:

The most trivial solution is to:
1. Take the first character of the needle: needle[0]
2. Loop through the haystack's characters and check if it is equal to needle[0]
3. Call a seperate function to check if the following letters are equal to the rest of the needle's characters

runtime: O(N^2) since we are comparing the rest of the characters of haystack on each iteration
"""

class Solution:
    
    
    
    def checkRest(self, word1, word2):
        
        
        if len(word2) > len(word1):
            return False
        
        
        
        for i in range(len(word2)):
            
            if word2[i] != word1[i]:
                return False
        return True
            
    
    
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        
        if len(needle) == 0:
            return 0
        
        if len(haystack) == 0:
            return -1
        first_char = needle[0]
        
        for i in range(len(haystack)):
            
            if haystack[i] == first_char:
                if self.checkRest(haystack[i:], needle):
                    return i
        return -1
            
