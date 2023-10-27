from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()

        ans = 0

        for node in range(n):
            if node not in seen:
                seen.add(node)
                ans += 1
                dfs(node)

        return ans