n, k = map(int, input().split())
a = list(map(int, input().split()))

MOD = 998244353

fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD

inv = [1] * (n + 1)
inv[n] = pow(fact[n], MOD - 2, MOD)
for i in range(n - 1, -1, -1):
    inv[i] = inv[i + 1] * (i + 1) % MOD

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD

s1 = sum(a) % MOD
s2 = sum(x * x % MOD for x in a) % MOD

ans = comb(n - 1, k - 1) * s2 % MOD

if k >= 2:
    ans += comb(n - 2, k - 2) * (s1 * s1 - s2) % MOD
    ans %= MOD

print(ans)
