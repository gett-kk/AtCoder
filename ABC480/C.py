n, k, t = map(int, input().split())
a = sorted(map(int, input().split()))  # 昇順の入力だと思っていたが、何もソートされていなかった...

now = 0
cnt = 0 if a and a[0] == 0 else 1

for x in a:
    if x > t:
        break
    cnt += max(0, (x - now - 1) // k)
    now = x

cnt += max(0, (t - now - 1) // k)
print(cnt)
