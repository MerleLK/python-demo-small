"""
@description: 通过前序和中序遍历结果求后序
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/24 
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return []
        cur = TreeNode(pre[0])
        index = tin.index(pre[0])
        cur.left = self.reConstructBinaryTree(pre[1: index + 1], tin[:index])
        cur.right = self.reConstructBinaryTree(pre[index + 1:], tin[index + 1:])

        return cur

    def rebuild(self, pre, tin):
        if tin:
            index = tin.index(pre.pop(0))
            root = TreeNode(tin[index])
            root.left = self.rebuild(pre, tin[:index])
            root.right = self.rebuild(pre, tin[index + 1:])

            return root

    def lookup(self, root):
        stack = [root]
        while stack:
            current = stack.pop(0)
            print(current.val, end=',')
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)


if __name__ == '__main__':
    p = "ABDGCEFH"
    p = {1, 2, 4, 7, 3, 5, 6, 8}
    p = [1, 2, 3, 4, 5, 6, 7]
    c = "DGBAECHF"
    c = {4, 7, 2, 1, 5, 3, 8, 6}
    c = [3, 2, 4, 1, 6, 5, 7]
    # t = Solution().reConstructBinaryTree(p, c)
    t = Solution().rebuild(p, c)
    print(t)
    Solution().lookup(t)
