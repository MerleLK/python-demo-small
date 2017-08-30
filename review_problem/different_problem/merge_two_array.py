"""
@description: 合并两个列表
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/30
@detail:
    存在两个已经排序的列表
    按照顺序合并两个列表
    eg. [2,4,6,8]
        [1,3,5,7]
    return [1,2,3,4,5,6,7,8]
"""


def merge_array(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1

    count1 = 0
    count2 = 0
    result = []

    while count1 < len(arr1) and count2 < len(arr2):
        if arr1[count1] > arr2[count2]:
            result.append(arr2[count2])
            count2 += 1
        else:
            result.append(arr1[count1])
            count1 += 1

    result += arr1[count1:]
    result += arr2[count2:]

    return result


if __name__ == '__main__':
    a = [2, 4, 6, 8]
    b = [1, 3, 5, 7, 9]

    print(merge_array(a, b))
