"""
Задача 35.Создать два класса: Окружность и Точка.
Создать в классе окружности метод, который принимает в качестве параметра точку и проверяет находится ли данная точка внутри окружности.
"""
import math

class Circle():


    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r



    def pretty_print(self):
        print('Circle with center:')
        print('x=', self.x)
        print('y=', self.y)
        print('Radius:', self.r)


    def check_point(self):
        a = int(input('Enter the coordinates of the point along the x axis:'))
        b = int(input('Enter the coordinates of the point along the y axis:'))

        if math.pow((self.x - a), 2) + math.pow((self.y - b), 2) <= math.pow((self.r), 2):
            print('Точка находится в окружности')
        else:
            print('Точка не попадает в окружность')



circle1 = Circle(2, 5, 10)
circle1.check_point()
print('================')
circle1.pretty_print()


