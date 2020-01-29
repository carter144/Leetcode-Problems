"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

Solution:
Have a check to make sure the two strings are the same length.
They should also be the same length when the duplicate characters are removed.
Have a hash map that maps characters from s to characters in t
On each iteration make sure that the characters from s don't map to a different character.

Runtime: O(N)
Space: O(N)
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_table = {}
        
        
        if len(s) != len(t):
            return False
        
        
        if len(set(s)) != len(set(t)):
            return False
        for i in range(len(s)):
            curr_character = s[i]
            
            
            
            if curr_character not in hash_table:
                hash_table[curr_character] = t[i]
            else:
                mapped_character = hash_table[curr_character]
                
                if mapped_character != t[i]:
                    return False
        return True
            