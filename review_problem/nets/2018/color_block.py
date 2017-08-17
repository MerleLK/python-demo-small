"""
@description: 彩色方块
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-17
@detail:
    小易有一些彩色的砖块。每种颜色由一个大写字母表示。各个颜色砖块看起来都完全一样。
    现在有一个给定的字符串s,s中每个字符代表小易的某个砖块的颜色。小易想把他所有的砖块排成一行。
    如果最多存在一对不同颜色的相邻砖块,那么这行砖块就很漂亮的。
    请你帮助小易计算有多少种方式将他所有砖块排成漂亮的一行。(如果两种方式所对应的砖块颜色序列是相同的,那么认为这两种方式是一样的。)

    例如: s = "ABAB",那么小易有六种排列的结果:
    "AABB","ABAB","ABBA","BAAB","BABA","BBAA"
    其中只有"AABB"和"BBAA"满足最多只有一对不同颜色的相邻砖块。

"""
import sys


def solution(s):
    char_list = []
    for i in s:
        if i not in char_list:
            char_list.append(i)

    if len(char_list) > 3:
        return 0
    if len(char_list) == 1:
        return 1
    else:
        return 2


try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        print(solution(line))
except:
    pass
