import math
# print('''Условия задачи:
#  Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости. Каждая окружность задается координатами центра и радиусом.
# def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
# ''')
#
#
# def circles_intersect(x1, y1, r1, x2, y2, r2):
#     if ((math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)) <= r1 + r2) and
#                     (math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)) >= math.fabs(r1 - r2))):
#         return True
#     else:
#         return False
#
#
#
# if circles_intersect(0, 0, 5, 0, 1, 1):
#         print('Окружности пересекаются')
# else:
#         print('Окружности не пересекаются')



def circles_intersect(x1, y1, r1, x2, y2, r2):
    # что бы найти длину между центрами окружости, рассмотрим 2 прямоугольных треугольника и найдем их гипотенузы
    dif_x = math.fabs(x2 - x1)  # расстояние между центрами по оси Х
    dif_y = math.fabs(y2 - y1)  # расстояние между центрами по оси Y
    if dif_x == 0:
        if dif_y == 0:
            if math.fabs(r1) == math.fabs(r2):
                return True
            else:
                return False
        else:
            y3 = dif_y / 2
            y3_x1 = math.sqrt(pow(x1, 2) + pow(y3, 2))
            print(y3_x1)  # гипотенуза 1 треугольника

            y3_x2 = math.sqrt(pow(x2, 2) + pow(y3, 2))
            print(y3_x2)  # гипотенуза 2 треугольника

            # зная гипотенузы , найдем углы между гипотенузой и нижним катетом
            cos_alfa_radians = y3 / y3_x1
            print(cos_alfa_radians)
            cos_alfa_degrees = (math.acos(cos_alfa_radians) * 180 / math.pi)
            print(cos_alfa_degrees)  # угол первого треугольника

            cos_beta_radians = y3 / y3_x2
            print(cos_beta_radians)
            cos_beta_degrees = (math.acos(cos_beta_radians) * 180 / math.pi)
            print(cos_beta_degrees)  # угол второго треугольника

            ''' зная 2 угла прямоугольных треугольников, вычислим угол треугольника образующегося между центрами окружностей
            и общей точкой прямоугольных треугольников
            '''
            cos_delta = 180 - cos_alfa_degrees - cos_beta_degrees
            print(cos_delta)  # угол искомого треугольника

            # зная 2 стороны и угол, найдем третью сторону треугольника и соответсвенно длину между центрами окружностей

            z = math.sqrt((math.pow(y3_x1, 2) + math.pow(y3_x2, 2) - 2 * y3_x1 * y3_x2 * math.cos(math.radians(cos_delta))))
            print(z)  # длина между центрами окружостей

            # теперь вернемся к задаче определения пересикаются ли окружности

            if z <= r1 + r2 and z >= math.fabs(r2 - r1):
                return True
            else:
                return False
    else:
        print(dif_x)
        x3 = dif_x / 2  # длина нижнего катета у обоих треугольников
        x3_y1 = math.sqrt(pow(x3, 2) + pow(y1, 2))
        print(x3_y1)  # гипотенуза 1 треугольника

        x3_y2 = math.sqrt(pow(x3, 2) + pow(y2, 2))
        print(x3_y2)  # гипотенуза 2 треугольника

        # зная гипотенузы , найдем углы между гипотенузой и нижним катетом
        cos_alfa_radians = x3 / x3_y1
        print(cos_alfa_radians)
        cos_alfa_degrees = (math.acos(cos_alfa_radians) * 180 / math.pi)
        print(cos_alfa_degrees)  # угол первого треугольника

        cos_beta_radians = x3 / x3_y2
        print(cos_beta_radians)
        cos_beta_degrees = (math.acos(cos_beta_radians) * 180 / math.pi)
        print(cos_beta_degrees)  # угол второго треугольника

        ''' зная 2 угла прямоугольных треугольников, вычислим угол треугольника образующегося между центрами окружностей
        и общей точкой прямоугольных треугольников
        '''
        cos_delta = 180 - cos_alfa_degrees - cos_beta_degrees
        print(cos_delta)  # угол искомого треугольника

        # зная 2 стороны и угол, найдем третью сторону треугольника и соответсвенно длину между центрами окружностей

        z = math.sqrt(
            (math.pow(x3_y1, 2) + math.pow(x3_y2, 2) - 2 * x3_y1 * x3_y2 * math.cos(math.radians(cos_delta))))
        print(z)  # длина между центрами окружостей

        # теперь вернемся к задаче определения пересикаются ли окружности

        if z <= r1 + r2 and z >= math.fabs(r2 - r1):
            return True
        else:
            return False



if circles_intersect(0, 0, 5, 0, 1, 1):
        print('Окружности пересекаются')
else:
        print('Окружности не пересекаются')