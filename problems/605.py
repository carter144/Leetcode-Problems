"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.

Solution:

To solve this, we just need to loop through all the elements of the flowerbed and check if we are able to plant a flower there.
We are able to plant a flower there if both sides of the position are equal to 0.  We are also able to plant if there is only one zero
for the end and beginning of the array.

Runtime: O(N) we need to loop through every element of flowerbed. N is the size of the flowerbed.
Space: O(1) We are not using an extra space.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0
        
        
        for i in range(len(flowerbed)):
            
            if (flowerbed[i] == 0) and (i == 0 or flowerbed[i - 1] == 0 ) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
            
            
        return count >= n