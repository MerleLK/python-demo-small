"""
@description: 旋转数组的最小数字
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/26
@detail:
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
    例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
    NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

    方法一:
        不考虑旋转数组， 其实就是遍历当前数组，找出数组的最小值
"""


class Solution(object):
    def min_number_in_rotate_array(self, rotate_array):
        if not rotate_array:
            return 0

    def find_array_min(self, array):
        return min(array)


if __name__ == '__main__':
    arr = [3, 4, 5, 1, 2]
    s = Solution()
    print(s.find_array_min(arr))
