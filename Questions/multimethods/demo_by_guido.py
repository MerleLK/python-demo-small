"""
@description: This is the demo for guido
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-8
"""


def foo(a, b):
    if isinstance(a, int) and isinstance(b, int):
        print(a + b)
    elif isinstance(a, float) and isinstance(b, float):
        print("float")
    elif isinstance(a, str) and isinstance(b, str):
        print("str")
    else:
        raise TypeError("Unsupported types{0},{1}".format(type(a), type(b)))


if __name__ == '__main__':
    foo(1.5, 1.5)
