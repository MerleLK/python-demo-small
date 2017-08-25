"""
@description: 非递归遍历所有文件夹
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/25 
"""

import os


def scan_dir(path):
    dir_list = []
    file_count = 0

    if os.path.isfile(path):
        file_count += 1
        return file_count

    for i in os.listdir(path):
        dir_list.append(path + "\\" + i)

    i = 0
    while len(dir_list) != 0:
        if os.path.isfile(dir_list[i]):
            file_count += 1
            dir_list.remove(dir_list[i])
        else:
            for k in os.listdir(dir_list[i]):
                path = dir_list[i]
                dir_list.append(path + "\\" + k)
            dir_list.remove(dir_list[i])
    return file_count


if __name__ == '__main__':
    p = "F:\MyProjects"
    p = "F:\OtherProjects"
    p = "F:\MyProjects\DjangoProjects"
    print(scan_dir(p))
