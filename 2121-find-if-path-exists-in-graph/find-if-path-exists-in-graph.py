from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}

        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append(v)
            graph[v].append(u)

        visited = [0] * n
        q = deque()
        q.append(source)
        visited[source] = 1

        while q:
            node = q.popleft()
            for x in graph.get(node, []):
                if not visited[x]:
                    q.append(x)
                    visited[x] = 1
            if visited[destination] == 1:
                return True
        return False