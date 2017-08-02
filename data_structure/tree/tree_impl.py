"""
@description: this is the different impl for tree
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017-07-31
"""

# 1. a simple tree structure
T = [["a", "b"], ["c"], ["d", ["e", "f"]]]

print(T[0][1])
print(T[2][1][0])


# 2. binary tree class
class BinaryTree(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right


t = BinaryTree(BinaryTree("a", "b"), BinaryTree("c", "d"))
print(t.right.left)


# 3.multiple way tree 多路搜索树
class MultiWayTree(object):
    def __init__(self, kids, _next=None):
        self.kids = self.val = kids
        self.next = _next


t2 = MultiWayTree(MultiWayTree("a", MultiWayTree("b", MultiWayTree("c", MultiWayTree("d")))))
print(t2.kids.next.next.val)

