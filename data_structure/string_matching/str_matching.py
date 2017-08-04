"""
@description: This some algorithms for string matching
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-3
"""


# 串匹配朴素算法
def simple_matching(t, p):
    """
    效率很低， 但易理解， 复杂度时O（m*n）.
    遇字符不等时将模式串 p 右移一个字符，再次从 p0（重置 j = 0 后）开始比较
    :param t:  目标串
    :param p:  需要查找的子串 即模式串
    :return:  index or -1
    """
    j, i = 0, 0
    n, m = len(t), len(p)

    while j < n and i < m:
        if t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            j, i = j - i + 1, 0

    if i == m:
        return j - i  # 找到匹配串 返回其初始下标
    return -1  # No matching


# 无回溯匹配  KMP算法    非平凡算法
def matching_kmp(t, p, p_next):
    j, i = 0, 0
    n, m = len(t), len(p)

    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            i = p_next[i]
    if i == m:
        return j - i  # 找到匹配串 返回其初始下标
    return -1  # No matching


# 基础生成p_next的算法
def gen_p_next_0(p):
    i, k, m = 0, -1, len(p)
    p_next = [-1] * m
    while i < m - 1:
        while k >= 0 and p[i] != p[k]:
            k = p_next[k]
        i, k = i + 1, k + 1
        p_next[i] = k
    return p_next


# 改进后生成p_next的算法
def gen_p_next_1(p):
    i, k, m = 0, -1, len(p)
    p_next = [-1] * m
    while i < m - 1:
        while k >= 0 and p[i] != p[k]:
            k = p_next[k]
        i, k = i + 1, k + 1
        if p[i] == p[k]:
            p_next[i] = p_next[k]
        else:
            p_next[i] = k
    return p_next


if __name__ == '__main__':
    des = "1203012031024"
    op = "0301"
    # print(simple_matching(des, op))
    print(matching_kmp(des, op, gen_p_next_1(op)))
