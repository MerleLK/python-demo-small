"""
@description: 替换空格
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/24 
"""


class Solution:
    # s 源字符串
    def replace_space(self, s):
        # write code here
        return "%20".join(s.split(" "))


if __name__ == '__main__':
    st = "We are Happy!"
    print(Solution().replace_space(st))
