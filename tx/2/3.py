"""
牛牛家有一个大花园，花园里有一棵大树，因为牛牛很喜欢二叉树，因此这棵树也便长成了二叉树的样子， 
牛牛认为，一颗二叉树是完美的，当且仅当这棵二叉树是一棵完全二叉树； 
牛牛想让它的花园里的大树是完美的，因此他决定对大树进行若干次修剪，即删去一些点，使得这棵大树变成一个 “完美的二叉树”， 
同时牛牛也想让这棵树尽量的大，它想知道最终这棵树最终长什么样。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 你需要返回一个指针，指向root，表示删减去若干个点后，剩下的树
# @param root TreeNode类 指向二叉树的根
# @return TreeNode类
#
from collections import deque


class Solution:
    def solve(self, root: TreeNode):
        # write code here
        # 拿深度
        q = deque([root])
        cnt = 0
        flag = True
        while q and flag:
            cnt += 1
            for i in range(len(q)):
                tmp = q.pop()
                if not tmp:
                    flag = False
                    break
                q.append(tmp.left)
                q.append(tmp.right)
        qq = deque([root])
        cnt -= 1
        while cnt:
            t = len(qq)
            for i in range(t):
                tmp = qq.pop()
                if tmp.left:
                    qq.append(tmp.left)
                if tmp.right:
                    qq.append(tmp.right)
            cnt -= 1
        while qq:
            tmp = qq.pop()
            tmp.left = None
            tmp.right = None
        return root

# 写吐都没写出来，边界难解决
