"""
@description: 二叉树
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-11
"""

# 二叉树的 list实现

empty_tree = []
simple_tree = ['A', ['B', ['c', 'd', []], []], []]


def bi_tree_list(root, left, right):
    return [root, left, right]


def is_empty_list(bit_tree):
    return bit_tree == []


def left_ch(bi_tree):
    return bi_tree[1]


def right_ch(bi_tree):
    return bi_tree[2]


class BiTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def is_empty(self):
        pass

    def is_full(self):
        pass
