"""
516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".



Solution:
Use dynamic programming with a 2D array of size n*n.
We will fill out only half of the 2D array of a digonal and up.

Start off by filling the diagonal with 1's. Each letter is a palindrome

Have an outer for loop for gap length:
This will look at 2 characters at a time, then 3 characters at a time then 4 characters
at a time and so on.

Have an inner for loop that loops to the end of the array minus gap length to prevent OOB

A second pointer j is used as the end of the current_gap length: als end of sliding window

We have two conditions:
    1. s[i] == s[j]:
        1a. dp[i][j] = dp[i + 1][j - 1] + 2
        2b. We take the bottom left corner and add two to increase the length
    2. s[i] != s[j]:
        2a. dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        2b. Take the max of left element, or bottom element
return dp[0][n - 1]
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # create our dp 2d array
        dp = dp = [[0 for x in range(n)] for y in range(n)]

        i = 0
        j = 0
        # Fill diagonal with 1's
        while i < len(s):
            dp[i][j] = 1
            i += 1
            j += 1
        
        # start gap length with 2 and increase by 1 each time
        for gap_length in range(2, len(s) + 1):

            # i is the start and loops until n - gap_length to prevent oob
            for i in range(n - gap_length + 1):

                # j is the end of the sliding window
                j = i + gap_length-1
            
                # the two characters are equal
                if s[i] == s[j]:
                    # take the bottom left and add two
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # the two characters are not equal
                    # take the max of the left, or bottom element
                    dp[i][j] = max(dp[i][j - 1], dp[i+1][j])
        
        return dp[0][n - 1]
    
    
        