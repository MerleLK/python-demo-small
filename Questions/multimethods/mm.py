"""
@description:
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-8
"""
registry = {}


class MultiMethods(object):
    def __init__(self, name):
        self.name = name
        self.typemap = {}

    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args)
        _function = self.typemap.get(types)
        if _function is None:
            raise TypeError("no match")
        return _function(*args)

    def register(self, types, _function):
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = _function


def multi_method(*types):
    def register(_function):
        name = _function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethods(name)
        mm.register(types, _function)
        return mm

    return register


if __name__ == '__main__':
    @multi_method(int, int)
    # @multi_method(int)
    def foo(a, b=10):
        print(a + b)

    @multi_method(int)
    def foo1(a2):
        print(a2)


    a1 = "asd"
    b1 = 1

    foo(a1, b1)
    foo1(a1)
