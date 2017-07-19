"""
@description: this is impl by the second answer from stackoverflow station
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-7-18
"""


def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()
    return property(fget, fset)


class _Const(object):
    @constant
    def FOO(self):
        return 0xBAADFACE

    @constant
    def BAR(self):
        return 0xDEADBEEF

CONST = _Const()

print(CONST.FOO())

CONST.FOO = 0
