"""
@description: 匹配ip列表
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/26
@detail:
    输入一个ip列表，和 一个ip段列表， 对ip和所属的ip段组队。
    简化操作， 可以对 数字和数字区间进行匹配
"""


def cmp_ip(ips, ip_array):
    ips = sorted(ips, reverse=False)
    ip_array = sorted(ip_array, key=lambda x: x[0], reverse=False)

    result_dict = {}
    i = 0
    for ip in ips:
        current_index = 0
        while i < len(ip_array):
            if ip in range(ip_array[i][0], ip_array[i][1]):
                result_dict[ip] = ip_array[i]
                current_index = i
                break
            else:
                i += 1
        if i >= len(ip_array):
            i = current_index
            result_dict[ip] = None
    return result_dict


if __name__ == '__main__':
    num = [3, 6, 13]
    nums = [[1, 3], [4, 8]]
    print(cmp_ip(num, nums))
