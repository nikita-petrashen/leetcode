def check_land(i, j, grid, m, n):
    if not (0 <= i < m) or not (0 <= j < n):
        return 0
    else:
        return int(grid[i][j])


def wasnt_visited(i, j, grid, m, n):
    if not (0 <= i < m) or not (0 <= j < n):
        return 1

    if grid[i][j] == -1:
        return 0
    else:
        return 1


def mark_visited(i, j, grid, m, n):
    if (0 <= i < m) and (0 <= j < n):
        grid[i][j] = -1


def visit_island(i, j, grid, m, n):
    is_land = check_land(i, j, grid, m, n)
    mark_visited(i, j, grid, m, n)
    if is_land:
        if wasnt_visited(i + 1, j, grid, m, n):
            visit_island(i + 1, j, grid, m, n)
        if wasnt_visited(i - 1, j, grid, m, n):
            visit_island(i - 1, j, grid, m, n)
        if wasnt_visited(i, j + 1, grid, m, n):
            visit_island(i, j + 1, grid, m, n)
        if wasnt_visited(i, j - 1, grid, m, n):
            visit_island(i, j - 1, grid, m, n)

    return is_land


class Solution:
    def numIslands(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if wasnt_visited(i, j, grid, m, n):
                    num_islands += visit_island(i, j, grid, m, n)

        return num_islands


if __name__ == '__main__':
    sol = Solution()
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(sol.numIslands(grid1))
    grid2 = grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
    ]
    print(sol.numIslands(grid2))
