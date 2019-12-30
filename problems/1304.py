"""
1304. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]

Solution:
 Add elements to from 1 to n - 1 and then add element (-sum) to the array
 For example : 5
 Add: 1, 2, 3, 4
 Then add: -10
 Runtime: O(N)
 Space: O(N)
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 2:
            return [-1, 1]
        if n == 1:
            return [0]
        if n == 3:
            return [-1, 0, 1]
        res = []
        curr_sum = 0
        for i in range(n - 1):
            res.append(i + 1)
            curr_sum += i + 1
        
        
        res.append(-curr_sum)
        return res
        