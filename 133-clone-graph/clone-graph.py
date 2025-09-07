"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return None
        
        Tracker = {}

        def dfs(original_node):
            if original_node in Tracker:
                return Tracker[original_node]

            cloned_node = Node(original_node.val)
            Tracker[original_node] = cloned_node
            
            for neighbor in original_node.neighbors:
                cloned_neighbor = dfs(neighbor)
                cloned_node.neighbors.append(cloned_neighbor)

            return cloned_node


        return dfs(node)
        
        