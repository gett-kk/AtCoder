n, m = map(int, input().split())

ans = [m // n] * n
ans[: m % n] = [x + 1 for x in ans[: m % n]]

print(*ans, sep="\n")
