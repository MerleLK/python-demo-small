# coding=utf-8

"""
    问题： 求斐波那契数列第n项的值
"""


def fib(number):

    if number <= 1:
        return number
    else:
        return fib(number - 1) + fib(number - 2)

if __name__ == '__main__':

    n = 5
    print(fib(n))
