"""
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

Solution:
Perform a binary search
1. Start left = 2 and right = x // 2 
2. calculate the mid point and square it
3. if mid*mid is too big move right to mid - 1
4. if mid*mid is too small move left to mid + 1
return right

Runtime: O(log N)
Space: O(1)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if (x < 2):
            return x
        
        left = 2
        right = x // 2
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if mid * mid == x:
                return mid
            
            elif mid*mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right