"""
@description: 找到优雅的点
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-9
@detail:
    已知： 圆的半径的平方
    得到圆上所有横纵坐标为整数的个数和。
    ex. 半径平方为25
    优雅的点就有 ： +-（3，4） +-（4， 3） （0， +-5）， （+-5， 0）
"""

import math

import sys


def check_point(x, y):
    if str(x).isdigit() and (str(y).endswith(".0") or str(y).isdigit()):
        return True
    return False


def calc(n):
    count = 0
    for x in range(int(math.sqrt(n)) + 1):
        y = math.sqrt(n - x * x)
        if check_point(x, y) and x != 0:
            print(x, y)
            count += 1
    return count * 4


try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        print(calc(int(line)))

except:
    pass

if __name__ == '__main__':
    num = 25
    c = calc(num)
    print(c)
