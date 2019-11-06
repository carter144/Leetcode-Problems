"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Solution:
1. Pad the beginning of each string with 0's
2. Add from the right to the left (sum of a[index] + b[index] + carry)
3. At each index we either have a sum of 0, 1, 2, or 3.
4. If the sum is >= 2 then we set the carry to 1
5. Remove padded zeroes at the beginning.
Runtime: O(N)
Space: O(N)
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if len(a) > len(b):
            while len(a) > len(b):
                b = '0' + b
                
        if len(b) > len(a):
            while len(b) > len(a):
                a = '0' + a
        
        a = '0' + a
        b = '0' + b
        index = len(b) - 1
        res = ""
        carry = 0
        tempSum = 0
        while index >= 0:
            tempSum = int(b[index]) + int(a[index]) + carry
            
            if tempSum == 0:
                carry = 0
                res = '0' + res
            if tempSum == 1:
                carry = 0
                res = '1' + res
            if tempSum == 2:
                carry = 1
                res = '0' + res
            if tempSum == 3:
                carry = 1
                res = '1' + res
            index = index - 1
            
        for i in res:
            if i == '0':
                res = res[1:]
            if i == '1':
                break
        if res == "":
            return '0'
        return res