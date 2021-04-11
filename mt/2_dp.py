from collections import Counter

n, m = map(int, input().split())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))
cnta = Counter(an)
cntb = Counter(bn)
dp = [float("-inf")] * 1002
dp[1] = sum(2 if bi > 1 else 1 for bi in bn) - sum(
    2 if ai > 1 else 1 for ai in an
)
for i in range(2, 1001):
    dp[i] = dp[i - 1] - cntb[i] + cnta[i]

print(max(dp))
