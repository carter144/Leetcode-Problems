"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Solution:

We first have to sort the intervals based on the start times.
Then, we utilize a stack to keep track of the intervals.

When we loop through the sorted intervals, we look at 2 elements: the top of the stack and the current interval.

If the element we are at has a start time earlier than the top of the stack: we pop the item and merge the intervals together
Otherwise: we push the current element we are at onto the top of the stack.

Then, we return the stack at the very end 

Runtime: O(N log N) where N is the number of intervals (We have to sort the intervals)
Space: O(N) for the stack
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


    	# Sort based on start times
        k = sorted(intervals, key=lambda x: x[0])
        
        # Initialize the stack
        stack = []
        
        # edge case if the intervals are empty
        if len(intervals) == 0:
            return []
        
        # Insert the first item into the stack
        stack.append(k[0])
        
        
        # Loop through sorted intervals
        for i in range(len(k)):
            top = stack[-1]
            
            
            curr_elem = k[i]
            
            # If the current element's start time is before the stack's end time we need to merge
            if curr_elem[0] <= top[1]:
                temp = stack.pop()
                stack.append([temp[0], max(temp[1], curr_elem[1])])
            # No merging needed
            else:
                stack.append(k[i])
        return stack