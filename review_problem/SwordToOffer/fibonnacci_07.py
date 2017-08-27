"""
@description: 斐波那次数列
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/27
@detail:
    大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
    [1,1,2,3,5,8,13....]
    n<=39

    方法一、递归
    时间复杂度过高。 计算第39项的值本机竟然跑了30s。
    方法二、迭代，
    每次保留有用的两个数字，即n-1项和n-2项
    节省了大量重复计算的过程。

"""
import datetime


class Solution(object):
    def fibonacci_recursion(self, n):
        if n <= 0:
            return 0
        if n <= 2:
            return 1
        else:
            return self.fibonacci_recursion(n - 1) + self.fibonacci_recursion(n - 2)

    def fibonacci_iter(self, n):
        n1 = n2 = n3 = 1
        if n < 1:
            return 0
        else:
            while n - 2 > 0:
                n3 = n2 + n1
                n1 = n2
                n2 = n3
                n -= 1
        return n3

    def fib(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    num = 39
    s = Solution()
    start = datetime.datetime.now()
    # print(s.fibonacci_recursion(num))
    # print(s.fibonacci_iter(num))
    print(s.fib(num))
    end = datetime.datetime.now()
    print("Cost: {}s".format((end - start).seconds))
