"""
@description: some method about the prime number
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-8
"""
import math
from itertools import count

"""
    Part one: 检查某个数是否为素数 
"""


# method one : 使用数学函数
def is_prime_by_math(n):
    # 对于小于或等于1的数，抛弃
    if n <= 1:
        return False
    # 遍历从2-n/2区间的数 如果出现整除 就返回False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        return True


# method two : 使用itertools模块
def is_prime_by_iter(n):
    # 对于小于或等于1的数，抛弃
    if n <= 1:
        return False

    for i in count(2):
        # 结束条件
        if i * i > n:
            return True
        if n % i == 0:
            return False


# method3： 不使用内置模块
def is_prime_no_module(n):
    # 对于小于或等于1的数，抛弃
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# 一种高效率的实现方法
def is_prime_num(n):
    # 对于小于或等于1的数，抛弃
    if n <= 1:
        return False
    # 2 是素数
    if n == 2:
        return True
    # 偶数都不是素数
    if n % 2 == 0:
        return False

    # 对剩下的奇数进行判断
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        return True


"""
    Part two: 得到某区域内的素数
"""

# 使用列表推导式

N = 100
prime_numbers = [p for p in range(2, N) if 0 not in [p % d for d in range(2, int(math.sqrt(p)) + 1)]]
print(prime_numbers)

if __name__ == '__main__':
    print(is_prime_by_math(5))
    print(is_prime_by_iter(5))
