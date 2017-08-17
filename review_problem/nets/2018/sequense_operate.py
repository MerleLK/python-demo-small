"""
@description: 操作序列
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-17
@detail:
    小易有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
    1、将a_i放入b序列的末尾
    2、逆置b序列
    小易需要你计算输出操作n次之后的b序列。
"""
import sys


# 内存溢出
def solution(n, array):
    b = []
    for i in array:
        b.append(i)
        b.reverse()
    result = ""
    for i in b:
        result += str(i) + " "
    return result.strip()


def solution2(n, array):
    odd_num = ""
    even_num = ""
    for i in range(n):
        if i % 2 == 0:
            odd_num += str(array[i]) + " "
        else:
            even_num += str(array[i]) + " "
    if n % 2 == 0:
        return even_num[::-1].strip() + " " + odd_num.strip()
    else:
        return odd_num[::-1].strip() + " " + even_num.strip()


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
        print(solution2(num, s))
except:
    pass


# if __name__ == '__main__':
#     import random
#
#     my_list = []
#     num = 1000
#     for _ in range(num):
#         my_list.append(random.randint(10000000, 99999999))
#     print(my_list)
#     print(solution2(num, my_list))
#     print(my_list)
#     print(solution(num, my_list))
