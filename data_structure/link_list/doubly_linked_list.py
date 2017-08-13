"""
@description: This the doubly linked list impl
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-8-2
"""
from data_structure.link_list.singly_linked_list import Node, SinglyLinkedListWithRearReference


class DoubleNode(Node):
    def __init__(self, prev, value, nxt):
        Node.__init__(self, value, nxt)  # 继承单链表的初始结点
        self.prev = prev  # 前结点


class DoublyLinkedList(SinglyLinkedListWithRearReference):
    # 继承带尾结点引用的单链表基础上实现双链表， 非变动的操作均可以直接复用
    def __init__(self):
        SinglyLinkedListWithRearReference.__init__(self)

    # 前端插入元素
    def prepend(self, element):
        # 前端插入元素时，变成首位元素， 前结点为None， 尾结点为原链表的首位
        p = DoubleNode(Node, element, self.head)
        self.head = p  # 将链表的首位置为自己
        if self.rear is None:  # 如果尾结点为None, 就说明没有尾结点，则尾结点指向自己
            self.rear = p
        else:
            # 正常的链表，就将下一个结点的前结点指向自己
            p.next.prev = p

    # 尾端插入结点
    def append(self, element):
        # 尾端插入元素时，前结点为原链表尾结点， 新的尾结点为None
        p = DoubleNode(self.rear, element, None)
        self.rear = p  # 将尾结点置为自己
        if self.head is None:  # 如果首结点不存在，那么就将自己作为首结点
            self.head = p
        else:
            # 将前一个结点的尾结点指向自己
            p.prev.next = p

    # 首端删除元素
    def pop(self):
        # 判断是否为空
        if self.head is None:
            raise ValueError
        e = self.head.val
        # 删除当前的首结点
        self.head = self.head.next
        # 如果删除后链表为空，就把rear也置为None
        if self.head is None:
            self.rear = None
        # 首结点的前结点置为None
        else:
            self.head.prev = None
        return e

    # 尾端删除元素
    def pop_last(self):
        # 判断是否为空
        if self.head is None:
            raise ValueError
        e = self.rear.val
        # 将尾结点置为原尾结点的前结点
        self.rear = self.rear.prev
        # 删除尾结点之后, 链表为空， 就把head也置为None
        if self.rear is None:
            self.head = None
        # 将链表的尾结点置为None
        else:
            self.rear.next = None
        return e
