"""
@description:  束式结构  from 《Python Cookbook》 by Alex Martelli
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-7-31

这种模式不仅可以用于树结构的创建;
在需要一个灵活的对象，其属性可以从构造器中被动态的设置时,也同样可以利用该模式实现。
"""


class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self
x = Bunch(name="Merle", position="Public Relations")
print(x.name)

T = Bunch
t = T(left=T(left="a", right="b"), right=T(left="c"))
print(t)
print(t.left)
print(t.left.right)
print(t['left']['right'])
print("left" in t.right)
print("right" in t.right)
