"""
Задача 34. Создать класс Годзилла. При создании Годзиллы указывается объем желудка. 
Написать для данного класса метод поедания людей eat. 
В данный метод должен передаваться объем съеденного человека и соответственно уменьшаться место в желудке.
 Когда Годзилла заполнит желудок на 90%, то Годзилла должен говорить он наелся и больше не может поедать людей.
"""
import math
import random

class Godzilla():
    fill_stomach = 0 # глобальный счетчик получается у меня это
    PERCENT_FILL = 90/100


    def __init__(self, name, age, stomach_value):
        self.name = name
        self.age = age
        self.stomach_value = stomach_value
        # self.total_stomach = self.godzilla_eat
        # print(self.fill_stomach.count(0))
        # print(len(self.fill_stomach))

    def pretty_print(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Stomach_value:', self.stomach_value)
        print('Fill_stomach:', self.fill_stomach)

    def godzilla_eat(self, mass):
        fill_stomach = self.fill_stomach
        if fill_stomach < int(self.stomach_value*self.PERCENT_FILL) and int(fill_stomach + mass) < int(self.stomach_value*self.PERCENT_FILL):
            fill_stomach = fill_stomach + mass
            self.fill_stomach = fill_stomach
            print("Годзилла %s не сытый, и еще может жрать студентов которые не сделали ДЗ" % self.name)
        else:
            print("Годзилла %s наелся, и больше не может жрать студентов которые не сделали ДЗ" % self.name)
            return fill_stomach
        return fill_stomach




godzilla1 = Godzilla('Morty', 10, 1000)
for i in range(int(godzilla1.stomach_value/75)+int(godzilla1.age/2)):
    godzilla1.godzilla_eat(random.randint(25, 100))

godzilla2 = Godzilla("Rik", 20, 2500)
for j in range(int(godzilla2.stomach_value / 75) + int(godzilla2.age / 2)):
    godzilla2.godzilla_eat(random.randint(25, 100))




godzilla1.pretty_print()
print("=================")
godzilla2.pretty_print()
