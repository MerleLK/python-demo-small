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
        这种方法肯定是不推荐的，因为没有利用到旋转数组的特性。
    方法二:
        考虑到旋转数组的特性，我们可以把当前数组分为两个已经部分有序的子数组
        前半部分始终是大于后半部分的元素的。并且最小的数字是这两个数组的分界点。

        我们可以进行二分查找，首先取到数组的第一个元素pre_num和数组的最后一个元素back_num，
        接着我们循环取到数组的中间元素mid_num，
        如果mid_num大于或者等于pre_num那么它就是属于前面子数组的。
        如果mid_num小于或者等于back_num那么它就是属于后面子数组的。
        我们替换掉对应的pre_num和back_num, 那么我们就可以缩小最小的数字存在的范围，
        结束条件就是pre_num指向前一个数组的最后一个数字，
        back_num指向后一个数组的第一个元素。
        并且下标是连续的。

        例外情况，如果数组的完全反转的，这个就要加上一个判断。

        第一个数字小于最后一个数字，就是完全反转、。

"""


class Solution(object):
    def min_number_in_rotate_array(self, rotate_array):
        if not rotate_array:
            return 0
        if rotate_array[0] <= rotate_array[-1]:
            return rotate_array[0]
        pre_num = rotate_array[0]
        back_num = rotate_array[-1]

        while pre_num != rotate_array[rotate_array.index(back_num) - 1]:
            mid_num = rotate_array[len(rotate_array) // 2]
            if mid_num >= pre_num:
                pre_num = mid_num
            elif mid_num <= back_num:
                back_num = mid_num
            else:
                pass
            rotate_array = rotate_array[rotate_array.index(pre_num): rotate_array.index(back_num) + 1]

        return back_num

    def find_array_min(self, array):
        return min(array)


if __name__ == '__main__':
    arr = [3, 4, 5, 1, 1, 2, 2]

    arr = [6501, 6828, 6963, 7036, 7422, 7674, 8146, 8468, 8704, 8717, 9170, 9359, 9719, 9895, 9896, 9913, 9962, 154,
           293, 334, 492, 1323, 1479, 1539, 1727, 1870, 1943, 2383, 2392, 2996, 3282, 3812, 3903, 4465, 4605, 4665,
           4772, 4828, 5142, 5437, 5448, 5668, 5706, 5725, 6300, 6335]
    arr = [1, 1, 2, 3, 3, 4, 6, 7, 8, 10]
    s = Solution()
    # print(s.find_array_min(arr))
    print(s.min_number_in_rotate_array(arr))
