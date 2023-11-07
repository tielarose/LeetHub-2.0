from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()

        def dfs(node):
            if node == destination:
                return True
            
            if node not in seen:
                seen.add(node)
                for neighbor in graph[node]:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)

        