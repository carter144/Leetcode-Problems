"""
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

Solution:
We have to keep track of the numbers that are in the current window. We can do this by using a queue. Each time we see a new number, if the amount of elements go above the size, then we need to remove an element from the queue. Each time we remove the element or add an element we have to update the curr_sum.

Solution: O(1)
Space: O(N)
"""

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = size
        self.count = 0
        self.curr_sum = 0
        

    def next(self, val: int) -> float:
        if self.count < self.size:
            self.queue.append(val)
            self.count += 1
            self.curr_sum += val
            return self.curr_sum / self.count
        else:
            t = self.queue.pop(0)
            self.curr_sum -= t
            self.count -= 1
            self.queue.append(val)
            self.curr_sum += val
            self.count += 1
            
            
            return self.curr_sum / self.count

