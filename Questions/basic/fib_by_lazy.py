"""
@description: This is a method to impl fib by lazy evaluation.
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-7-19
列出前n项的值
"""
from itertools import islice


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == '__main__':

    print(list(islice(fib(), 10)))
