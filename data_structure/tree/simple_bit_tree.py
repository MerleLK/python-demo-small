"""
@description: 二叉树的实现
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 2017-08-22
"""


# 二叉树节点
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 定义一个二叉树
tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))


# 层次遍历
def lookup(root):
    stack = [root]
    while stack:
        current = stack.pop(0)
        print(current.data, end=",")
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    print()


def deep(root):
    if not root:
        return
    print(root.data, end=",")
    deep(root.left)
    deep(root.right)


def mid(root):
    if not root:
        return
    mid(root.left)
    print(root.data, end=",")
    mid(root.right)


def back(root):
    if not root:
        return
    back(root.left)
    back(root.right)
    print(root.data, end=",")


# 递归
def max_depth(root):
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p and q:
        return p.data == q.data and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False


if __name__ == '__main__':
    # lookup(tree)
    # deep(tree)
    # mid(tree)
    # back(tree)
    # print(max_depth(tree))
    tree2 = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    print(is_same_tree(tree, tree2))
