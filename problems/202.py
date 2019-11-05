"""
202. Happy Number


Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Solution:
Have a while loop: while n != 1:
If the while loop exists and break, we return true
Inside the while loop update n to be the sum of the digits squared
Check if n has already been seen by a set(). If it is in the set already then we return false.

Runtime: O(N)
Space: O(N)
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            seen.add(n)
            temp = str(n)
            new_sum = 0
            for num in temp:
                new_sum += int(num) * int(num)
            n = new_sum
            if n in seen:
                return False
        return True