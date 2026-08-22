from collections import deque

h, w, k = map(int, input().split())
grid = []

for _ in range(h):
    grid.append(list(input()))

row_bombs = [0] * h
col_bombs = [0] * w

for r in range(h):
    for c in range(w):
        if grid[r][c] == '#':
            row_bombs[r] = 1
            col_bombs[c] = 1

dist = [[-1] * w for _ in range(h)]
dq = deque()

for r in range(h):
    for c in range(w):
        if grid[r][c] == '.' and not(row_bombs[r] or col_bombs[c]):
            dist[r][c] = 0
            dq.append((r, c))

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while dq:
    r, c = dq.popleft()

    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if (
            (0 <= nr < h and 0 <= nc < w) and
            (grid[nr][nc] == "." and dist[nr][nc] == -1)
        ):
            dist[nr][nc] = dist[r][c] + 1
            dq.append((nr, nc))

ans = 0
for r in range(h):
    for c in range(w):
        if (
            grid[r][c] == "." and
            (dist[r][c] != -1 and dist[r][c] <= k)
        ):
            ans += 1

print(ans)
