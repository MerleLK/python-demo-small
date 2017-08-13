"""
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-8
@description:
    geohash编码：geohash常用于将二维的经纬度转换为字符串，分为两步：第一步是经纬度的二进制编码，第二步是base32转码。
    此题考察纬度的二进制编码：算法对纬度[-90, 90]通过二分法进行无限逼近（取决于所需精度，本题精度为6）。
    注意，本题进行二分法逼近过程中只采用向下取整来进行二分，针对二分中间值属于右区间。
    算法举例如下： 针对纬度为80进行二进制编码过程：
    1) 区间[-90, 90]进行二分为[-90, 0),[0, 90]，成为左右区间，可以确定80为右区间，标记为1；
    2) 针对上一步的右区间[0, 90]进行二分为[0, 45),[45, 90]，可以确定80是右区间，标记为1；
    3) 针对[45, 90]进行二分为[45, 67),[67,90],可以确定80为右区间，标记为1；
    4) 针对[67,90]进行二分为[67, 78),[78,90]，可以确定80为右区间，标记为1；
    5) 针对[78, 90]进行二分为[78, 84),[84, 90]，可以确定80为左区间，标记为0；
    6) 针对[78, 84)进行二分为[78, 81), [81, 84)，可以确定80为左区间，标记为0；

    ex. input 80   output: 111100

"""
import sys
import math


def get_encode(n):
    result = ''
    left = -90
    right = 90
    while len(result) <= 5:
        mid_temp = (left + right) / 2
        if mid_temp > 0:
            mid = math.floor(mid_temp)
        else:
            mid = math.ceil(mid_temp)
        if n >= mid:
            left = mid
            result += '1'
        else:
            right = mid
            result += '0'
    return result


try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        print(get_encode(int(line)))

except:
    pass
