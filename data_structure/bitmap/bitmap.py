"""
@description: the structure bitmap impl
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-8
"""


class Bitmap(object):
    def __init__(self, max):
        self.size = int((max + 31 - 1) / 31)
        self.array = [0 for i in range(self.size)]

    def bit_index(self, num):
        return num % 31

    def set(self, num):
        elem_index = num / 31
        byte_index = self.bit_index(num)
        elem = self.array[elem_index]
        self.array[elem_index] = elem | (1 << byte_index)

    def test(self, i):
        elem_index = i / 31
        byte_index = self.bit_index(i)
        if self.array[elem_index] & (1 << byte_index):
            return True
        return False


if __name__ == '__main__':
    MAX = ord('z')
    suffle_array = [x for x in 'coledraw']
    result = []
    bitmap = Bitmap(MAX)
    for c in suffle_array:
        bitmap.set(ord(c))
    for i in range(MAX + 1):
        if bitmap.test(i):
            result.append(chr(i))
    print("origin data is:{}".format(suffle_array))
    print("sorted data is: {}".format(result))
