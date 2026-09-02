import collections

n = int(input())
c = list(map(int, input().split()))

cnt = collections.Counter(c)

print(sum(sorted(list(cnt.values()), reverse=True)[1:]))
