"""
@description: 变态跳台阶问题
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/27
@detail:

    一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
    求该青蛙跳上一个n级的台阶总共有多少种跳法。

    解法:
        我们根据数学归纳法可以得到
        F(n)=2^(n-1)
"""
import datetime


class Solution(object):
    def bt_fib(self, n):

        if n < 2:
            return n
        else:
            return 2 * self.bt_fib(n - 1)


if __name__ == '__main__':
    num = 39
    start = datetime.datetime.now()
    s = Solution()
    print(s.bt_fib(num))
    end = datetime.datetime.now()
    print("Cost: {}s".format((end - start).seconds))
