s = input()

ans = ""
idx = 0

for i in range(len(s) * 2 - 1):
    if i % 2 == 0:
        ans += s[idx]
        idx += 1
    else:
        ans += "o"

print(ans)
