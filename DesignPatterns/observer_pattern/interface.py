"""
@description: 观察者的基本类实现
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-4
"""


class AbstractObserver(object):
    def update(self, tem, hum, pre):
        raise NotImplementedError("Must subclass me")

    def display(self):
        raise NotImplementedError("Must subclass me")


class AbstractSubject(object):
    def register_observer(self, observer):
        raise NotImplementedError("Must subclass me")

    def remove_observer(self, observer):
        raise NotImplementedError("Must subclass me")

    def notify_observers(self):
        raise NotImplementedError("Must subclass me")
