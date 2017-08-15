"""
@description: 希尔排序
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-15
@detail:
    先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序，
    然后依次缩减增量再进行排序，(一般缩减1/2)
    待整个序列中的元素基本有序（增量足够小）时，
    再对全体元素进行一次直接插入排序。
    因为直接插入排序在元素基本有序的情况下（接近最好情况），效率是很高的，因此希尔排序在时间效率上比前两种方法有较大提高。
"""


def shell_sort(array, n):
    step = 2
    now_gap = n // step
    while now_gap > 0:
        for i in range(now_gap, n):

            temp = array[i]
            j = i
            while j >= now_gap and array[j - now_gap] > temp:
                array[j] = array[j - now_gap]
                j = j - now_gap
            array[j] = temp
        now_gap //= step
    return array


def shell_sort1(array):
    length = len(array)
    step = 3
    group_num = length // step
    while group_num > 0:
        for i in range(0, group_num):
            j = i + group_num
            while i < length:
                k = j - group_num
                key = array[j]
                while k >= 0:
                    if array[k] > key:
                        array[k + group_num] = array[k]
                        array[k] = key
                    k -= group_num
                j += group_num
        group_num //= step
    return array


if __name__ == '__main__':
    # my_list = [49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    my_list = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    # num = len(my_list)
    # hill_sort(my_list, num)
    # print(shell_sort(my_list))
    print(shell_sort(my_list, len(my_list)))
