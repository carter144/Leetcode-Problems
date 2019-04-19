"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

Solution:
This is one of the more straight forward problems where we just validate whether or not the input string is balanced.
The solution is to use a stack to store the opening parentheses such as: ( { [
Then every time we see a closing parentheses: ) } ] we have to pop the stack and see if the item we popped matches with the current one. If the stack is empty when we attempt to pop, then it is not valid.

Then at the very end we check if the stack is empty or not.  If the stack is empty then we know it is valid.
O(N) runtime
O(N) space
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.insert(0, i)
            
            if i == ')':
                #todo
                if len(stack) == 0:
                    return False
                if '(' != stack.pop(0):
                    
                    return False
            
            
            if i == '}':
                #todo
                if len(stack) == 0:
                    return False
                if '{' != stack.pop(0):
                    return False
            
            if i == ']':
                #todo
                if len(stack) == 0:
                    return False
                if '[' != stack.pop(0):
                    return False
            
        return len(stack) == 0