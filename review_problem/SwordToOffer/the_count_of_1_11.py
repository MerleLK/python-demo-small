"""
@description: 一个整数的二进制数中的1的个数。
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/27
@detail:
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

    循环比较法: 依次与1相与的方法

    eg. 5->101   101 & 001 -> 001!=0 count+1
    将101 向右移一位 编程

    快速比较法: 1的个数有多少，就比较多少次

    eg. 14->1110, 13->1101,   14&13 -> 1100
    此时我们经过这次运算之后，消去了14的最低位的1，计数+1.
    持续运算，我们一直消去最低位的1， 持续计数，即可得到结果。

"""


def cmp_count(n):
    count = 0
    if n < 0:
        n &= 0xffffffff
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count


def count_num(n):
    count = 0
    if n < 0:
        n &= 0xffffffff
    while n:
        count += 1
        n &= n - 1
    return count


if __name__ == '__main__':
    num = -18
    print(count_num(num))
    print(cmp_count(num))
