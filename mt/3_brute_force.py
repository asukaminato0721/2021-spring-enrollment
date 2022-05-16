"""
题目描述：
给一个长度为 n 的只包含 0 和 1 的序列，每次可以使用魔法消除相邻的 3 个数。
在可以用任意次魔法的前提下，0 的个数和 1 的个数的最大差值为多少？
输出这个最大差值。
输入描述
第一行是一个正整数 n，表示序列的长度。
第二行是只包含 0 和 1 的序列，其长度为 n。
输出描述
输出一个整数，表示这个最大差值。
样例输入
5
00001
样例输出
3
提示
n≤100000
"""


# AC 91%
n = input()
line = input()
cnt0 = line.count("0")  # On
cnt1 = line.count("1")  # On
dic = {"0": "1", "1": "0"}
if cnt0 < cnt1:
    line = "".join(dic[x] for x in line)  # On
while "111" in line:
    line = line.replace("111", "")
while "110" in line or "011" in line or "101" in line:
    line = line.replace("110", "").replace("011", "").replace("101", "")
print(line.count("0") - line.count("1"))
