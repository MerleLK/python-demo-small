# coding=utf-8

"""
    一、邻接列表及其相似结构
    1.邻接集表示法
    1.当图的结构十分密集,
"""
a, b, c, d, e, f, g, h = range(8)
N1 = [
    {b, c, d, e, f},
    {c, e},
    {d},
    {e},
    {f},
    {c, g, h},
    {f, h},
    {f, g}
]

print(b in N1[a])
print(len(N1[f]))

"""
    2.邻接列表表示法
    1.可以支持低成本下对图N(v)中所有的节点进行有效遍历
    2.其在检查u,v是否互为邻居的成本为O(N(v))
"""
N2 = [
    [b, c, d, e, f],
    [c, e],
    [d],
    [e],
    [f],
    [c, g, h],
    [f, h],
    [f, g]
]

"""
    3.加权邻接字典表示法
    1. 加上了边的权重
"""

N3 = [
    {b: 2, c: 1, d: 3, e: 9, f: 4},
    {c: 4, e: 3},
    {d: 8},
    {e: 7},
    {f: 5},
    {c: 2, g: 2, h: 2},
    {f: 1, h: 6},
    {f: 9, g: 8}
]
print(b in N3[a])
print(len(N3[f]))
print(N3[a][b])  # 获取权值

"""
    4.邻接集的字典表示法  
"""

N4 = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}

print(N4['a'])
print(N4)

"""
    二、邻接矩阵
    1.使用嵌套list实现邻接矩阵
"""

#    a  b  c  d  e  f  g  h
N5 = [
    [0, 1, 1, 1, 1, 1, 0, 0],  # a
    [0, 0, 1, 0, 1, 0, 0, 0],  # b
    [0, 0, 0, 1, 0, 0, 0, 0],  # c
    [0, 0, 0, 0, 1, 0, 0, 0],  # d
    [0, 0, 0, 0, 0, 1, 0, 0],  # e
    [0, 0, 1, 0, 0, 0, 1, 1],  # f
    [0, 0, 0, 0, 0, 1, 0, 1],  # g
    [0, 0, 0, 0, 0, 1, 1, 0],  # h
]

print(N5[a][b])
print(sum(N5[f]))

"""
    2.对不存在的边赋予无限大权值的加权矩阵
"""

inf = float('inf')
#    a  b  c  d  e  f  g    h
W = [
    [0, 2, 1, 3, 9, 4, inf, inf],  # a
    [inf, 0, 4, inf, 3, inf, inf, inf],  # b
    [inf, inf, 0, 8, inf, inf, inf, inf],  # b
    [inf, inf, inf, 0, 7, inf, inf, inf],  # c
    [inf, inf, inf, inf, 0, 5, inf, inf],  # d
    [inf, inf, inf, inf, inf, inf, inf, inf],  # e
    [inf, inf, inf, inf, inf, 0, 2, 2],  # f
    [inf, inf, inf, inf, inf, 1, 0, 6],  # g
    [inf, inf, inf, inf, inf, 9, 8, 0],  # h
]

print(W[a][b] < inf)
print(W[c][e] < inf)
print(sum(1 for w in W[a] if w < inf) - 1)  # Degree
