from typing import List

def is_island(graph, x, y):
    if x == 0:
        if y >= 0 and y <= len(graph[0])-1:
            if graph[x][y] == 1:
                return True
    if x > 0 and x < len(graph)-1 and y >= 0 and y <= len(graph[0]):
        print(x, y)
        if graph[x][y] == 1:
            return True
    return False

def dfs(graph, start):
    visited = set()
    visited.add(start)
    q = []
    q.append(start)
    dist = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    c = 0
    while q:
        print(q, c)
        x, y = q.pop()
        val = graph[x][y]
        for d in dist:
            coord = (x + d[0], y + d[1])
            if is_island(graph, coord[0], coord[1]) and coord not in visited:
                q.append(coord)
                visited.add(coord)
            else:
                if coord not in visited:
                    c += 1
    return c




def find_start(graph):
    for n in range(len(graph)):
        for m in range(len(graph[n])):
            if graph[n][m] == 1:
                return (n, m)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        start = find_start(grid)
        return dfs(graph=grid, start=start)

s = Solution()
print(s.islandPerimeter(grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))