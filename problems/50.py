"""
50. Pow(x, n)


Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Solution:
Have a recursive function
1. Base case: if n == 0; return 1
2. Checks:
	2a. if n < 0: we have a negative exponent, so we divide the answer by 1 and flip the sign
	2b. if n % 2 == 1: if n is odd we pull out an x and multiply it by the answer, subtracting n by 1
	2c. if n is even then, we square x and divide n by two
Solution:
Runtime: O(log N)
Space: O(log N) space for recursive call stacks
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        
        else:
            return self.myPow(x * x, n/2)
