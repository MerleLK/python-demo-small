"""
@description: 测试观察者模式
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-4
"""
from DesignPatterns.observer_pattern.subjects import WeatherData
from DesignPatterns.observer_pattern.observers import CurrentConditionDisplay, AllDataShow

if __name__ == '__main__':
    w = WeatherData()
    c = CurrentConditionDisplay(w)
    w.set_data(12, 30, 1.5)

    a = AllDataShow(w)
    w.set_data(27, 50, 1.6)
