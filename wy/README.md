# 网易笔试

由同学口述

一棵二叉树
叶节点称作樱桃
叶节点相连的称为柄节点
一个柄节点如果带有一个樱桃，卖 2 元
如果带有 2 个樱桃，卖 5 元
给一个二叉树
返回卖多少钱

层序/也许后序遍历

---

给一个数组，里面有各个城市的距离
然后返回最适合作为物流中心的城市
这个城市到其他所有城市的距离和最小
list【list】
每个内层 list 是 3 元组
city1，city2，distance
一开始给的距离不是两个城市的最小距离
只是直接的距离
也可能有城市不能和其他相连

dijkstra

---

一个 string 和一个 char 数组
求最长的包含偶数个 char 数组中字符的连续的子字符串

---

一棵二叉树
每个节点有一个数字
给一个数组
从根节点到叶节点，里面包含这个数组
这样的一条路径称作有效路径
求最长的最靠左的有效路径
包含数组要按顺序
返回数组

---

问答 1：shared_ptr 的实现原理

2：new 和 malloc 的区别