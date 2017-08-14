"""
@description: 快速排序
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-11
@detail:
    1.先从数组中取出一个数作为基准数
    2.按照基准数将数组分为两部分， 比之大的放在左边，比之小的放在右边
    3.再对左右区间重复第二步。
    4.直至各区间只有一个数
"""


def py_quick_sort(array):
    if len(array) <= 1:
        return array
    return py_quick_sort([x for x in array if x < array[0]]) + [x for x in array if x == array[0]] + py_quick_sort(
        [x for x in array if x > array[0]])


def q(array):
    if len(array) <= 1:
        return array
    key = array[0]
    less, greater = [], []
    for i in range(1, len(array)):
        if array[i] > key:
            greater.append(array[i])
        else:
            less.append(array[i])
    return q(less) + [key] + q(greater)


if __name__ == '__main__':
    l = [8, 10, 9, 6, 4, 16, 5, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3]
    print(l)
    print(q(l))
    print(py_quick_sort(l))

