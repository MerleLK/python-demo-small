"""
@description:  归并排序
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-15
@detail:
    1. 合并
    2. 分解
"""


def merge_array(array1, array2):
    left_index = right_index = 0
    result = []
    # 循环比较两个数组，知道某个数组为空
    while len(array1) > left_index and len(array2) > right_index:
        if array1[left_index] < array2[right_index]:
            result.append(array1[left_index])
            left_index += 1
        else:
            result.append(array2[right_index])
            right_index += 1
    # 将不为空数组剩下的数字依次加入到结果列表中。另一个是空列表，所以可以这样实现。
    result += array1[left_index:]
    result += array2[right_index:]
    return result


def divide_array(array):
    # 结束条件
    if len(array) <= 1:
        return array

    index = len(array) // 2

    left = divide_array(array[:index])  # 左半部分
    right = divide_array(array[index:])  # 右半部分

    return merge_array(left, right)


if __name__ == '__main__':
    my_list = [49, 38, 65, 97, 26, 13, 27, 49, 55, 4]

    print(divide_array(my_list))
