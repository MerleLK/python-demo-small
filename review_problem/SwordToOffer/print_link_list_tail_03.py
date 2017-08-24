"""
@description: 从尾部到头部打印链表
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/24 
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def print_list_from_tail_to_head(self, list_node):
        # write code here
        if list_node:
            temp_list = []
            while list_node != None:
                temp_list.append(list_node.val)
                list_node = list_node.next
            # temp_list.reverse()
            temp_list = temp_list[::-1]
            return temp_list
        else:
            return []


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = None
    print(Solution().print_list_from_tail_to_head(l))
    l1 = {}
    print(Solution().print_list_from_tail_to_head(l1))
