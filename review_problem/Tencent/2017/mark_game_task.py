"""
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-8
@description:
    游戏里面有很多各式各样的任务，其中有一种任务玩家只能做一次，这类任务一共有1024个，任务ID范围[1,1024]。
    请用32个unsigned int类型来记录着1024个任务是否已经完成。初始状态都是未完成。
    输入两个参数，都是任务ID，需要设置第一个ID的任务为已经完成；并检查第二个ID的任务是否已经完成。
    输出一个参数，如果第二个ID的任务已经完成输出1，如果未完成输出0。
    如果第一或第二个ID不在[1,1024]范围，则输出-1。

@detail:
    利用位图的原理可以很简单的解决这个问题：
    生成一个 1024长度的数组 每个位上用 0 ，1表示任务是否完成

"""
import sys

bit = [0] * 1024


def check_finish(a, b):
    if a > 1024 or a < 0 or b > 1024 or b < 0:
        return -1
    bit[a - 1] = 1
    return bit[b - 1]


try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print(check_finish(int(lines[0]), int(lines[1])))

except:
    pass
