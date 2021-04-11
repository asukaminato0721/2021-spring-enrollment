# 小美和小团居住的城市有 n 座房子呈一条直线排列，相邻两房子间隔相同，
# 第 i 座房子编号为 i. 小美知道小团的房子可能在某些房子中，
# 他想买一套房子使得距离小团可能所在房子的期望距离尽可能小，同时又不超过 k 元钱，于是向你求助.
# 输入描述
# 第一行 2 个正整数 n,k 如上文所述.
# 第二行n个整数,a1,...,an，分别为第i座房子的价格,若价格为0表示小美可能在这一房子中,
# 且此座房子不可购买.小美出现在所有可能房子中的概率相同。
# 2≤n≤100,0≤ai,k≤100
# 输出描述
# 输出一个正整数，表示小团需购买的房间的编号。
# 数据保证至少有一间房间是小美可能居住的地方且至少有一间房间小团可购买
n, k = map(int, input().split())
fz = list(map(int, input().split()))
zero_pos = [x for x, y in enumerate(fz, 1) if y == 0]
ans = min(
    (x for x, y in enumerate(fz, 1) if y != 0 and y <= k),
    key=lambda x: sum(abs(x - k) for k in zero_pos),
)
print(ans)
# 样例输入
# 5 3
# 4 5 0 3 3
# 样例输出
# 4