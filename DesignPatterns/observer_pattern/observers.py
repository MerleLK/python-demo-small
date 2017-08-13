"""
@description: 观察者们的实现
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-4
"""
from DesignPatterns.observer_pattern.interface import AbstractObserver


class CurrentConditionDisplay(AbstractObserver):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.tem = 0.0
        self.hum = 0.0
        self.pre = 0.0
        # 将自己注册到观察者队列中
        weather_data.register_observer(self)

    def update(self, tem, hum, pre):
        self.tem = tem
        self.hum = hum
        self.pre = pre
        self.display()

    def display(self):
        print("Now the weather data is: \ntemperature: {}°C. \nhumidity: {}%. \n ".format(self.tem, self.hum))


class AllDataShow(AbstractObserver):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.tem = 0.0
        self.hum = 0.0
        self.pre = 0.0
        # 将自己注册到观察者队列中
        weather_data.register_observer(self)

    def update(self, tem, hum, pre):
        self.tem = tem
        self.hum = hum
        self.pre = pre
        self.display()

    def display(self):
        print("Now the data is: \ntemperature: {}°C. \nhumidity: {}%. \npressure: {}MPa."
              "".format(self.tem, self.hum, self.pre))


class TestObserver(AbstractObserver):
    def __init__(self):
        pass


if __name__ == '__main__':
    t = TestObserver()
    print(t)
