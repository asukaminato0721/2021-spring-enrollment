"""
//3
小 A 的公司，在发放年终奖，有 n 个礼品盒。每个礼品盒都有一个重量 w 。
规则是这样的，小 A 可以从 n 个礼品盒拿任意多个礼品盒。
但是必须满足这些拿走的礼品盒中没有两个礼品盒的重量差值为 1 。
小 A 希望可以拿走尽量多的礼品盒，你帮他计算一下最多可以拿走多少礼品盒。
5
2 2 2 1 3

3

2
1 2

1
"""

"""
20%
"""
n = int(input())
from collections import Counter

he = sorted(map(int, input().split()))
cnt = sorted(Counter(he).items(), key=lambda x: x[0])
dp = [1] * (n + 1)
dp[0] = 1
for i in range(1, n):
    if he[i] - he[i - 1] != 1:
        ...
print(1)