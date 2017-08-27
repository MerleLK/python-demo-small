"""
@description: 矩形覆盖
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/27
@detail:
    我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形.
    请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

    是斐波那次数列的变形。

    假如我们对2*n的覆盖方法记F(n). 如果横着放， 那么在左上角和左下都必须横着放置两个， 剩下2*(n-2)格子，就是f(n-2)
    竖着放置，那么剩下就是2*(n-1)格子，所以就是f(n-1)
    那么此时的总的方法就是f(n-1)+f(n-2),就是斐波那次数列。
"""


class Solution(object):
    def rect_cover(self, number):
        if number <= 0:
            return 0
        a, b = 0, 1
        for _ in range(number):
            a, b = b, a + b
        return b
