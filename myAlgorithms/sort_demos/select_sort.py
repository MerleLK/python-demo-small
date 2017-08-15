"""
@description:  选择排序
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-15
@detail:
     1.初始时，数组全为无序区为a[0..n-1]。令i=0
     2.在无序区a[i…n-1]中选取一个最小的元素，将其与a[i]交换。交换之后a[0…i]就形成了一个有序区。
     3.i++并重复第二步直到i==n-1。排序完成。
"""


def select_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


if __name__ == '__main__':
    my_list = [49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    print(select_sort(my_list))
