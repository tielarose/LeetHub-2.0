from collections import defaultdict

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(row, col):
            return (0 <= row < height) and (0 <= col < width) and (grid[row][col] == "1")

        def dfs(row, col):
            for x, y in directions:
                new_row, new_col = y + row, x + col
                if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)
        
        width = len(grid[0])
        height = len(grid)
        seen = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        num_islands = 0

        for i in range(height):
            for j in range(width):
                if int(grid[i][j]) and ((i, j) not in seen):
                    num_islands += 1
                    seen.add((i, j))
                    dfs(i, j)

        return num_islands
        