"""
@description: 双核CPU问题
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/25 
"""
import sys


def divide_list(array):
    array = sorted(array, reverse=True)
    time_long_1 = array.pop(0)
    time_long_2 = array.pop(0)

    for i in array:
        if time_long_1 < time_long_2:
            time_long_1 += i
        else:
            time_long_2 += i

    return time_long_1 if time_long_1 > time_long_2 else time_long_2


def long_time(n, array):
    if n < 1:
        return -1
    elif n == 1:
        return array[0]
    elif n == 2:
        return array[0] if array[0] > array[1] else array[1]
    else:
        return divide_list(array)


try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        line2 = sys.stdin.readline().strip()
        if line2 == '':
            break
        num = int(line)
        arr = line2.split(" ")
        arr = [int(x) for x in arr]
        print(long_time(num, arr))
except:
    pass

# if __name__ == '__main__':
#     num = 5
#     arr = [3072, 3072, 7168, 3072, 1024]
#     num = 1
#     arr = [1024]
#     print(long_time(num, arr))
