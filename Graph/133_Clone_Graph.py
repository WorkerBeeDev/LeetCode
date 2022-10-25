"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
 
    visited = {}


    def cloneGraph(self, node: 'Node') -> 'Node':

        # not node return NULL
        if not node:
            return node

        # to avoid cycle
        if node in self.visited:
            return self.visited[node]

        # clone node has empty neighbors
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node


        if node.neighbors:
            clone_node.neighbors = [ self.cloneGraph(n) for n in node.neighbors ] 

        return clone_node
