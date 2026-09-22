class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        visited = {}
        def clone(node):
            if node in visited:
                return visited[node]
            new_node = Node(node.val)
            visited[node] = new_node
            for neighbros in node.neighbors:
                new_node.neighbors.append(clone(neighbros))
            return new_node
        return clone(node)