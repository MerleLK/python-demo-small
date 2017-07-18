"""
@description: This file is to customize the const variable for your project.
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-7-18
"""
import sys


class CustomerConst(object):

    """
    How to use:
        in other modules you can use it like this.

        from customize_module import customize_constant
        customize_constant.MY_CONSTANT = 1

    """
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    # 自定义__setattr__ 函数， 对相关的数据进行检查
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't change const.'{}'".format(name))

        if not name.isupper():
            raise self.ConstCaseError("const name '{}' is not all uppercase!".format(name))

        self.__dict__[name] = value


# register the CustomerConst to sys.modules
# 把自定义的常量类注册到系统模块的全局字典中.
custom_constant = CustomerConst()
sys.modules[__name__] = custom_constant

# those you defined constants
custom_constant.MY_CONSTANT = 1
custom_constant.MY_SECOND_CONSTANT = 2
