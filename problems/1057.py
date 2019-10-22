"""
1057. Campus Bikes

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation: 
Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].

Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: [0,2,1]
Explanation: 
Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].

Solution:

1. Create a nested for loop of workers on the outer loop and bikes on the inner loop.
2. Calculate the distances or each worker, bike pair and store them into a hash_map.
3. The hash_map's keys will be distances and values will be arrays of pairs of worker, bike indexes
4. Iterate through the hash_map's keys (distances) in increasing order
5. Greedily try to assign the bike to the worker if they are both available.

Runtime O(M*N) where M is the length of the workers array and N is the length of the bikes array
Space is O(M*N) since we will have to store all the pairs into a hash_map as values
"""

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # create a result array size of workers
        res = [-1] * len(workers)
        
        # create an array of booleans to track which bike has been used
        used_bikes = [False] * len(bikes)
        
        # initialize a hash map
        hash_map = {}
        # this will store distance as key, and a list of [worker, bike] pairs as values
        # for example:
        # hash_map = {
        #    1: [[4, 3], [1, 0]],
        #    2: [[3, 1], [4, 2]]
        # }
        #
        #
        for i in range(len(workers)):
            worker = workers[i]
            
            for j in range(len(bikes)):
                bike = bikes[j]
                
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                
                if distance not in hash_map:
                    hash_map[distance] = []
                    
                    hash_map[distance].append([i, j])
                    
                else:
                    
                    hash_map[distance].append([i, j])
                    
        # we need to loop through the keys from the smallest distance first
        # this way we don't need to sort the dictionaries keys
        for j in range(2001):
            
            # if the current number we are on is a distance,
            if j in hash_map:
                current_distance = hash_map[j]

                # we loop through each pair and greedily choose the first available pair to assign
                for pair in current_distance:
                    worker = pair[0]
                    bike = pair[1]
                    
                    # check if the worker hasn't already been assigned and the bike hasn't already been assigned
                    if res[worker] == -1 and used_bikes[bike] == False:
                        res[worker] = bike
                        used_bikes[bike] = True
                    
        return res