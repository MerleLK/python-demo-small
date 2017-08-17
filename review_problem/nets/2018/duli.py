"""
@description:独立的小易
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-17
@detail:
    小易每天必须吃一个水果并且需要每天支付x元的房屋租金。
    当前小易手中已经有f个水果和d元钱,小易也能去商店购买一些水果,商店每个水果售卖p元。
    小易为了表现他独立生活的能力,希望能独立生活的时间越长越好,小易希望你来帮他计算一下他最多能独立生活多少天。

    输入描述：
        输入包括一行,四个整数x, f, d, p(1 ≤ x,f,d,p ≤ 2 * 10^9),以空格分割
"""
import sys


def day_num(x, f, d, p):
    x = int(x)
    f = int(f)
    d = int(d)
    p = int(p)
    if d < x * f:
        return d // x
    money = d - f * x
    return money // (p + x) + f


try:
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        param = line.split(" ")
        print(day_num(*param))
except:
    pass


# if __name__ == '__main__':
#     print(day_num(3, 5, 100, 10))
