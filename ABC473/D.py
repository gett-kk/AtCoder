n, k = map(int, input().split())

stack = [(1, k, [])]

while stack:
    i, rem, cur = stack.pop()

    if i == n:
        if rem % n == 0:
            print(*(cur + [rem // n]))
    else:
        for a in range(rem // i, -1, -1):
            stack.append((i + 1, rem - i * a, cur + [a]))
