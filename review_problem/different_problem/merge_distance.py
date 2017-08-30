"""
@description: 合并一个二维列表表示的区间
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/30
@detail:
    给出一个二维列表[[1,3],[4,5][3,7]...]
    子列表是前一项小于后一项 标识坐标尺上的距离区间
    就合并交叉区间后的新列表
"""


def merge_array(array):
    if not array:
        return []

    array = sorted(array, key=lambda x: x[0])
    result = []
    item = array[0]

    count = 1
    while count < len(array):
        if item[1] > array[count][0]:  # 比较当前的区间和下一个区下标
            # 如果当前区间完全覆盖下一个区间 直接取当前区间
            if item[1] > array[count][1]:
                item = item
            else:
                item = [item[0], array[count][1]]
        else:
            result.append(item)
            item = array[count]
        count += 1
    result.append(item)
    return result


if __name__ == '__main__':
    arr = [[1, 5], [3, 7], [8, 10], [9, 15], [16, 20], [2, 8]]

    print(merge_array(arr))
