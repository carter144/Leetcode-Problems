"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Solution:
Dynamic programming: Create a dp array length of the string and place -1 in all the slots.
Have a recursive helper method that has the base cases:
	if index >= len(s): return 1
	if dp[index] > -1: return dp[index]

other wise make a variable called ways
check if index + 1 is in bounds and if the character is valid then we set ways += recursive call incrementing index by 1.
Do the same for two characters and then set dp[index] = ways
return dp[index]


Runtime: O(N)
Space: O(N)
"""
class Solution:
    
    def isValid(self, s):
        if len(s) == 0:
            return False
        
        if s[0] == '0':
            return False
        
        val = int(s)
        return val >= 1 and val <= 26
            
    
    
    def helper(self, s, index, dp):
        if index >= len(s):
            return 1
        
        if dp[index] > -1:
            return dp[index]
        
        
        ways = 0
        if index + 1 <= len(s):
            # single character decode
            first = s[index:index + 1]
            if self.isValid(first):
                ways += self.helper(s, index + 1, dp)
        
        if index + 2 <= len(s):
            # double character decode
            second = s[index: index + 2]
            if self.isValid(second):
                ways += self.helper(s, index + 2, dp)
        
        dp[index] = ways
        return dp[index]
        
        
    
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        return self.helper(s, 0, dp)