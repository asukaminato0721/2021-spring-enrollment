"""
小 A 在玩一款游戏。这游戏有一个副本。有 n * m 个房间，如下图。每个房间都有一只怪。每只怪都有一个攻击力。只有主角的攻击力大于怪的攻击力，才能进入这个房间。 副本的入口是左上房间。出口在右下房间。每个房间都只能往右走或者往下走。问主角至少需要多少攻击力才能通关。
"""


n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(m):
    dp[0][i] = max(room[0][: i + 1]) + 1
第一列 = next(zip(*room))
for i in range(n):
    dp[i][0] = max(第一列[: i + 1]) + 1
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = min(
            max(dp[i - 1][j], room[i][j] + 1), max(dp[i][j - 1], room[i][j] + 1)
        )
print(dp[n - 1][m - 1])
