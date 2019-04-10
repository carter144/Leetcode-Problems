"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

Solution:
We basically need to create an array of strings which will hold the characters that belong to that certain row.  For example rows[1] in the first example will have "APLSIIG" and the second example rows[1] will have "ALSIG". To strategically place each character in s into the correct row, we have to calculate which direction we are currently at and take the modulus of the current index and the number of rows.  We flip directions once the current (index % numRows - 1) == 0
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        rows = [""] * numRows
        
        i = 0
        direction = - 1
        
        for character in s:
            rows[i] = rows[i] + character
            if i % (numRows - 1) == 0:
                direction = direction * -1
            i = (i + direction) % numRows
            
        print(rows[1])
        return ''.join(rows)