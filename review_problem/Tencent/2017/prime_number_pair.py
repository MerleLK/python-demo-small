"""
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-8
@description:
    给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。
    如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10,分别为(5,5),(3,7)）

@detail:
    1.得到给定值之下的所有素数列表
    2.对素数列表进行枚举
    3.去掉左右调换相同的， 但是保留同一个素数出现两次的

"""
import sys
import math


def calc_count(n):
    count = 0
    my_nums = get_all_prime_num(n)
    print(my_nums)
    for i in my_nums:
        if i < (n * 0.5 + 1):
            if is_prime(n - i):
                count += 1
    return count


# 得到给定值之下的所有素数
def get_all_prime_num(n):
    i = 0
    my_prime = []
    while i < n:
        if is_prime(i):
            my_prime.append(i)
        i += 1
    return my_prime


# 判断一个数是不是素数。
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        print(calc_count(int(line)))

except:
    pass
