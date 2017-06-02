# coding=utf-8

"""
    问题：
    将一个数字旋转180°， 判断是否还是一个数字 是就打印
    eg： 123 --- false    169 --- 961
"""


def palindrome(x):

    my_dict = {1: 1, 6: 9, 8: 8, 9: 9}
    new_int = ''
    for i in range(len(str(x))):
        remainder = x % 10
        if remainder in [2, 3, 4, 5, 7]:
            return False
        new_int += str(my_dict.get(remainder))
        x = x // 10
    return int(new_int)


if __name__ == '__main__':

    num = 1681618
    print(palindrome(num))
