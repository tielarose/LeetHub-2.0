from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        original_edges = set()
        seen = {0}

        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            original_edges.add((x,y))

        def dfs(node):
            edges_changed = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in original_edges:
                        edges_changed += 1
                    seen.add(neighbor)
                    edges_changed += dfs(neighbor)
            return edges_changed

        return dfs(0)
        
