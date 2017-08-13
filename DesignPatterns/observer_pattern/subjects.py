"""
@description: 主题们的实现
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-4
"""
from DesignPatterns.observer_pattern.interface import AbstractSubject


class WeatherData(AbstractSubject):
    def __init__(self):
        self.observers = []
        self.tem = 0.0
        self.hum = 0.0
        self.pre = 0.0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def get_tem(self):
        return self.tem

    def get_hum(self):
        return self.hum

    def get_pre(self):
        return self.pre

    def set_data(self, tem, hum, pre):
        self.tem = tem
        self.hum = hum
        self.pre = pre
        # print(self.observers)
        self.data_changed()

    def data_changed(self):
        self.notify_observers()

    def notify_observers(self):
        for ob in self.observers:
            ob.update(self.tem, self.hum, self.pre)


if __name__ == '__main__':
    wea = WeatherData()
