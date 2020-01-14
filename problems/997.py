"""
997. Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N

Solution:
Create an array of length N + 1 that stores the amount of people that trusts a particular candidate at that index in the array
Loop through the trust list and whenever we see a person being "trusted" we increment the index of the candidates array by 1 to show that this person has 1 person that trusts them. 
We also keep a set of trusters so we can check at the end if a candidate has trusted another person.

The judge will have candidates[i] = 1 and is not in the trusters set
If we didn't return anything then there is no judge so we return -1

Runtime: O(N)
Space: O(N)
"""
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        candidates = [0] * (N + 1)
        
        trusters = set()
        
        for elem in trust:
            start = elem[0]
            trusters.add(start)
            end = elem[1]
            
            candidates[end] -= 1
            
        
        for i in range(1, len(candidates)):
            if candidates[i] == 1 and i not in trusters:
                return i
        
        
        return -1