# 4 Инкапсуляция. Определить класс Car, который будет содержать конструктор,
# в котором будет инициализироваться private переменная maxprice,
# а также методы изменения и вывода максимальной стоимости машины.

class Car:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, maxprice = None):
        self.__maxprice = maxprice

    def cost(self, maxcost = None):
        self.maxcost = maxcost

    def maxcost(self):
        return print(self.__maxprice)

cost = Car(1500)
cost.maxcost()
