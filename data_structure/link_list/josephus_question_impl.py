"""
@description: 经典问题 Josephus问题
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-2
@detail: 问题描述：
    设有n个人围坐一圈，现在从第k个人开始报数，报到第m的人退出。
    然后继续报数，直至所有人退出。输出出列人顺序编号。
"""
from data_structure.link_list.singly_linked_list import CircularSinglyLinkedList


# 基于list和固定大小的数组
def josephus_list(n, k, m):
    """
    1.建立一个包含n个人（编号）的list
    2.找到k个人， 从那里开始
        处理过程中，把对应的表元素修改为0表示人已经退出
    3.反复操作：
        数m个（在席）人
        把表示第m个人的元素修改为0
    Tips: 数到list最后元素之后转到下标为0的元素继续
    :param n: 列表的长度
    :param k: 开始位置
    :param m: 退出条件
    :return: 无
    """
    people = list(range(1, n + 1))
    print(people)

    i = k - 1  # 开始位置的下标
    for num in range(n):
        count = 0  # 报数编号
        # 一次循环最多到m， 此时就会把最后一个人踢出
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")
                people[i] = 0
            i = (i + 1) % n  # 遍历到最后一个位置就会从首位再次开始
        print("," if num < n - 1 else "\n", end="")


def josephus_list_pop(n, k, m):
    """
    1.算出应该退出的元素之后, 将其从表中删除
    2.直至表长度为0的时候结束
    复杂度： O(n^2)
    :param n: 列表的长度
    :param k: 开始位置
    :param m: 退出条件
    :return: 无
    """
    people = list(range(1, n + 1))
    i = k - 1
    for num in range(n, 0, -1):
        i = (i + int(m) - 1) % num
        print(people.pop(i), end="")
        print("," if num > 1 else "\n", end="")


class JosephusLinkedList(CircularSinglyLinkedList):
    """
    1.从形式看，循环单链表很好地表现了围坐一圈的人
    2.顺序的数人头，很好的符合了循环表中沿着next链扫描
    3.某人退出之后，删除相应结点，之后可以继续沿着原来的方向数人头

    算法复杂度 O(m*n)
    """

    def __init__(self, n, k, m):
        CircularSinglyLinkedList.__init__(self)
        # 创建包含n个元素的循环链表
        for i in range(n):
            self.append(i + 1)
        # 将初始结点移动到k处
        self.turn(k - 1)

        # 循环弹出第m个元素直到链表为空
        while not self.is_empty():
            self.turn(m - 1)
            print(self.pop(), end="")
            print("," if self.rear is not None else "\n", end="")

    # 将循环表对象的rear指针沿着next移动了m步
    def turn(self, m):
        for i in range(m):
            self.rear = self.rear.next


if __name__ == '__main__':
    josephus_list(10, 2, 7)
    josephus_list_pop(10, 2, 7)
    JosephusLinkedList(10, 2, 7)
