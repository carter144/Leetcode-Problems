"""
133. Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 
Solution:
1. Initialize a hash_map
2. Initialize a queue and add the first element to the queue.
3. BFS with a queue, at each node: loop through the neighbors and see if it already exists in the hash_map.
	3a. If the neighbor DOES NOT exists in the hash_map create it in the hash_map and add to queue
4. add the neighbor to the current node's neighbors

Runtime: O(N)
Space: O(N)
"""

    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # initialize a hash map
        hash_map = {}
        
        if node is None:
            return None
        
        # BFS with a queue
        queue = []
        queue.append(node)
        
        # Initialize the first entry point node
        hash_map[node] = Node(node.val, [])
        
        
        while len(queue) > 0:
            curr = queue.pop(0)
            
            # for each neighbor
            for neighbor in curr.neighbors:
                
                # check if the neighbor already exists, if not create one
                if neighbor not in hash_map:
                    # add the neighbor to the hash_map
                    hash_map[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                
                # add the neighbor to the current nodes neighbors
                hash_map[curr].neighbors.append(hash_map[neighbor])
        return hash_map[node]
                
        