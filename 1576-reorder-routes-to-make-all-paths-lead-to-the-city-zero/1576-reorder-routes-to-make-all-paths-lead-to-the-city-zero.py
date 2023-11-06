from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
        seen = {0}

        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x,y))

        def dfs(node):
            ans = 0

            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        ans += 1
                    seen.add(neighbor)
                    ans += dfs(neighbor)

            return ans

        return dfs(0)


        