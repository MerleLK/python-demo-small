"""
@description: insert sort demo
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-7-26
    Test find the first use time is most short to second method.
"""
import time

from myAlgorithms.sort_demos.build_test_value import numbers


def insert_while(nums):
    for index in range(1, len(nums)):
        deal_num = nums[index]
        j = index - 1
        while j >= 0 and nums[j + 1] > deal_num:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = deal_num


def insert_for(nums):
    for index in range(len(nums) - 1):
        for j in range(index + 1, len(nums)):
            if nums[j] < nums[index]:
                nums[j], nums[index] = nums[index], nums[j]

if __name__ == '__main__':

    start = time.time()
    insert_for(numbers)
    # insert_while(numbers)
    end = time.time()
    print(numbers)
    print("cost time is: {}".format(end-start))
