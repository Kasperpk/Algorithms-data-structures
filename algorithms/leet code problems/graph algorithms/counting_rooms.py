from collections import deque

def counting_rooms(grid):
    rooms = 0
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    def bfs(start):
        queue = deque([start])
        visited[start[0]][start[1]] = True
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '.' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and not visited[r][c]:
                bfs((r, c))
                rooms += 1
    return rooms

if __name__ == '__main__':
    n,m = map(int, input().split())
    graph = [input() for _ in range(n)]
    result = counting_rooms(graph)
    print(result)
