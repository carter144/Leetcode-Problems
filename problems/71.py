"""
71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

 

Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: "/a/./b/../../c/"
Output: "/c"
Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"

Solution:
1. Split the string on the delimiter '/'
2. Initialize a stack that will hold our results.
3. Loop through the splitted elements
	3a. If the element is empty or the element is ".", then we do nothing and continue
	3b. If the element is ".." we have to move up one so we pop an element off the stack if there are elements
	3c. Otherwise we add the current element to the stack.
4. Return the stack and add "/" in between each element.

Runtime: O(N)
Space: O(N)
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        frags  = path.split("/")
        for frag in frags:
            if frag == "" or frag == ".":
                continue
            elif frag == "..": 
                if len(stack) > 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(frag)
        return "/" + "/".join(stack)