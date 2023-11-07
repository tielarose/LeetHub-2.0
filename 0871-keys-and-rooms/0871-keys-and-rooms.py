from collections import defaultdict

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        seen = {0}

        for ind, keys_list in enumerate(rooms):
            graph[ind] = keys_list

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        dfs(0)

        return len(rooms) == len(seen)