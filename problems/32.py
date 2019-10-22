"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

Solution:
1. Create a loop going from 0 to len(s)
	1a. Keep track of counts of the left and right brackets
	1b. If left == right: calculate result
	1c. if right >= left: reset left and right to 0
2. Create a loop going from len(s) - 1 to -1:
	2a. Keep track of counts of the left and right brackets
	2b. If left == right: calculate result
	2c. If left >= right: reset left and right to 0

Runtime: O(N)
Space: O(1)
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        left = 0
        right = 0
        
        res = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                res = max(res, left + right)
            elif right >= left:
                right = 0
                left = 0
        left = 0
        right = 0
        for j in range(len(s) - 1, -1, -1):
            if s[j] == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                res = max(res, left + right)
            elif left >= right:
                left = 0
                right = 0
        return res