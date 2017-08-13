# coding=utf-8

"""
    This is a link list demo with python
    1.单向链表
"""


# a simple Node for link list
class Node(object):
    def __init__(self, x, nxt):
        self.val = x
        self.next = nxt


# 单向链表
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    # 判空只需要判断指向的下一个节点是否为None
    def is_empty(self):
        return self.head is None

    # 链表首端加入新元素
    def prepend(self, element):
        self.head = Node(element, self.head)

    # 尾端加入新元素
    def append(self, element):
        # 判断是否为空链表, 是就直接添加
        if self.head is None:
            self.head = Node(element, None)
            return

        # 链表不为空, 遍历得到表里最后一个节点, 然后用这个节点的next域记录新结点的链接
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(element, None)

    # 首端弹出元素
    def pop(self):
        if self.head is None:
            raise ValueError
        value = self.head.val
        self.head = self.head.next
        return value

    # 弹出尾端元素
    def pop_last(self):
        # 首先判断是否为空链表
        if self.head is None:
            raise ValueError
        p = self.head
        # 如果链表只有一个元素
        if p.next is None:
            value = p.val
            self.head = None
            return value
        # 遍历链表 直到找到最后一个节点, 将前一个节点的next置为None
        while p.next.next is not None:
            p = p.next
        value = p.next.val
        p.next = None
        return value

    # 查找元素
    def find(self, element):
        p = self.head
        while p is not None:
            if element == p.val:
                return p.next.val
            p = p.next
        return None

    # 打印出所有元素
    def print_all(self):
        p = self.head
        while p is not None:
            print(p.val, end="")
            p = p.next
        print("")


# 带尾结点引用的单链表  尾结点引用--->即指向最后一个节点
# 较之上一个实现, 有效的解决了尾端插入的效率问题
class SinglyLinkedListWithRearReference(SinglyLinkedList):
    def __init__(self):
        SinglyLinkedList.__init__(self)
        self.rear = None

    # 首端加入新元素
    def prepend(self, element):
        # 如果为空列表, 就将将元素置为第一个,并将尾节点引用指向当前节点
        self.head = Node(element, self.head)
        if self.rear is None:
            self.rear = self.head

    # 尾端加入新元素
    def append(self, element):
        if self.head is None:
            # 直接调用首端加入, 对于第一个元素, 加入都是一致的
            self.prepend(element)
        else:
            # 尾端加入新的元素时, 将尾结点引用指向当前新加入的节点
            self.rear.next = Node(element, None)
            self.rear = self.rear.next

    # 从首端删除元素
    def pop(self):
        if self.head is None:
            raise ValueError
        value = self.head.val
        # 如果尾结点引用指向了头结点, 那么说明 当前链表只有一个元素节点, 删除之后需要将尾结点引用置为None
        if self.rear is self.head:
            self.rear = None
        # 将链表的头指向下一个元素节点
        self.head = self.head.next
        return value

    # 从尾端删除元素
    def pop_last(self):
        if self.head is None:
            raise ValueError

        val = self.rear.val
        p = self.head
        while p.next.val != val:
            p = p.next

        p.next = None
        self.rear = p


# 循环单链表  不必要使用单链表为基类
class CircularSinglyLinkedList(object):
    def __init__(self):
        # 表对象只需要一个rear域  ？？
        self.rear = None

    # 判断是否为空
    def is_empty(self):
        return self.rear is None

    # 首端加入新元素
    def prepend(self, element):
        p = Node(element, None)
        # 如果是空链表，就要建立初始的循环链接， 即自己链接自己
        if self.rear is None:
            p.next = p
            self.rear = p
        # 链表不空，就要链接在尾结点之后， 就是首结点
        else:
            p.next = self.rear.next  # 先将原来的首结点链接在自己的后边
            self.rear.next = p  # 自己成为首结点

    # 尾端加入新元素
    def append(self, element):
        # 直接调用之前的加入操作
        self.prepend(element)
        # 将尾节点置换为新加入的结点
        self.rear = self.rear.next

    # 删除首端元素
    def pop(self):
        # 首先判断是否为空列表
        if self.rear is None:
            raise ValueError
        p = self.rear.next
        # 如果尾节点指向自己，说明只有一个结点， 弹出结点之后 将尾节点置空
        if self.rear is p:
            self.rear = None
        # 正常情况下，删除首结点，并将首结点置为原来首结点的下一个
        else:
            self.rear.next = p.next
        return p.val

    # 删除尾端元素
    def pop_last(self):
        # 首先判断是否为空列表
        if self.rear is None:
            raise ValueError
        p = self.rear.next
        if p is self.rear:
            self.rear = None
            return p.val
        while p.next is not self.rear:
            p = p.next
        p.next = self.rear.next
        self.rear = p
        return p.val

    # 遍历所有结点
    def print_all(self):
        p = self.rear.next
        while True:
            print(p.val, end="")
            if p is self.rear:
                print("")
                break
            p = p.next
