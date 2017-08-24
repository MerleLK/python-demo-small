"""
@description: 二位数组中的查找
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-9
"""


class Solution:
    def find(self, target, array):
        # write code here
        if array == [[]]:
            return False
        for row in array:
            if target <= row[len(row) - 1]:
                if row.count(target) != 0:
                    return True
            else:
                pass
        return False


if __name__ == '__main__':
    arr = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    tar = 5
    print(Solution().find(target=tar, array=arr))
