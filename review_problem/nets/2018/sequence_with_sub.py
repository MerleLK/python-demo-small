"""
@description: 等差数列
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-17
@detail:
    如果一个数列S满足对于所有的合法的i,都有S[i + 1] = S[i] + d, 这里的d也可以是负数和零,我们就称数列S为等差数列。
    小易现在有一个长度为n的数列x,小易想把x变为一个等差数列。小易允许在数列上做交换任意两个位置的数值的操作,并且交换操作允许交换多次。
    但是有些数列通过交换还是不能变成等差数列,小易需要判别一个数列是否能通过交换操作变成等差数列?
"""
import sys


def check_sequence(n, array):
    if n < 2:
        return "Possible"
    array = sort(array)
    val = array[1] - array[0]
    for i in range(n - 1):
        if array[i + 1] - array[i] != val:
            return "Impossible"
    return "Possible"


def sort(array):
    if len(array) <= 1:
        return array
    mid = key = array[0]
    less = []
    biger = []
    for i in range(1, len(array)):
        if array[i] > key:
            biger.append(array[i])
        else:
            less.append(array[i])
    return sort(less) + [mid] + sort(biger)

try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        num = int(line)
        line2 = sys.stdin.readline().strip()
        if line == '':
            break
        s = [int(x) for x in line2.split(" ")]
        print(check_sequence(num, s))
except:
    pass
