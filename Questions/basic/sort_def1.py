# coding=utf-8

"""
    问题：在一行中对给定的任意整数数列， 按如下规则排序：
    1.非负数在前，负数在后
    2.非负数按照从小到大排序
    3.负数部分按照从大到小排序
    如： 数列foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
    排序后： [0, 2, 4, 8, 8, 9, -2, -4, -4, -5, -20]
"""

my_list = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]


def sort_def(x):

    new_list = sorted(x, key=lambda i: (i >= 0 and -abs(1/float(i+1)) or abs(i)))

    return new_list

if __name__ == '__main__':

    print(sort_def(my_list))
