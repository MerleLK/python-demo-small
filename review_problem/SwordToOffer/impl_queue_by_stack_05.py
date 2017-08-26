"""
@description: 使用两个栈实现一个队列，完成队列的Push和Pop操作， 队列中的元素为int类型
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/25 
"""


class Solution(object):
    def __init__(self):
        self.in_stack = []  # 进入元素的列表
        self.out_stack = []  # 弹出元素的列表

    def push(self, node):
        """
        add node to queue.
        :param node: the node to add
        :return: the queue added the element
        """
        self.in_stack.append(node)

    def pop(self):
        """
        :return: xx the number del
        """
        if not self.out_stack:
            if self.in_stack:
                for i in range(len(self.in_stack)):
                    self.out_stack.append(self.in_stack.pop())
            else:
                return None
        return self.out_stack.pop()

if __name__ == '__main__':

    s = Solution()
    s.push(1)
    s.push(2)
    print(s.in_stack)
    print(s.pop())
