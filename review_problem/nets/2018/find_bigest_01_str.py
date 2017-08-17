"""
@description:
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-17
@detail:
    如果一个01串任意两个相邻位置的字符都是不一样的,我们就叫这个01串为交错01串。
    例如: "1","10101","0101010"都是交错01串。
    小易现在有一个01串s,小易想找出一个最长的连续子串,并且这个子串是一个交错01串。
    小易需要你帮帮忙求出最长的这样的子串的长度是多少。
"""
import sys


def find_big_sequence(string):
    """
    注意遍历出所有的子串 取最大的那个子串的长度即可
    :param string: 被操作的字符串
    :return:
    """
    count = 1
    big_count = 0
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            count += 1
        else:
            count = 1
        big_count = count if big_count < count else big_count
    return big_count


# try:
#     while True:
#         line = sys.stdin.readline().strip()
#         if line == '':
#             break
#         print(find_big_sequence(line))
# except:
#     pass

if __name__ == '__main__':
    s = "1010101"
    print(find_big_sequence(s))
