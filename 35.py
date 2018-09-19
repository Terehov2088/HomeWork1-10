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
        print('x= %d, y= %d' % (self.x, self.y))
        print('Radius:', self.r)



class Point():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def check_point(self, circle):
        # a = int(input('Enter the coordinates of the point along the x axis:'))
        # b = int(input('Enter the coordinates of the point along the y axis:'))

        if math.pow((circle1.x - self.a), 2) + math.pow((circle1.y - self.b), 2) <= math.pow((circle1.r), 2):
            print('Точка находится в окружности')
        else:
            print('Точка не попадает в окружность')


circle1 = Circle(2, 5, 10)
point = Point(10, 20)
point.check_point(circle1)
print('================')
circle1.pretty_print()


