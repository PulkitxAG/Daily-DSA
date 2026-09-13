"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clone = {}
        visited = set()
        q = deque()
        q.append(node)
        clone[node] = Node(node.val)
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            for nei in curr.neighbors:
                if nei not in clone:
                    clone[nei] = Node(nei.val)
                clone[curr].neighbors.append(clone[nei])
                if nei not in visited:
                    q.append(nei)
        return clone[node]