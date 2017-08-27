"""
@description: 青蛙跳台阶问题。
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/27
@detail:
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

    其实就是一个斐波那次数列 求第n项

    详细见代码 07

"""


class Solution(object):
    def fib(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    num = 39
    s = Solution()
    print(s.fib(num))
