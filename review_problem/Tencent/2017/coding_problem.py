"""
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-8
@description:
    Q:  假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把该编码按字典序排序，形成一个数组如下：
    a, aa, aaa, aaaa, aaab, aaac, … …, b, ba, baa, baaa, baab, baac … …, yyyw, yyyx, yyyy
    其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 编写一个函数，输入是任意一个编码，输出这个编码对应的Index.

    输入描述： 输入一个待编码的字符串 长度小于100
    输出描述： 输出这个编码的index

    ex. input: baca  output: 16331

@detail:
    保存相邻2个同位数编码的距离， 存入一个列表中
    1. aaaa-aaab的距离  存入my_list[3]
    2. aaa-aab的距离  存入my_list[2]
    3. aa-ab的距离  存入my_list[1]
    4. a-b的距离  存入my_list[0]

    从高位一直扫描到低位, 不同位上的距离相加就是结果

    每位上相比的是本位上最初始的字母  也就是a
"""
import sys

# 建立一个列表存储每个位置上的数目
my_list = [1]
for a in range(3):
    my_list.insert(0, 25 * my_list[0] + 1)


def check(string):
    index = 0
    for count, s in enumerate(string):
        index += (ord(s) - ord('a')) * my_list[count] + 1

    return index - 1

# 测试代码
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        print(check(line))
except:
    pass
