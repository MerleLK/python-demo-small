"""
@description: 寻找缺失的整数
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-9
"""


def check(my_list):
    my_dict = {}
    for i in range(100):
        my_dict.update({i + 1: 0})

    for i in my_list:
        my_dict[i] = 1

    for i in range(100):
        if my_dict[i + 1] == 0:
            return i + 1


def sort_check(my_list):
    my_list.sort()
    if 1 not in my_list:
        return 1
    if 100 not in my_list:
        return 100
    for i in range(len(my_list) - 1):
        if my_list[i + 1] - my_list[i] != 1:
            return my_list[i] + 1


def simple_check(my_list):
    result = sum([i + 1 for i in range(100)])

    for i in my_list:
        result -= i
    return result


# problem 扩展
def check_one_num(my_list):
    result = 0
    for i in my_list:
        result ^= i
    return result


def check_two_num(my_list):
    result = 0
    num1 = 0
    num2 = 0
    for i in my_list:
        result ^= i
    tail = str(bin(result)).rindex('1')
    flag = str(bin(result))[tail:]
    for i in my_list:
        if str(bin(i)).endswith(flag):
            num1 ^= i
        else:
            num2 ^= i
    return num1, num2


if __name__ == '__main__':
    origin_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                   53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                   78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
         59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
         87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    d2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
          30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
          57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
          84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1, 2, 3, 4, 6, 7, 9, 10, 11, 12,
          13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
          30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
          57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
          84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    # check(d)
    # print(sort_check(d))
    # print(simple_check(d))
    # print(check_two_num(d2))
