def is_valid_move(cells, row, col, visited):
    if row >= 0 and row < len(cells) and col >= 0 and col < len(cells[0]):
        if cells[row][col] != '#' and not visited[row][col]:
            return True
    return False


def find_shortest_path(cells, start_row, start_col, end_row, end_col):
    visited = [[False for _ in range(len(cells[0]))] for _ in range(len(cells))]
    queue = []
    queue.append((start_row, start_col, 0))
    visited[start_row][start_col] = True
    while queue:
        current_row, current_col, distance = queue.pop(0)
        if current_row == end_row and current_col == end_col:
            return distance
        for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = current_row + row_offset
            new_col = current_col + col_offset
        if is_valid_move(cells, new_row, new_col, visited):
            queue.append((new_row, new_col, distance + 1))
            visited[new_row][new_col] = True

    return -1
    

N, M = map(int, input().split())
maze = []
for _ in range(N):
    row = input().strip()
    maze.append(list(row))
start_row, start_col = None, None
end_row, end_col = None, None

for row in range(N):
    for col in range(M):
        if maze[row][col] == 'E':
            start_row, start_col = row, col
        if maze[row][col] == 'S':
            end_row, end_col = row, col
shortest_path = find_shortest_path(maze, start_row, start_col, end_row, end_col)
print(shortest_path)