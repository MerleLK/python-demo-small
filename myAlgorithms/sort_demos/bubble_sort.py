"""
@description: 冒泡排序
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-8-14
@detail:
    1．比较相邻的前后二个数据，如果前面数据大于后面的数据，就将二个数据交换。
    2．这样对数组的第0个数据到N-1个数据进行一次遍历后，最大的一个数据就“沉”到数组第N-1个位置。
    3．N=N-1，如果N不为0就重复前面二步，否则排序完成。
"""


def bubble_sort(array):
    length = len(array)
    while length > 0:
        for i in range(length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        length -= 1
    return array


def bubble_sort_better(array):
    """
    设置一个标志，如果这一趟发生了交换，则为true，否则为false。
    明显如果有一趟没有发生交换，说明排序已经完成。
    :param array: 需要排序的数组
    :return:
    """
    length = len(array)
    flag = False
    while length > 0:
        for i in range(length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = True
            else:
                flag = False
        if flag is False:
            return array
        length -= 1
    return array


def bubble_sort_best(array):
    """
    如果有100个数的数组，仅前面10个无序，后面90个都已排好序且都大于前面10个数字，
    那么在第一趟遍历后，最后发生交换的位置必定小于10，且这个位置之后的数据必定已经有序了，
    记录下这位置，第二次只要从数组头部遍历到这个位置就可以了。
    :param array:  需要排序的数组
    :return:
    """
    length = len(array)
    while length > 0:
        for i in range(length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                length = i + 1
        length -= 1
    return array


if __name__ == '__main__':
    my_list = [8, 10, 1, 20, 11, 40, 13, 28, 10, 51, 52, 53, 54, 55]
    # bubble_sort(my_list)
    # bubble_sort_better(my_list)
    bubble_sort_best(my_list)
    print(my_list)
