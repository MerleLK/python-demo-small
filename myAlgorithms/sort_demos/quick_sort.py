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


def quick_sort_nic(array):
    if len(array) <= 1:
        return array
    return quick_sort_nic([x for x in array if x < array[0]]) + [x for x in array if x == array[0]] + quick_sort_nic(
        [x for x in array if x > array[0]])


def quick_sort_simple(array):
    if len(array) <= 1:
        return array
    key = array[0]
    less, greater = [], []
    for i in range(1, len(array)):
        if array[i] > key:
            greater.append(array[i])
        else:
            less.append(array[i])
    return quick_sort_simple(less) + [key] + quick_sort_simple(greater)


# 没有开辟多余空间
def quick_sort(ary):
    return qsort(ary, 0, len(ary) - 1)


def qsort(ary, left, right):
    # 快排函数，ary为待排序数组，left为待排序的左边界，right为右边界
    if left >= right: return ary
    key = ary[left]  # 取最左边的为基准数
    lp = left  # 左指针
    rp = right  # 右指针
    while lp < rp:
        while ary[rp] >= key and lp < rp:
            rp -= 1
        while ary[lp] <= key and lp < rp:
            lp += 1
        ary[lp], ary[rp] = ary[rp], ary[lp]
    ary[left], ary[lp] = ary[lp], ary[left]
    qsort(ary, left, lp - 1)
    qsort(ary, rp + 1, right)
    return ary


if __name__ == '__main__':
    l = [8, 10, 9, 6, 4, 16, 5, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3]
    print(l)
    print(quick_sort_simple(l))
    print(quick_sort_nic(l))
    print(quick_sort(l))
