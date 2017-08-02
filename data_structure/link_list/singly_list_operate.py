"""
@description: 一些基于单链表的操作
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-2
@detail:
    对于链表修改表元素的顺序可以采用两种方法：
    1.结点间搬运元素，   ----对于单链表，此方法效率低下，且麻烦
    2.修改链接关系
"""

from data_structure.link_list.singly_linked_list import SinglyLinkedList


# 反序链表
def reverse_by_singly(my_list):
    """
    使用修改链接关系：
    1如果一直向首端添加结点，最先进去的就会在尾结点
    2一直从首端取元素，最后得到的时尾结点。
    这样就可以实现反转算法了
    :param my_list: 被操作的链表
    :return: 无
    """

    p = None
    while my_list.head is not None:
        q = my_list.head
        my_list.head = q.next
        q.next = p
        p = q
    my_list.head = p


# 基于移动元素的单链表排序
def sort_linked_list_by_move_value(my_list):
    """
    为了有效实现，算法只能从头到尾方向检查和处理。
    每次拿出一个元素，在已排序的序列中找到正确位置插入
    :param my_list: 被操作的链表
    :return: 无
    """

    if my_list.head is None:
        return
    crt = my_list.head.next  # 计算从首结点之后开始，即首结点已排序完毕
    while crt is not None:
        x = crt.val
        p = my_list.head
        # 从原链表的首结点开始进行比较，存在如下情况
        # 1. 当前结点的值大于已排序完毕的结点，跳过
        while p is not crt and p.val <= x:
            p = p.next
        # 2. 当前结点的值小于已排序完毕的结点， 交换元素位置
        while p is not crt:
            x, p.val = p.val, x
            p = p.next
        crt.val = x
        crt = crt.next


# 基于调整链接关系实现排序工作
def sort_linked_list_by_change_relation(my_list):
    """
    基本处理模式与移动元素类似.
    但是这里不在结点之间移动表元素，而是把被处理的结点取下来接到正确的位置上。
    :param my_list: 被操作的链表
    :return: 无
    """
    # 判断链表是否为空
    if my_list.head is None:
        return
    # 初始 已排序的段只有一个结点
    last = my_list.head  # 表示已排序段的尾结点
    crt = last.next      # 待排序段的首结点
    # 顺序链表的结点，每次处理一个结点
    while crt is not None:
        # 设置扫描指针的初始值
        p = my_list.head  # 已排序，并且比较完毕的段
        q = None  # 已排序但为比较完毕的段
        while p is not crt and p.val <= crt.val:
            # 顺序更新两个扫描指针
            q = p
            p = p.next
        # 当 p 是 crt 时 不需要修改链接，设置last到下一个结点crt
        if p is crt:
            last = crt
        else:
            # 取出当前结点
            last.next = crt.next
            # 接好后置链接
            crt.next = p
            if q is None:
                # 作为新的首结点
                my_list.head = crt
            else:
                # 接在表中间
                q.next = crt
        # crt 指向last的下一个结点
        crt = last.next


if __name__ == '__main__':
    s = SinglyLinkedList()
    s.append(5)
    s.append(2)
    s.append(4)
    s.append(3)
    s.append(1)

    # reverse_by_singly(s)
    sort_linked_list_by_change_relation(s)
    s.print_all()
